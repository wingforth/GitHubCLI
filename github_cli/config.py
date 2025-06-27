"""
Configuration

GITHUB_TOKEN: GitHub access token.
CACHE_DIR: The directory of HTTP request cache.
"""

from pathlib import Path


def _get_github_token(file: Path) -> str | None:
    """Read GitHub access token from .github-token file in the parent directory.
    Args:
        file (Path): The file where the GitHub token is saved.
    Returns:
        str | None: GitHub access token, or None if not found.
    """

    if not file.exists():
        return None
    with open(file) as fd:
        return fd.read().strip()


_cwd = Path(__file__).resolve().parent.parent
GITHUB_TOKEN = _get_github_token(_cwd / ".github-token")
CACHE_DIR = _cwd / "cache"
