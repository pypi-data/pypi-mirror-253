"""Runs the virtual orb on your computer."""

import asyncio
import tkinter as tk

from orb.impl.base import BaseOrb


class TkApp:
    """Runs an orb through a Tkinter GUI."""

    def __init__(
        self,
        orb: BaseOrb,
        listening_text: str = "Orb is listening...",
        not_listening_text: str = "Orb is not listening",
    ) -> None:
        super().__init__()

        # Stores app parameters.
        self.orb = orb
        self.listening_text = listening_text
        self.not_listening_text = not_listening_text

        # Creates a GUI.
        self.app = tk.Tk()
        self.app.title("Orb")

        # Bind spacebar press and release events.
        self.app.bind("<KeyPress-space>", lambda event: asyncio.ensure_future(self.on_space_press(event)))

        # Create a label widget
        self.label = tk.Label(self.app, text=self.not_listening_text, font=("Arial", 14))
        self.label.pack(pady=20)

    async def on_space_press(self, event: tk.Event) -> None:
        await self.orb.toggle()

        # Updates the label to match the current state.
        if self.orb.listening:
            self.label.config(text=self.listening_text)
        else:
            self.label.config(text=self.not_listening_text)

    async def start(self) -> None:
        try:
            while True:
                self.app.update()
                await asyncio.sleep(0.01)
        except tk.TclError as e:
            if "application has been destroyed" not in e.args[0]:
                raise
