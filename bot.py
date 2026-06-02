import discord
import os

# ===== KONFIGURASI =====
ZONE_USER_ID = 1285096974676267028
GENERAL_CHANNEL_ID = 1509844019298045972
SERVER_ID = 1506936183224139817
# =======================

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

zone_was_online = False

@client.event
async def on_ready():
    print(f"Bot aktif sebagai {client.user}")

@client.event
async def on_presence_update(before, after):
    global zone_was_online

    if after.id != ZONE_USER_ID:
        return

    is_online_now = after.status != discord.Status.offline
    was_online = before.status != discord.Status.offline

    if is_online_now and not was_online:
        guild = client.get_guild(SERVER_ID)
        channel = guild.get_channel(GENERAL_CHANNEL_ID)
        if channel:
            await channel.send("🟢 **Zone lagi online nih!** Siapa yang mau mabar? 🎮")
        zone_was_online = True
    elif not is_online_now and was_online:
        zone_was_online = False

client.run(os.environ["BOT_TOKEN"])
