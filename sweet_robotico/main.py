import random
import discord
from discord.ext import commands
from audio import audio

intents = discord.Intents.all()
intents.voice_states = True
bot = commands.Bot("!", intents=intents)

def aiii() -> str:
    gritos = ["AI", "AII", "AIAI", "AIAII", "AIII", "AIIII", "AIAIAI", "AIAIAII", "AIAIII", "AIAIIII"]
    gritosm = []
    n = random.randint(10, 20)
    for i in range(n):
        gritosm.append(random.choice(gritos))
    return " ".join(gritosm)

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
            await audio(bot = bot, message = message, mp3 = 'audios/kazakhstan.mp3')
        else:
            if message.author.id in sweet:
                await message.reply("EU SOU O CABEÇA CARA", mention_author=True)
            elif message.author.id == skyline:
                await message.reply("E ESSE CHIFRE AI SKY KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK", mention_author=True)
                await audio(bot = bot, message = message, mp3 = 'audios/corno.mp3')
            elif message.author.id == skoolage or message.author.id in dmr:
                await message.reply(aiii(), mention_author=True)
                await audio(bot = bot, message = message, mp3 = 'audios/aiii.mp3')

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
        await interaction.response.send_message("Kazakhstan 🇰🇿 ogrozhayet nam bombarderofky")
    await audio('audios/kazakhstan.mp3', bot, interaction=interaction)

@bot.tree.command(name="aiii", description="AIII AIII AIII")
async def gritos(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        gritos = aiii()
        await interaction.response.send_message(gritos) 
    await audio('audios/aiii.mp3', bot, interaction=interaction)

@bot.tree.command(name="corno", description="DESÇA DAI SEU CORNO")
async def corno(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        await interaction.response.send_message('DESÇA DAI SKILINE CHAN')  
    await audio('audios/corno.mp3', bot, interaction=interaction)

@bot.tree.command(name="yamete", description="YAMETE KUDASAI")
async def corno(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        await interaction.response.send_message('YAMETE KUDASAI')  
    await audio('audios/yamete.mp3', bot, interaction=interaction)

@bot.tree.command(name="tralalero", description="TRALALERO TRALALA")
async def corno(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        await interaction.response.send_message('Trallallero Trallalla, porco dio e porco Allah. Ero con il mio fottuto figlio merdardo a giocare a Fortnite, quando a un punto arriva mia nonna, Ornella Leccacappella, a avvisarci che quello stronzo di Burger ci aveva invitato a cena per mangiare un purè di cazzi')  
    await audio('audios/tralalero.mp3', bot, interaction=interaction)

@bot.tree.command(name="sahur", description="TUNG TUNG TUNG SAHUR")
async def corno(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        await interaction.response.send_message('Tung, tung, tung, tung, tung, tung, tung, tung, tung Sahur. Anomali mengerikan yang hanya keluar pada sahur. Konon katanya kalau ada orang yang dipanggil sahur tiga kali dan tidak nyaut, maka makhluk ini datang di rumah kalian. Hiiii, seramnya! Tung tung ini biasanya bersuara layaknya pukulan kentungan sepereti ini. Tung, tung, tung, tung, tung, tung, tung! Share ke teman kalian yang susah sahur.')  
    await audio('audios/sahur.mp3', bot, interaction=interaction)

@bot.tree.command(name="bombardino", description="BOMBARDINO CROCODILO")
async def corno(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        await interaction.response.send_message('Bombardiro Crocodilo, un fottuto alligatore volante, che vola e bombarda i bambini a Gaza e in Palestina. Non crede in Allah, e ama le bombe. Si nutre dello spirito di tua madre. E se hai tradotto tutto questo, allora sei uno stronzo. Non rompere la battuta, prostituta.')  
    await audio('audios/bombardino.mp3', bot, interaction=interaction)

@bot.tree.command(name="uiia", description="U II A U II A")
async def corno(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        await interaction.response.send_message('U II A U II A')  
    await audio('audios/uiia.mp3', bot, interaction=interaction)

bot.run("MTIyNzgwOTg0NDcyODI5OTU2MA.Ggftrv.HtC6p3dSgqIP64PMhaNPa-Rvl62nMypucufQ2k")