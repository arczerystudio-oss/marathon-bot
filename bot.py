import discord

TOKEN = "MTQ2MzYzMzc1NDg3MzY1OTY1Nw.GLANQf.O4NoA0RHcJ3SmR1-wzasRQd3Qd8jEnXEF1DMxI"

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
