"""Run a command."""
import subprocess as sp

import rich
from loguru import logger


def run_cmd(
    cmd: str,
    mute_stdout: bool = True,
    mute_stderr: bool = False,
    raise_stderr: bool = True,
):
    """
    Execute cmd.

    Args:
    ----
    cmd: command to execute
    mute_stdout: default True, do not output stdout if True
    mute_stderr: default False, do not output stderr if True
    raise_stderr: default True, raise Exception(ret.stderr) if set

    Returns:
    -------
        CompletedProcess(args=cmd, returncode=0|..., stdout='...', stderr='...'
    """
    logger.info(f"\n\t{cmd=}")
    ret = sp.run(cmd, capture_output=True, check=False, shell=True, encoding="utf8")
    if ret.stdout and not mute_stdout:
        rich.print(ret.stdout)
    if ret.stderr and not mute_stderr:
        rich.print("[red bold]" + ret.stderr)
        if raise_stderr:
            raise Exception(ret.stderr)

    return ret
