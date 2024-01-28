"""Runs the virtual orb on your computer."""

import asyncio

from orb.api.tk import TkApp
from orb.impl.openai_elevenlabs import OpenAIElevenlabsOrb


async def main() -> None:
    orb = OpenAIElevenlabsOrb()
    app = TkApp(orb)
    await app.start()


if __name__ == "__main__":
    # python -m orb.cli.virtual
    asyncio.run(main())
