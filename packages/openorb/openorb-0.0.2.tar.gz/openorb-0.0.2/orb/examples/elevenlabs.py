"""Elevenlabs websockets test."""

import argparse
import asyncio
import base64
import json
import os
import shutil
import subprocess
from typing import AsyncIterator

import websockets as ws
from yarl import URL

FRAME_RATE = 44100

DEFAULT_VOICE_ID = "jl15NxMxnp9NtPqmGDM2"
DEFAULT_MODEL_ID = "eleven_turbo_v2"
DEFAULT_OUTPUT_FORMAT = "mp3_44100_128"


def get_ws_url(
    voice_id: str = DEFAULT_VOICE_ID,
    model_id: str = DEFAULT_MODEL_ID,
    output_format: str = DEFAULT_OUTPUT_FORMAT,
    latency: int = 3,
) -> URL:
    return URL.build(
        scheme="wss",
        host="api.elevenlabs.io",
        path=f"/v1/text-to-speech/{voice_id}/stream-input",
        query={
            "model_id": model_id,
            "output_format": output_format,
            "optimize_streaming_latency": latency,
        },
    )


async def text_chunker(chunks: AsyncIterator[str]) -> AsyncIterator[str]:
    splitters = (".", ",", "?", "!", ";", ":", "—", "-", "(", ")", "[", "]", "}", " ")
    buffer = ""

    async for text in chunks:
        if buffer.endswith(splitters):
            yield buffer + " "
            buffer = text
        elif text.startswith(splitters):
            yield buffer + text[0] + " "
            buffer = text[1:]
        else:
            buffer += text

    if buffer:
        yield buffer + " "


def is_installed(lib_name: str) -> bool:
    return shutil.which(lib_name) is not None


async def stream(audio_stream: AsyncIterator[bytes]) -> None:
    if not is_installed("mpv"):
        raise ValueError("mpv not found, necessary to stream audio.")

    with subprocess.Popen(
        ["mpv", "--no-cache", "--no-terminal", "--", "fd://0"],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ) as mpv_process:
        assert (stdin_stream := mpv_process.stdin) is not None
        async for chunk in audio_stream:
            if chunk:
                stdin_stream.write(chunk)
                stdin_stream.flush()
        stdin_stream.close()
        mpv_process.wait()


class AsyncElevenlabsAgent:
    def __init__(self, audio_wait_timeout: float = 1.0) -> None:
        super().__init__()

        self.token_wait_timeout = audio_wait_timeout

    async def run(self, tokens: AsyncIterator[str]) -> None:
        headers = {"Xi-Api-Key": os.environ["ELEVEN_API_KEY"]}
        bos = json.dumps(
            {
                "text": " ",
                "voice_settings": {
                    "stability": "0.5",
                    "similarity_boost": 0.8,
                },
                "generation_config": {
                    "chunk_length_schedule": [50],
                },
            }
        )
        eos = json.dumps({"text": ""})
        ws_url = str(get_ws_url())
        async with ws.connect(ws_url, extra_headers=headers) as conn:
            await conn.send(bos)

            async def listen() -> AsyncIterator[bytes]:
                while True:
                    try:
                        message = await conn.recv()
                        data = json.loads(message)
                        if audio := data.get("audio"):
                            yield base64.b64decode(audio)
                        elif data.get("isFinal"):
                            break
                    except ws.exceptions.ConnectionClosed:
                        break

            listen_task = asyncio.create_task(stream(listen()))

            async for text in text_chunker(tokens):
                input_data = {"text": text, "try_trigger_generation": True}
                await conn.send(json.dumps(input_data))

            await conn.send(json.dumps(eos))

            await listen_task


async def main() -> None:
    parser = argparse.ArgumentParser(description="Test streaming to the OpenAI API")
    parser.add_argument("-p", "--prompt", type=str, default="Hello, agent. How are you?", help="Prompt to send")
    args = parser.parse_args()

    agent = AsyncElevenlabsAgent()

    async def gen_text() -> AsyncIterator[str]:
        for text in args.prompt.split():
            yield text + " "

    await agent.run(gen_text())


if __name__ == "__main__":
    # python -m orb.examples.elevenlabs
    asyncio.run(main())
