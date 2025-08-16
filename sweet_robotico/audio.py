import discord
from discord.ext import commands

async def audio(mp3, bot, message = None, interaction = None):
    if message != None:
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
    elif interaction != None:
        user = interaction.user
        if user.voice and user.voice.channel:
            channel = user.voice.channel
        else:
            await interaction.response.send_message("VC NEM TA EM CALL PORRA", ephemeral=True)
            return
        voice_client = interaction.guild.voice_client
        if voice_client:
            await voice_client.move_to(channel)
        else:
            voice_client = await channel.connect()
        source = discord.FFmpegPCMAudio(mp3)
        voice_client.play(source, after=lambda e: bot.loop.create_task(voice_client.disconnect()))