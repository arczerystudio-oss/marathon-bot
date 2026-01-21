import discord

import os
TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"READY: {client.user}", flush=True)
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="// SERVER ONLINE"
    )
    await client.change_presence(status=discord.Status.online, activity=activity)

try:
    print("STARTING BOT...", flush=True)
    client.run(TOKEN)
except Exception as e:
    print("CRASH:", repr(e), flush=True)
    raise
