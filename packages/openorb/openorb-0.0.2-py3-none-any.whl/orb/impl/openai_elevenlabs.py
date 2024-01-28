"""Defines an orb which uses the OpenAI and Elevenlabs APIs."""

from typing import Any

import numpy as np
import sounddevice as sd

from orb.impl.base import BaseOrb

FRAME_RATE = 22050


class OpenAIElevenlabsOrb(BaseOrb):
    def __init__(self) -> None:
        super().__init__()

        self.input_stream = sd.InputStream(
            samplerate=FRAME_RATE,
            channels=1,
            callback=self.listen,
        )

        self.input_buffer: list[np.ndarray] = []

    async def on_touch(self) -> None:
        self.input_stream.start()

    async def on_release(self) -> None:
        self.input_stream.stop()
        input_waveform = np.concatenate(self.input_buffer)
        self.input_buffer.clear()
        await self.handle_input(input_waveform)

    def listen(self, indata: np.ndarray, frames: int, *_: Any) -> None:
        if self.listening:
            self.input_buffer.append(indata.squeeze(1))

    async def handle_input(self, input_buffer: np.ndarray) -> None:
        raise NotImplementedError()
