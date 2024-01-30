#!/usr/bin/env python3

## Copyright 2024 David Miguel Susano Pinto <pinto@robots.ox.ac.uk>
##
## Licensed under the Apache License, Version 2.0 (the "License"); you
## may not use this file except in compliance with the License.  You
## may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
## implied.  See the License for the specific language governing
## permissions and limitations under the License.

"""Commands to download, upload, and update VIA projects in VFS.

## Synopsis

    python -m via.vfs download [--url URL] [UUID]
    python -m via.vfs upload [--url URL] [PROJECT-FPATH ...]


## Description --- ``download``

For a given project UUID, download it from the VFS server and display
it on standard output.  This can be redirected to a file or piped to
another tool such as `jq <https://jqlang.github.io/jq/>`__.

### Examples

* Download one project and save it to a file:

      python -m via.vfs download \
          xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
          > this-project.json

* Get current revision number for a project (with `jq`):

      python -m via.vfs download \
          xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
          | jq '.project.shared_rev'

* Get number of annotations in a VIA 3 project (with `jq`):

      python -m via.vfs download \
          xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
          | jq '.metadata | length'

* Get number of annotations in a LISA project (with `jq`):

      python -m via.vfs download \
          xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
          | jq '[.files[].regions | length] | add'

* Get number of files in a LISA project (with `jq`):

      python -m via.vfs download \
          xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
          | jq '.files | length'

### TODO

It should be possible to add an option to download a specific revision
number of a project but I haven't figured if VFS actually supports
that.  Similarly, a new ``list`` subcommand to list all revision
numbers and timestamps for one project would be nice.


## Description --- ``upload``

Upload, or update, project files in a VFS server.  It outputs the
project UUID, revision number, and file paths (separated by tabs), for
each of the successfully uploaded files.

File that fail to upload will be skipped with a notice in stderr (so
that stdout is still safe to use) and cause exit code to be non-zero.

The file path is the *last* column of the output.  It is the last
column because it is the one whose value we have no control over and
it may contain tabs which would cause issues for any automatic use of
the output (file path may also include newlines but if anyone has
newlines on their file paths, they're looking for problems, in which
case we're happy to oblige).


### TODO (maybe)

We decide whether to create a new project or update an existing one
based on whether there's already shared project details on the file.
But it may be interesting to force creation of a new shared project
instead of updating.  But that can be done trivially on shell with:

    python -m via.vfs upload \
        <(jq '.project.shared_fid = "__FILE_ID__"
              | .project.shared_rev = "__FILE_REV_ID__"
              | .project.shared_rev_timestamp = "__FILE_REV_TIMESTAMP__"' \
              project-file.json)

But then again, this tool can be done trivially on shell as well and
here we are.

"""


import argparse
import json
import logging
import sys
from typing import List

import via.vfs

_logger = logging.getLogger(__name__)


def main_download(vfs_url: str, project_uuid: str) -> int:
    project = via.vfs.download(vfs_url, project_uuid)
    json.dump(project, fp=sys.stdout)
    return 0


def main_upload(vfs_url: str, project_fpaths: List[str]) -> int:
    all_succeed = True
    for fpath in project_fpaths:
        try:
            vfs_resp = via.vfs.upload_file(vfs_url, fpath)
        except Exception as ex:
            _logger.error("failed to upload '%s': %s", fpath, ex)
            all_succeed = False
        else:
            print(f"{vfs_resp.uuid}\t{vfs_resp.rev}\t{fpath}")

    return 0 if all_succeed else 1


def main(argv: List[str]) -> int:
    logging.basicConfig()
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action")

    # download project
    download_subparser = subparsers.add_parser(
        "download",
        help="Download project from VFS server",
        description=(
            "For a given project UUID, download it from the VFS server and"
            " display it on standard output.  If you want to save it to a"
            " file, redirect stdout to that file."
        ),
    )
    download_subparser.add_argument(
        "--url",
        default="https://meru.robots.ox.ac.uk/store/",
        metavar="VFS-URL",
        help="URL of the VFS server",
    )
    download_subparser.add_argument(
        "project_uuid",
        help="UUID of the project to be downloaded",
    )

    # upload project
    upload_subparser = subparsers.add_parser(
        "upload",
        help="Upload (or update) project to VFS server",
        description=(
            "Upload, or update, project files in a VFS server.  It outputs"
            " the project UUID, revision number, and file paths separated by"
            " tabs."
        ),
    )
    upload_subparser.add_argument(
        "--url",
        default="https://meru.robots.ox.ac.uk/store/",
        metavar="VFS-URL",
        help="URL of the VFS server",
    )
    upload_subparser.add_argument(
        "project_fpaths",
        nargs="+",
        help="Filepath for the projects to be uploaded",
    )

    args = parser.parse_args(argv[1:])
    if args.action == "download":
        return main_download(args.url, args.project_uuid)
    elif args.action == "upload":
        return main_upload(args.url, args.project_fpaths)
    else:
        # We should not get here because `parse_args` should error on
        # unknown actions.
        raise Exception(f"Unknown action {args.action}")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
