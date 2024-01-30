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

import json
import logging
import re
from typing import Dict, NamedTuple, TypedDict, cast

import requests

_logger = logging.getLogger(__name__)


MAGIC_FID = "__FILE_ID__"
MAGIC_REV = "__FILE_REV_ID__"
MAGIC_TIMESTAMP = "__FILE_REV_TIMESTAMP__"


class VFSPostResponse(NamedTuple):
    uuid: str
    rev: int


class ProjectInfo(TypedDict):
    """This is the 'project' field of a `Project` instance.

    Yes, the naming is confusing.  The `Project` class is the object
    and the value of the `project` field is `ProjectInfo`.  But if we
    name this `Project` what do we call the actual stuff stored in
    VFS?  That things is currently named project.  The naming here
    matches what's used in the vfs source code.

    This will be more confusing if a project ever gains a `info`
    field.

    """

    shared_fid: str
    shared_rev: str
    shared_rev_timestamp: str


class Project(TypedDict):
    """The project object/json stored in a VFS server."""

    project: ProjectInfo


def is_uuid(maybe_uuid: str) -> bool:
    return bool(
        re.fullmatch(
            "[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}",
            maybe_uuid,
        )
    )


def is_str_pos_int(maybe_pos_int: str) -> bool:
    return bool(re.fullmatch("[1-9][0-9]*", maybe_pos_int))


def is_str_nneg_int(maybe_nneg_int: str) -> bool:
    return bool(re.fullmatch("[0-9]+", maybe_nneg_int))


def is_new_project(project_json: Project) -> bool:
    fid = project_json["project"]["shared_fid"]
    rev = project_json["project"]["shared_rev"]
    timestamp = project_json["project"]["shared_rev_timestamp"]
    return (
        fid == MAGIC_FID and rev == MAGIC_REV and timestamp == MAGIC_TIMESTAMP
    )


def is_shared_project(project_json: Project) -> bool:
    fid = project_json["project"]["shared_fid"]
    rev = project_json["project"]["shared_rev"]
    timestamp = project_json["project"]["shared_rev_timestamp"]
    return is_uuid(fid) and is_str_pos_int(rev) and is_str_nneg_int(timestamp)


def is_project(json_obj: Dict) -> bool:
    """Check whether a dict is a valid project for VFS."""
    # We already list the required fields in the TypedDict
    # declarations.  Would be nice if we could just use them to
    # simplify this check.  At the moment it seems doing it requires a
    # dependency on external dependencies like pydantic (that I don't
    # want to bring in).

    if "project" not in json_obj:
        return False

    for key in ProjectInfo.__required_keys__:
        if key not in json_obj["project"]:
            _logger.warning(
                "required key obj.project.{%s} does not exist", key
            )
            return False

    project_json = cast(Project, json_obj)
    if not is_shared_project(project_json) and not is_new_project(
        project_json
    ):
        _logger.warning(
            "invalid shared fid, rev, and rev_timestamp combination"
        )
        return False

    return True


def download(vfs_url: str, project_uuid: str) -> Project:
    if not is_uuid(project_uuid):
        raise Exception(f"Invalid UUID '{project_uuid}'")

    if vfs_url.endswith("/"):
        url = vfs_url + project_uuid
    else:
        url = vfs_url + "/" + project_uuid
    _logger.debug("Downloading '%s' from '%s'", project_uuid, url)
    resp = requests.get(url)
    resp.raise_for_status()

    obj = resp.json()
    if not is_project(obj):  # maybe this optional?
        raise Exception("Downloaded file is not a valid VFS project")
    return obj


def _vfs_post(url: str, project_json: Project) -> VFSPostResponse:
    resp = requests.post(url, json=project_json)
    resp.raise_for_status()
    obj = resp.json()
    return VFSPostResponse(uuid=obj["shared_fid"], rev=obj["shared_rev"])


def upload_new_project(vfs_url: str, project_json: Project) -> VFSPostResponse:
    """Upload to VFS server (creating a new project)"""
    return _vfs_post(vfs_url, project_json)


def upload_updated_project(
    vfs_url: str, project_json: Project
) -> VFSPostResponse:
    rev = project_json["project"]["shared_rev"]
    uuid = project_json["project"]["shared_fid"]
    sep = "" if vfs_url.endswith("/") else "/"
    url = f"{vfs_url}{sep}{uuid}?rev={rev}"

    # Shallow copy to modify these two keys which will be
    # updated/replaced on VFS.
    project_copy = project_json.copy()
    project_copy["project"] = project_copy["project"].copy()
    project_copy["project"]["shared_rev"] = MAGIC_REV
    project_copy["project"]["shared_rev_timestamp"] = MAGIC_TIMESTAMP

    return _vfs_post(url, project_copy)


def upload_project(vfs_url: str, project_json: Project) -> VFSPostResponse:
    if is_new_project(project_json):
        return upload_new_project(vfs_url, project_json)
    elif is_shared_project(project_json):
        return upload_updated_project(vfs_url, project_json)
    else:
        # We should not get here unless we are not handling a valid
        # project.
        raise Exception("Not a new or a shared project")


def upload_file(vfs_url: str, fpath: str) -> VFSPostResponse:
    with open(fpath, "r") as fh:
        project_json = json.load(fh)
    if not is_project(project_json):
        raise Exception(f"File '{fpath}' is not a valid project file")
    return upload_project(vfs_url, project_json)
