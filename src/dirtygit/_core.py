import logging
import os
import subprocess

logger = logging.getLogger(__name__)


def check() -> str:
    if os.getenv("IGNORE_DIRTYGIT") == "true":
        logger.warning("WARNING - IGNORE_DIRTYGIT IS TRUE. WILL NOT ASSERT CLEAN GIT STATUS.")
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert status.stdout == "", f"Git repo is dirty:\n{status.stdout}"

    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()
