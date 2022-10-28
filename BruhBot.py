import os
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord import FFmpegPCMAudio
from discord.utils import get
import discord
import random

intents = discord.Intents.default()
intents.message_content = True
token = ""
bot = commands.Bot(command_prefix="$", intents=intents)



@bot.event
async def on_message(message):
    if "cazzo" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro")

    elif "merda" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro")

    elif "vaffanculo" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro")

    elif "gym" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro")

    elif "fuck" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro")

    elif "porco dio" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro")

    elif "porcodio" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro")

    elif "puttana" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro ()")

    elif "fabrizio" in message.content.lower():
        await message.channel.send(f"{message.author} calmati bro ()")

    await bot.process_commands(message)



@bot.command()
async def info(ctx, member: discord.Member = None):
    if member == None:
        enb = discord.Embed(timestamp=ctx.message.created_at)
        enb.set_author(name="Bot info")
        enb.add_field(name="Prefix: $", value="###", inline=False)
        enb.add_field(name="randomjoke", value="Genera una battuta blackhumor casuale", inline=False)
        enb.add_field(name="voicekick", value="Kicka un utente dalla chat vocale", inline=False)
        enb.add_field(name="move", value="Sposta un utente da una chat vocale all'altra", inline=False)
        enb.add_field(name="handicaplevel", value="Calcola il tuo livello di handicap", inline=False)
        enb.add_field(name="ban", value="Banna un utente", inline=False)
        enb.add_field(name="play", value="Ascolta un audio casuale", inline=False)
        enb.add_field(name="stop", value="Disconnetti il bot dalla chat vocale", inline=False)

        await ctx.send(embed=enb)

    else:
        try:
            infoEmbed = discord.Embed(timestamp=ctx.message.created_at)
            infoEmbed.set_author(name=f"User info - {member}")
            infoEmbed.set_thumbnail(url=member.display_avatar)
            infoEmbed.add_field(name="ID:", value=member.id, inline=False)
            infoEmbed.add_field(name="Name:", value=member.display_name, inline=False)
            infoEmbed.add_field(name="Creato il:", value=member.created_at, inline=False)
            infoEmbed.add_field(name="Entrato il:", value=member.joined_at, inline=False)
            infoEmbed.add_field(name="Bot?:", value=member.bot, inline=False)
            await ctx.send(embed=infoEmbed)

        except:
            await ctx.send("User non valido", delete_after=4)


@bot.command()
async def randomjoke(ctx, index=None):
    jokes = [
        "Ad una bambina in Africa le sono arrivate le medicine per l'ebola ma dietro c'è scritto: 'Da consumare dopo i pasti'.",
        # 0
        "Sai qual’è la differenza tra un ebreo e una palla. È che la palla può uscire dal campo, l’ebreo no.",  # 1
        "Perché i musulmani si fanno saltare in aria? Perché non possono volare.",  # 2
        "Quale è la frase preferita dai Nazisti?....Hai da accendere?",  # 3
        "Come si chiama un negro in macchina? Ladro",  # 4
        """
             Un frocio va dal dottore per una visita
         Dottore: Mi dispiace, ma hai preso l'AIDS
         Frocio: Oh no dottore, che posso fare? Cosa posso fare??
         Dottore: Ora torna a casa, mangia molte castagne, una torta al cioccolato e molte molte prugne
         Frocio: Questo mi guarirà?
         Dottore: No, ma almeno ti ricorderà a cosa serve il buco del culo!
             """,  # 5
        "Come fai a capire di essere ad un picnic tra gay? Gli hotdog sanno di merda."  # 6
        ]

    if index == None:
        joke = random.choice(jokes)
        await ctx.send(joke)

    elif int(index) > 6 or int(index) < 0:
        await ctx.send("Index Saverio", delete_after=4)

    else:
        await ctx.send(jokes[int(index)])


@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, reason=None):
    try:
        if reason == None:
            reason = "nessun motivo"

        if member == ctx.message.author or member == None:
            await ctx.send(f"{ctx.message.author} non puoi bannarti", delete_after=4)
            return

        await member.ban(reason=reason)
        emb = discord.Embed(title="User banning",
                            description=f"{ctx.message.author} ha bannato {member} per {reason}",
                            color=0x6109af)

        await ctx.send(embed=emb)
        await member.send(f"Sei stato bannato da {member.guild.name} per {reason}")

    except:
        await ctx.send("Non hai abbastanza permessi", delete_after=4)


@bot.command()
@has_permissions(ban_members=True)
async def pardon(ctx, *, member):
    banned = await ctx.guild.bans()
    memberName, discriminator = member.split("#")

    for bans in banned:
        users = bans.user

        if (users.name, users.discriminator) == (memberName, discriminator):
            await ctx.guild.unban(users)
            await ctx.send(f"{users.mention} è stato sbannato")
            return


# Move command

@bot.command()
async def move(ctx, member: discord.Member, chan):
    member_id = member.id
    print(member_id, chan)
    channel = discord.utils.get(ctx.guild.channels, name=chan)
    await member.edit(voice_channel=channel)


# Kick from Voice Channel

@bot.command()
async def voicekick(ctx, member: discord.Member):
    await member.edit(voice_channel=None)
    emb = discord.Embed(title="User kick",
                        description=f"{member} è stato kickato da {ctx.message.author}",
                        color=0x6109af)
    await ctx.send(embed=emb)

@bot.command()
async def handicaplevel(ctx, member: discord.Member = None):
    level = random.randint(0, 104)
    if member == None:
        emb = discord.Embed(title=f"{ctx.message.author}",
                            description=f"Il tuo livello di handicap è {str(level)} su 104",
                            color=0x6109af)
        await ctx.send(embed=emb)

    else:
        emb = discord.Embed(title=f"{member}",
                            description=f"Il livello di handicap di {member} è {str(level)} su 104",
                            color=0x6109af)
        await ctx.send(embed=emb)

@bot.command()
async def play(ctx, argument=None):
    check = True
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        audioList = os.listdir("audio")
        print(argument)

        if str(argument).strip() == "list":
            musicList = discord.Embed(timestamp=ctx.message.created_at)
            musicList.set_author(name="Musica disponibile")
            for i in range(len(audioList)):
                musicList.add_field(name="--------------", value=f"{audioList[i][: -4]}", inline=False)

            await ctx.send(embed=musicList)

        else:
            if argument is None:
                try:
                    voice = await channel.connect()
                    randomAudio = random.choice(audioList)
                    source = FFmpegPCMAudio(f"./audio/{randomAudio}")
                    voice.play(source)

                except:
                    await ctx.send("First use $leave")

            else:
                print(len(audioList))
                for i in range(len(audioList)):
                    if argument == audioList[i][: -4]:
                        voice = await channel.connect()
                        voice.play(FFmpegPCMAudio(f"./audio/{audioList[i]}"))
                        check = True
                        break

                    else:
                        check = False
                        continue

                if not check:
                    await ctx.send("Brano non trovato")



    else:
        await ctx.send("Entra prima in un canale vocale")

@bot.command()
async def stop(ctx):
    voice = ctx.message.guild.voice_client
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")



""" -------------------------------------------- Error Handling -------------------------------------------- """


@info.error
async def info_error(ctx,error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Utente inesistente", delete_after=4)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Utente inesistente", delete_after=4)


@move.error
async def move_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Non esiste nessuno con quel nome", delete_after=4)

@handicaplevel.error
async def handicaplevel_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("L'utente non esiste", delete_after=4)

bot.run(token)
