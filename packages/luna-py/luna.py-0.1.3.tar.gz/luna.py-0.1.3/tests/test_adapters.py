import datetime

import discord
from luna import Adapter, Engine


class Member:
    """A discord.py-like Member object for testing."""

    def __init__(self):
        self.id = 615439976574740340
        self.display_name = "Akai"
        self.nick = "Akai"
        self.discriminator = "0"
        self.avatar = None
        self.color = discord.Colour.red()
        self.bot = False
        self.created_at = datetime.datetime.now()


def test_engine_process():
    adapters = [Adapter.from_member(Member())]
    output = Engine.process("Hello {member(name)}, welcome to {unknown_var}", adapters)

    assert output == "Hello Akai, welcome to {unknown_var}"
