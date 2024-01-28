"""Defines functionality for interacting with an Orb."""

from abc import ABC, abstractmethod


class BaseOrb(ABC):
    """Defines the concept of an orb."""

    def __init__(self) -> None:
        super().__init__()

        self.__listening = False

    @abstractmethod
    async def on_touch(self) -> None:
        """Function that triggers when the orb is touched."""

    @abstractmethod
    async def on_release(self) -> None:
        """Function that triggers when the orb is released."""

    async def toggle(self) -> None:
        if self.__listening:
            self.__listening = False
            await self.on_release()
        else:
            self.__listening = True
            await self.on_touch()

    @property
    def listening(self) -> bool:
        return self.__listening
