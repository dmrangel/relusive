import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.voice_states = True
bot = commands.Bot("!", intents=intents)

def risos_molestados() -> str:
    risos = ["AI", "AII", "AIAI", "AIAII", "AIII", "AIIII", "AIAIAI", "AIAIAII", "AIAIII", "AIAIIII"]
    risosm = []
    for i in range(20):
        risosm.append(random.choice(risos))
    return " ".join(risosm)

async def audio(bot, message, mp3):
    if not message.author.voice or not message.author.voice.channel:
        return
    channel = message.author.voice.channel
    voice_client = message.guild.voice_client
    if voice_client:
        await voice_client.move_to(channel)
    else:
        voice_client = await channel.connect()
    try:
        source = discord.FFmpegPCMAudio(mp3)
        voice_client.play(source, after=lambda e: bot.loop.create_task(voice_client.disconnect()))
        print(f"Playing `{mp3}` on channel {channel.name}.")
    except FileNotFoundError:
        print(f"File {mp3} not found.")
        await voice_client.disconnect()
    except Exception as e:
        print(f"Error while playing audio: {e}")
        await voice_client.disconnect()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commands found.")
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

    chance = random.randint(1, 10) == 10
    kazakhstan_chance = random.randint(1, 10) == 10
    sweet = (776930700175343636, 1046252358058909758)
    skyline = 543631112715632651
    dmr = (1128921873200193656, 1236704731548876826)
    skoolage = 327492854312075264
    if chance:
        if kazakhstan_chance:
            await audio(bot, message, 'audios/kazakhstan.mp3')
        else:
            if message.author.id in sweet:
                await message.reply("EU SOU O CABEÇA CARA", mention_author=True)
            elif message.author.id == skyline:
                await message.reply("E ESSE CHIFRE AI SKY KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK", mention_author=True)
                await audio(bot, message, 'audios/corno.mp3')
            elif message.author.id == skoolage or message.author.id in dmr:
                await message.reply(risos_molestados(), mention_author=True)
                await audio(bot, message, 'audios/aiii.mp3')

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send("PONG")

@bot.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

@bot.tree.command(name="macumba", description="SEU FRANGO DE MACUMBA")
async def macumba(interaction: discord.Interaction):
    await interaction.response.send_message("SEU FRANGO DE MACUMBA")

@bot.tree.command(name="kazakhstan", description="Kazakhstan ogrozhayet nam bombarderofky")
async def kazakhstan(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        channel = user.voice.channel
        await interaction.response.send_message("Kazakhstan 🇰🇿 ogrozhayet nam bombarderofky")
    else:
        await interaction.response.send_message("VC NEM TA EM CALL PORRA", ephemeral=True)
        return
    voice_client = interaction.guild.voice_client
    if voice_client:
        await voice_client.move_to(channel)
    else:
        voice_client = await channel.connect()
    source = discord.FFmpegPCMAudio('audios/kazakhstan.mp3')
    voice_client.play(source, after=lambda e: bot.loop.create_task(voice_client.disconnect()))

@bot.tree.command(name="aiii", description="AIII AIII AIII")
async def risos(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        channel = user.voice.channel
        risos = risos_molestados()
        await interaction.response.send_message(risos)
    else:
        await interaction.response.send_message("VC NEM TA EM CALL PORRA", ephemeral=True)
        return
    voice_client = interaction.guild.voice_client
    if voice_client:
        await voice_client.move_to(channel)
    else:
        voice_client = await channel.connect()
    source = discord.FFmpegPCMAudio('audios/aiii.mp3')
    voice_client.play(source, after=lambda e: bot.loop.create_task(voice_client.disconnect()))

bot.run("MTIyNzgwOTg0NDcyODI5OTU2MA.Ggftrv.HtC6p3dSgqIP64PMhaNPa-Rvl62nMypucufQ2k")