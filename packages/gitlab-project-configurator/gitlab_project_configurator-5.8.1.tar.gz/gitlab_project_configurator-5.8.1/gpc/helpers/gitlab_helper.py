# Standard Library
from typing import Union  # pylint: disable=unused-import

# Third Party Libraries
import boltons.cacheutils
import gitlab.const

from boltons.urlutils import parse_url
from gitlab import Gitlab  # pylint: disable=unused-import
from gitlab.exceptions import GitlabGetError

# Gitlab-Project-Configurator Modules
from gpc.helpers.exceptions import GpcUserError
from gpc.helpers.types import ProjectName
from gpc.helpers.types import Url


cache_users = boltons.cacheutils.LRI(10000)
cache_users_id = boltons.cacheutils.LRI(10000)
cache_groups = boltons.cacheutils.LRI(10000)
cache_subgroups = boltons.cacheutils.LRI(10000)
cache_allgroups = boltons.cacheutils.LRI(10000)

VISIBILITY_VALUES = ["internal", "private", "public"]
MERGE_METHODS = ["merge", "rebase_merge", "ff"]
SQUASH_OPTIONS = {
    "do not allow": "never",
    "allow": "default_off",
    "encourage": "default_on",
    "require": "always",
}
INV_SQUASH_OPTIONS = {
    "never": "do not allow",
    "default_off": "allow",
    "default_on": "encourage",
    "always": "require",
}

MAP_ACCESS = {
    "no one": 0,
    "none": 0,
    "maintainers": gitlab.const.MAINTAINER_ACCESS,
    "guests": gitlab.const.GUEST_ACCESS,
    "reporters": gitlab.const.REPORTER_ACCESS,
    "owners": gitlab.const.OWNER_ACCESS,
    "developers": gitlab.const.DEVELOPER_ACCESS,
    "admins": 60,
}

MAP_ACCESS_REVERT = {
    0: "no one",
    gitlab.const.MAINTAINER_ACCESS: "maintainers",
    gitlab.const.GUEST_ACCESS: "guests",
    gitlab.const.REPORTER_ACCESS: "reporters",
    gitlab.const.OWNER_ACCESS: "owners",
    gitlab.const.DEVELOPER_ACCESS: "developers",
    60: "admins",
}


@boltons.cacheutils.cached(cache_users)
def get_user_by_username(gl: Gitlab, username):
    users = gl.users.list(username=username, retry_transient_errors=True)
    if users:
        # The username is an unique field
        return users[0]  # type: ignore
    raise GpcUserError(f"User {username} does not exist")


@boltons.cacheutils.cached(cache_users_id)
def get_user_by_id(gl: Gitlab, user_id):
    return gl.users.get(user_id, retry_transient_errors=True)


@boltons.cacheutils.cached(cache_groups)
def get_group(gl: Gitlab, group_path):
    return gl.groups.get(group_path, retry_transient_errors=True)


@boltons.cacheutils.cached(cache_subgroups)
def _get_subgroups(gl: Gitlab, group_path):
    group = get_group(gl, group_path)
    subgroups = []
    if group.shared_with_groups:
        subgroups = [x.get("group_full_path") for x in group.shared_with_groups]
    return subgroups


@boltons.cacheutils.cached(cache_allgroups)
def get_subgroups(gl: Gitlab, group_path):
    all_groups = []
    subgroups = _get_subgroups(gl, group_path)
    if not subgroups:
        return []
    all_groups.extend(subgroups)
    for subgroup in subgroups:
        all_groups.extend(_get_subgroups(gl, subgroup))
    return all_groups


def clean_gitlab_project_name(project_name_or_url: Union[ProjectName, Url]) -> ProjectName:
    if project_name_or_url.startswith("https://"):
        o = parse_url(project_name_or_url)
        project_name = o["path"]
    else:
        project_name = project_name_or_url
    project_name = project_name.strip("/").lower()
    if project_name.endswith(".git"):
        project_name = project_name[:-4]
    return project_name


def is_archived_project(gl: Gitlab, project_path):
    gl_project = gl.projects.get(project_path)
    return gl_project.archived


def is_shared_project(project, group):
    return group.full_path in (sg["group_full_path"] for sg in project.shared_with_groups)


def is_existing_project(gl: Gitlab, project_path):
    try:
        gl.projects.get(project_path)
        return True
    except GitlabGetError:
        return False


def is_existing_group(gl: Gitlab, group_path):
    try:
        gl.groups.get(group_path)
        return True
    except GitlabGetError:
        return False
