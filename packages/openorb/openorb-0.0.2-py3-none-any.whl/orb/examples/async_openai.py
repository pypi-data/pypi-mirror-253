"""OpenAI async API test."""

import argparse
import asyncio
import io
import sys
import tempfile
from pathlib import Path
from types import TracebackType
from typing import AsyncIterable, Literal, TypedDict, cast

import numpy as np
import openai
import sounddevice as sd
from openai.resources.chat.completions import AsyncStream, ChatCompletionChunk
from pydub import AudioSegment

FRAME_RATE = 22050

DEFAULT_PROMPT = "You are a helpful call agent."


class StartEndNotifier:
    """Prints a message when the context manager is entered and exited."""

    def __init__(self, message: str, end_message: str = "Done") -> None:
        super().__init__()

        self.message = message
        self.end_message = end_message

    async def __aenter__(self) -> None:
        print(self.message, end="", flush=True, file=sys.stderr)

    async def __aexit__(
        self, _t: type[BaseException] | None, _e: BaseException | None, _tr: TracebackType | None
    ) -> None:
        print(f" {self.end_message}", flush=True, file=sys.stderr)


async def record_audio(duration: float = 1.0) -> np.ndarray:
    async with StartEndNotifier("Recording..."):
        audio = sd.rec(int(duration * FRAME_RATE), samplerate=FRAME_RATE, channels=1)
        sd.wait()
    return audio


async def play_audio(audio_data: np.ndarray) -> None:
    audio = np.frombuffer(audio_data, dtype=np.int16)
    async with StartEndNotifier("Playing response..."):
        sd.play(audio, FRAME_RATE)
        sd.wait()


class Message(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


class AsyncOpenAIAgent:
    def __init__(self, prompt: str = DEFAULT_PROMPT) -> None:
        super().__init__()

        self.client = openai.AsyncOpenAI()
        self.messages: list[Message] = [{"role": "system", "content": prompt}]

    async def transcribe(self, user_speech: np.ndarray) -> str:
        """Transcribes the user speech to text using the OpenAI API.

        Args:
            user_speech: The user's speech as bytes.

        Returns:
            The model response as text.
        """
        user_speech_bytes = np.int16(user_speech * 32767).tobytes()
        audio = AudioSegment.from_file(
            io.BytesIO(user_speech_bytes),
            format="raw",
            frame_rate=FRAME_RATE,
            channels=1,
            sample_width=2,
        )
        with tempfile.NamedTemporaryFile(suffix=".wav") as f:
            audio.export(f.name, format="wav")
            f.seek(0)
            transcript = await self.client.audio.transcriptions.create(
                file=Path(f.name),
                model="whisper-1",
                language="en",
                response_format="text",
            )
        return cast(str, transcript)

    async def get_response(self, text: str) -> AsyncIterable[str]:
        """Gets the model response using the OpenAI API.

        Args:
            text: The text to prompt the model with.

        Returns:
            The model response as text.
        """
        self.messages.append({"role": "user", "content": text})
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages,  # type: ignore[arg-type]
            stream=True,
        )
        chunk_texts = []
        try:
            async for chunk in cast(AsyncStream[ChatCompletionChunk], response):
                chunk_text = chunk.choices[0].delta.content
                if chunk_text:
                    yield chunk_text
                    chunk_texts.append(chunk_text)
        finally:
            content = "".join(chunk_texts)
            self.messages.append({"role": "assistant", "content": content})

    async def say(self, text: str) -> AsyncIterable[np.ndarray]:
        """Synthesizes the text to speech using the OpenAI API.

        Args:
            text: The text to synthesize.

        Returns:
            The model response as audio bytes.
        """
        async with self.client.audio.speech.create(
            input=text,
            model="tts-1",
            voice="alloy",
            response_format="mp3",
        ) as response:
            with tempfile.NamedTemporaryFile(suffix=".mp3") as f:
                await response.stream_to_file(f.name)
                audio = AudioSegment.from_mp3(f.name)
                yield audio.raw_data


async def main() -> None:
    parser = argparse.ArgumentParser(description="Test streaming to the OpenAI API")
    parser.add_argument("-d", "--duration", type=float, default=1.0, help="Duration of recording in seconds")
    parser.add_argument("-n", "--num-repeats", type=int, default=1, help="Number of times to repeat")
    args = parser.parse_args()

    agent = AsyncOpenAIAgent()

    for _ in range(args.num_repeats):
        recorded_audio = await record_audio(duration=args.duration)
        prompt = await agent.transcribe(recorded_audio)
        text_chunks = []
        async for chunk in agent.get_response(prompt):
            text_chunks.append(chunk)
        async for audio_chunk in agent.say("".join(text_chunks)):
            await play_audio(audio_chunk)


if __name__ == "__main__":
    # python -m orb.examples.async_openai
    asyncio.run(main())
