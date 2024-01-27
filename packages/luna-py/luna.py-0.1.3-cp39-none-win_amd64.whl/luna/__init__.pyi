from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List

if TYPE_CHECKING:
    from discord import Guild, Member
    from discord.abc import GuildChannel

class Adapter:
    """
    Adapter class for adapting different components.

    Attributes
    ----------
    variables : List[str]
        List of strings representing variables.
    default_attribute : str
        Default attribute as a string.
    attributes : Dict[str, str]
        Dictionary mapping attribute names to their values.
    """

    variables: List[str]
    default_attribute: str
    attributes: Dict[str, str]

    @classmethod
    def from_member(cls, member: Member) -> Adapter:
        """
        Create an Adapter instance from a Member object.

        Parameters
        ----------
        member : Member
            The Member object to create an Adapter from.

        Returns
        -------
        Adapter
            An instance of Adapter.
        """
        ...

    @classmethod
    def from_server(cls, server: Guild) -> Adapter:
        """
        Create an Adapter instance from a Guild object.

        Parameters
        ----------
        server : Guild
            The Guild object to create an Adapter from.

        Returns
        -------
        Adapter
            An instance of Adapter.
        """
        ...

    @classmethod
    def from_channel(cls, channel: GuildChannel) -> Adapter:
        """
        Create an Adapter instance from a GuildChannel object.

        Parameters
        ----------
        channel : GuildChannel
            The GuildChannel object to create an Adapter from.

        Returns
        -------
        Adapter
            An instance of Adapter.
        """
        ...

class Engine:
    """Engine class for processing messages with adapters."""

    @staticmethod
    def process(message: str, adapters: List["Adapter"]) -> str:
        """
        Process the given message using a list of adapters.

        Parameters
        ----------
        message : str
            The message to be processed.
        adapters : List[Adapter]
            List of Adapter instances to use in the processing.

        Returns
        -------
        str
            The processed message.
        """
        ...
