import discord
import asyncio
import os

async def audio(mp3, bot, message=None, interaction=None):
    if interaction:
        ctx_guild = interaction.guild
        ctx_author = interaction.user
        await interaction.response.defer(ephemeral=True, thinking=True)
        responder = interaction.followup.send

    elif message:
        ctx_guild = message.guild
        ctx_author = message.author
        responder = message.channel.send
    else:
        print("ERRO: A função 'audio' foi chamada sem 'message' ou 'interaction'.")
        return

    if not ctx_author.voice or not ctx_author.voice.channel:
        await responder("Você precisa estar em um canal de voz para usar este comando!", ephemeral=True)
        return

    canal_de_voz = ctx_author.voice.channel
    voice_client = ctx_guild.voice_client

    try:
        if not voice_client:
            voice_client = await canal_de_voz.connect()
            await asyncio.sleep(0.5)
        elif voice_client.channel != canal_de_voz:
            await voice_client.move_to(canal_de_voz)
            await asyncio.sleep(0.5)

        if not voice_client.is_connected():
            await responder("Falha ao estabelecer a conexão de voz.", ephemeral=True)
            return

        caminho_script = os.path.dirname(os.path.abspath(__file__))
        caminho_audio_abs = os.path.join(caminho_script, mp3)
        
        source = discord.FFmpegPCMAudio(caminho_audio_abs)
        voice_client.play(source, after=lambda e: bot.loop.create_task(voice_client.disconnect()))

        await responder(f"Tocando `{os.path.basename(mp3)}` em **{canal_de_voz.name}**.")

    except FileNotFoundError:
        await responder(f"Arquivo não encontrado: `{mp3}`", ephemeral=True)
        if ctx_guild.voice_client: await ctx_guild.voice_client.disconnect()
    except Exception as e:
        await responder(f"Ocorreu um erro: {e}", ephemeral=True)
        if ctx_guild.voice_client: await ctx_guild.voice_client.disconnect()