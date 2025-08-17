import random
import discord
from discord.ext import commands
from audio import audio
import os
from dotenv import load_dotenv

# Config
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

# IDs
def carregar_ids():
    try:
        with open("ids.txt", "r", encoding="utf-8") as file:
            ids = dict()
            for line in file:
                if line.strip():
                    key, value = line.strip().split(" - ")
                    ids[key] = [int(id.strip()) for id in value.split(",")]
            print("Arquivo de IDs carregado com sucesso.")
            return ids
    except FileNotFoundError:
        print("ERRO: Arquivo 'ids.txt' não encontrado.")
        return {}
    except Exception as e:
        print(f"ERRO ao ler 'ids.txt': {e}")
        return {}

IDS_AMIGOS = carregar_ids()

# Functions
def aiii() -> str:
    gritos = ["AI", "AII", "AIAI", "AIAII", "AIII", "AIIII", "AIAIAI", "AIAIAII"]
    gritosm = [random.choice(gritos) for _ in range(random.randint(10, 20))]
    return " ".join(gritosm)

# Events
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} comandos de barra sincronizados.")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)

    ctx = await bot.get_context(message)
    if ctx.command:
        return

    if random.randint(1, 10) == 1:
        if random.randint(1, 10) == 1:
            await audio(mp3='audios/kazakhstan.mp3', bot=bot, message=message)
            await message.reply("Kazakhstan 🇰🇿 ogrozhayet nam bombarderofky", mention_author=True)
        else:
            author_id = message.author.id
            if author_id in IDS_AMIGOS.get("sweet", []):
                await message.reply("EU SOU O CABEÇA CARA", mention_author=True)
            elif author_id in IDS_AMIGOS.get("skyline", []):
                await message.reply("E ESSE CHIFRE AI SKY KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK", mention_author=True)
                await audio(mp3='audios/corno.mp3', bot=bot, message=message)
            elif author_id in IDS_AMIGOS.get("skoolage", []) or author_id in IDS_AMIGOS.get("dmr", []):
                await message.reply(aiii(), mention_author=True)
                await audio(mp3='audios/aiii.mp3', bot=bot, message=message)

# Simple comms
@bot.command()
async def ping(ctx):
    await ctx.send("PONG")

@bot.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

# Tree comms
@bot.tree.command(name="aiii", description="AIII AIII AIII")
async def gritos(interaction: discord.Interaction):
    await audio('audios/aiii.mp3', bot=bot, interaction=interaction)

@bot.tree.command(name="kazakhstan", description="Kazakhstan ogrozhayet nam bombarderofky")
async def kazakhstan(interaction: discord.Interaction):
    await audio('audios/kazakhstan.mp3', bot=bot, interaction=interaction)

@bot.tree.command(name="uiia", description="U II A U II A")
async def uiia(interaction: discord.Interaction):
    await audio('audios/uiia.mp3', bot=bot, interaction=interaction)

@bot.tree.command(name="corno", description="DESÇA DAI SEU CORNO")
async def corno(interaction: discord.Interaction):
    await audio('audios/corno.mp3', bot=bot, interaction=interaction)

@bot.tree.command(name="yamete", description="YAMETE KUDASAI")
async def yamete(interaction: discord.Interaction):
    await audio('audios/yamete.mp3', bot=bot, interaction=interaction)

@bot.tree.command(name="tralalero", description="TRALALERO TRALALA")
async def tralalero(interaction: discord.Interaction):
    await audio('audios/tralalero.mp3', bot=bot, interaction=interaction)

@bot.tree.command(name="sahur", description="TUNG TUNG TUNG SAHUR")
async def sahur(interaction: discord.Interaction):
    await audio('audios/sahur.mp3', bot=bot, interaction=interaction)

@bot.tree.command(name="bombardino", description="BOMBARDINO CROCODILO")
async def bombardino(interaction: discord.Interaction):
    await audio('audios/bombardino.mp3', bot=bot, interaction=interaction)

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("ERRO: Token do bot não encontrado. Verifique seu arquivo .env")