import discord
from discord import app_commands
from dotenv import load_dotenv
from os import getenv
from rcon import rcon
import asyncio

load_dotenv()

TOKEN = getenv('DISCORD_TOKEN')
ALLOWED_USERS = [int(u.strip()) for u in getenv('DISCORD_ALLOWED_USERS', '').split(',')]
IP = getenv('MINECRAFT_IP')
PASS = getenv('MINECRAFT_PASS')
PORT = int(getenv('RCON_PORT') or 25575)
TIMEOUT = int(getenv('RCON_TIMEOUT') or 10)

# Setup bot intents
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@tree.command(name="send", description="Send a command to the Minecraft server via RCON")
@app_commands.describe(command="The command to execute")
async def send(interaction: discord.Interaction, command: str):
    if interaction.user.id not in ALLOWED_USERS:
        await interaction.response.send_message("You are not authorized to use this command.", ephemeral=True)
        return

    await interaction.response.defer(ephemeral=True)  # Show "thinking..." message

    try:
        with rcon(IP, PASS, PORT, timeout=TIMEOUT) as mcr:
            response = mcr.command(command)
    except Exception as e:
        await interaction.followup.send(f"Failed to send command: {e}", ephemeral=True)
        return

    if not response:
        response = "No response received."

    await interaction.followup.send(f"Command executed:\n```{command}```\nResponse:\n```{response}```", ephemeral=True)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user} (ID: {client.user.id})")


client.run(TOKEN)
