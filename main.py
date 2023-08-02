import discord
import asyncio
import os
import urllib.parse, urllib.request, re
import aiofiles
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure
import random

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print("Cog Loaded!")
    print(f'{client.user} has connected to Discord!')

client.run("MTAyMDUyNDU3NjIwNTE5NzMzNQ.Gl3jpI.L9OfjoBZ-DLhfkd_jiYCFSvqrhEHa4qEw7fd-Y")
