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

    if not ctx_author.voice or not ctx_author.voice.channel:
        await responder("VOCE NEM TA EM CALL PORRA", ephemeral=True)
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
            await responder("NAO DEU PRA ENTRAR NA CALL", ephemeral=True)
            return

        caminho_script = os.path.dirname(os.path.abspath(__file__))
        caminho_audio_abs = os.path.join(caminho_script, mp3)
        
        source = discord.FFmpegPCMAudio(caminho_audio_abs)
        voice_client.play(source, after=lambda e: bot.loop.create_task(voice_client.disconnect()))

        await responder(f"TOMA SUA PUTA", ephemeral=True)

    except FileNotFoundError:
        await responder(f"NAO ENCONTREI O AUDIO NAO CHEFE", ephemeral=True)
        if ctx_guild.voice_client: await ctx_guild.voice_client.disconnect()
    except Exception as e:
        await responder(f"DEU MERDA MANO: {e}", ephemeral=True)
        if ctx_guild.voice_client: await ctx_guild.voice_client.disconnect()

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
    
def aiii() -> str:
    gritos = ["AI", "AII", "AIAI", "AIAII", "AIII", "AIIII", "AIAIAI", "AIAIAII"]
    gritosm = [random.choice(gritos) for _ in range(random.randint(10, 20))]
    return " ".join(gritosm)