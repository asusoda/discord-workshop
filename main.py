import os

import discord
from discord.ext import commands
client = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix="%"
)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for guild in client.guilds:
        print(guild.name)
        for category in guild.categories:
            print(f"|-{category.name}")
            for channel in category.channels:
                print(f" |-{channel.name}")
                perms = channel.permissions_for(guild.me)
                if perms.send_messages:
                    print(f"  |-I can send messages in {channel.name}")
                if perms.view_channel:
                    print(f"  |-I can view {channel.name}")
                if perms.read_messages:
                    print(f"  |-I can read messages in {channel.name}")
                if perms.manage_messages:
                    print(f"  |-I can manage messages in {channel.name}")
                if perms.manage_channels:
                    print(f"  |-I can manage channels in {channel.name}")
                if perms.administrator:
                    print(f"  |-I am an admin in {channel.name}")
                    

@client.command()
async def test(ctx):
    print(ctx.guild.name)

client.run(os.getenv('DISCORD_BOT_TOKEN'))

