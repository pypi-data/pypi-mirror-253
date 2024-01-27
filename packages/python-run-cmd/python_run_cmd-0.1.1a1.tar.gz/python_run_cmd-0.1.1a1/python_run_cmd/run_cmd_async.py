"""Run subcommands asynchronously."""
import asyncio
import os
from shlex import split
from typing import List, Union


async def run_cmd_async(cmd: Union[str, List[str]]):
    """
    Run subcommands asynchronously.

    https://github.com/jmorganca/ollama/blob/main/examples/jupyter-notebook/ollama.ipynb
    """
    if isinstance(cmd, str):
        cmd = split(cmd, posix=os.name in ["posix"])
    print(">>> starting", *cmd)
    p = await asyncio.subprocess.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    async def pipe(lines):
        async for line in lines:
            print(line.strip().decode("utf-8"))

    await asyncio.gather(
        pipe(p.stdout),
        pipe(p.stderr),
    )


async def main():
    return await asyncio.gather(
        # run(['ollama', 'serve']),
        # run(['ngrok', 'http', '--log', 'stderr', '11434']),
        run_cmd_async("ping www.baidu.com"),
        run_cmd_async("ls"),
        run_cmd_async("py -m http.server"),
    )


if __name__ == "__main__":
    asyncio.run(main())

    # this works up to python 3.10, but not python 3.11
    # asyncio.run(
    # asyncio.wait([
    # run_cmd_async("ping www.baidu.com"),
    # run_cmd_async("ls")
    # ])
    # )

    # run in colab/ipython/jupyter:
    # await asyncio.gather(
    #   run("ping www.baidu.com"),
    #   run("ls"),
    # )
