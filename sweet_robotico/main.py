import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} - {bot.user.id}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commands found.")
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1405586295308161094)
    await channel.send(f"User {member.mention} joined the server.")

@bot.tree.command(name="macumba", description="SEU FRANGO DE MACUMBA")
async def macumba(interaction: discord.Interaction):
    await interaction.response.send_message("SEU FRANGO DE MACUMBA")

@bot.command()
async def ping(ctx):
    await ctx.send("PONG")

@bot.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

bot.run("MTIyNzgwOTg0NDcyODI5OTU2MA.Ggftrv.HtC6p3dSgqIP64PMhaNPa-Rvl62nMypucufQ2k")