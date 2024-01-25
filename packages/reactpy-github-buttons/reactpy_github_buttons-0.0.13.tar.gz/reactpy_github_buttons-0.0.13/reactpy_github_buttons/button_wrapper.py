from os import environ
from typing import Optional
from enum import Enum
from pathlib import Path

from reactpy.web.module import export, module_from_file


# class syntax


class ColorScheme(str, Enum):
    LIGHT = "light"
    LIGHT_HIGH_CONTRAST = "light_high_contrast"
    DARK = "dark"
    DARK_DIMMED = "dark-dimmed"
    DARK_HIGH_CONTRAST = "dark_high_contrast"


def make_color_scheme(
    no_preference: ColorScheme, light: ColorScheme, dark: ColorScheme
) -> str:
    """Create button color scheme"""
    return f"no-preference: {no_preference.value}; light: {light.value}; dark: {dark.value};"


# pylint: disable=missing-function-docstring, dangerous-default-value
# pylint: disable=disable=invalid-name, too-many-arguments

_js_module = module_from_file(
    "reactpy_github_buttons",
    file=Path(__file__).parent/"bundle.dev.js" if environ.get("REACTPY_DEBUG_MODE") else Path(__file__).parent/"bundle.min.js" ,
    fallback="⏳",
)

_RactpyGithubButtons = export(_js_module, "RactpyGithubButtons")


def GithubButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    props: dict = {},
    large=False,
    show_count=False,
    standard_icon=False,
    color_scheme="",
):
    """Wrapper for github-buttons library. For API and examples see:

    https://github.com/buttons/github-buttons
    """

    _args = {"href": f"https://github.com/{user}/{repo}", **props}

    if large:
        _args.update({"data-size": "large"})

    if show_count:
        _args.update({"data-show-count": "true"})

    if standard_icon and 'data-icon' in _args:
        _args.pop("data-icon")

    if color_scheme:
        _args.update({"data-color-scheme": color_scheme})

    if not user:
        del _args["href"]

    if "text" in props:
        _args["data_text"] = props["text"]

    # log.info("args=[%s]", _args)

    return _RactpyGithubButtons(_args)


def FollowButton(
    user: Optional[str] = None, large=False, show_count=False, color_scheme=""
):
    props = {
        "text": "Follow @buttons",
        "aria-label": "Follow @buttons on GitHub",
        "href": f"https://github.com/{user}",
    }

    return GithubButton(
        user=user,
        props=props,
        large=large,
        show_count=show_count,
        color_scheme=color_scheme,
    )


def SponsorButton(
    user: Optional[str] = None, large=False, standard_icon=False, color_scheme=""
):
    props = {
        "text": "Sponsor",
        "data-icon": "octicon-heart",
        "aria-label": "Sponsor @buttons on GitHub",
        "href": f"https://github.com/sponsors/{user}",
    }

    return GithubButton(
        user=user,
        props=props,
        large=large,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def WatchButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    show_count=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Watch",
        "data-icon": "octicon-eye",
        "aria-label": "Watch buttons/github-buttons on GitHub",
        "href": f"https://github.com/{user}/{repo}/subscription",
    }

    return GithubButton(
        user=user,
        props=props,
        large=large,
        show_count=show_count,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def StarButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    show_count=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Star",
        "data-icon": "octicon-star",
        "aria-label": "Star buttons/github-buttons on GitHub",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        show_count=show_count,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def ForkButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    show_count=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Fork",
        "data-icon": "octicon-repo-forked",
        "aria-label": "Fork buttons/github-buttons on GitHub",
        "href": f"https://github.com/{user}/{repo}/fork",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        show_count=show_count,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def IssueButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    show_count=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Issue",
        "data-icon": "octicon-issue-opened",
        "aria-label": "Issue buttons/github-buttons on GitHub",
        "href": f"https://github.com/{user}/{repo}/issues",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        show_count=show_count,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def DiscussButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Discuss",
        "data-icon": "octicon-comment-discussion",
        "aria-label": "Discuss buttons/github-buttons on GitHub",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def DownloadButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Download",
        "data-icon": "octicon-download",
        "aria-label": "Download buttons/github-buttons on GitHub",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def InstallPackageButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Install this package",
        "data-icon": "octicon-package",
        "aria-label": "Install this package buttons/github-buttons on GitHub",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def UseTemplateButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Use this template",
        "data-icon": "octicon-repo-template",
        "aria-label": "Use this template buttons/github-buttons on GitHub",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )


def UseThisGitHubActionButton(
    user: Optional[str] = None,
    repo: Optional[str] = None,
    large=False,
    standard_icon=False,
    color_scheme="",
):
    props = {
        "text": "Use this GitHub Action",
        "data-icon": "octicon-play",
        "aria-label": "Use this GitHub Action buttons/github-buttons on GitHub",
    }

    return GithubButton(
        user=user,
        repo=repo,
        props=props,
        large=large,
        standard_icon=standard_icon,
        color_scheme=color_scheme,
    )
