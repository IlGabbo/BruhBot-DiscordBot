import os
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord import FFmpegPCMAudio
from discord.utils import get
import discord
import random

intents = discord.Intents.default()
intents.message_content = True
token = "MTAzMzk5MDcwNzk4OTQ2NzE4Ng.G8VSm3.rdgWDfcgRcxJL38tfi0_KnpQctGLyJ9A-Ojjzc"
bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_message(message):
    notAcceptedMessage = [
        "cazzo",
        "merda",
        "vaffanculo",
        "fanculo",
        "gym",
        "fuck",
        "porco dio",
        "porcodio",
        "puttana",
        "troia",
        "zoccola"
    ]

    for i in range(len(notAcceptedMessage)):
        if notAcceptedMessage[i] in message.content.lower():
            await message.channel.send(f"{message.author} calmati bro")

    await bot.process_commands(message)


@bot.command()
async def info(ctx, member: discord.Member = None):
    if member is None:
        enb = discord.Embed(timestamp=ctx.message.created_at)
        enb.set_author(name="Bot info")
        enb.add_field(name="Prefix: $", value="###", inline=False)
        enb.add_field(name="randomjoke", value="Generate a joke", inline=False)
        enb.add_field(name="voicekick", value="Kick a user from voice chat", inline=False)
        enb.add_field(name="move", value="Move a user from one voice chat to another", inline=False)
        #enb.add_field(name="handicaplevel", value="Calculate your handicap level", inline=False)
        enb.add_field(name="ban", value="Ban a user", inline=False)
        enb.add_field(name="play", value="Play random audio", inline=False)
        enb.add_field(name="stop", value="Disconnect bot from voice chat", inline=False)

        await ctx.send(embed=enb)

    else:
        try:
            infoEmbed = discord.Embed(timestamp=ctx.message.created_at)
            infoEmbed.set_author(name=f"User info - {member}")
            infoEmbed.set_thumbnail(url=member.display_avatar)
            infoEmbed.add_field(name="ID:", value=member.id, inline=False)
            infoEmbed.add_field(name="Name:", value=member.display_name, inline=False)
            infoEmbed.add_field(name="Created:", value=member.created_at, inline=False)
            infoEmbed.add_field(name="Joined:", value=member.joined_at, inline=False)
            infoEmbed.add_field(name="Is a bot?:", value=member.bot, inline=False)
            await ctx.send(embed=infoEmbed)

        except:
            await ctx.send("Not a valid user", delete_after=4)


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

    if index is None:
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
        if reason is None:
            reason = "'None'"

        if member == ctx.message.author or member == None:
            await ctx.send(f"{ctx.message.author} you can't ban yourself", delete_after=4)
            return

        await member.ban(reason=reason)
        emb = discord.Embed(title="User banning",
                            description=f"{ctx.message.author} banned {member}, Reason: {reason}",
                            color=0x6109af)

        await ctx.send(embed=emb)
        await member.send(f"You are banned {member.guild.name}, Reason: {reason}")

    except:
        await ctx.send("Permission Denied", delete_after=4)

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
                        description=f"{member} was kicked by {ctx.message.author}",
                        color=0x6109af)
    await ctx.send(embed=emb)


@bot.command()
async def handicaplevel(ctx, member: discord.Member = None):
    level = random.randint(0, 104)
    if member is None:
        emb = discord.Embed(title=f"{ctx.message.author}",
                            description=f"Your hadicap level is {str(level)} out of 104",
                            color=0x6109af)
        await ctx.send(embed=emb)

    else:
        emb = discord.Embed(title=f"{member}",
                            description=f"The handicap level of {member} is {str(level)} out of 104",
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
            musicList.set_author(name="Available Audios")
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
                    await ctx.send("First use $stop")

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
                    await ctx.send("Audio not found")



    else:
        await ctx.send("First join to voice channel")


@bot.command()
async def stop(ctx):
    voice = ctx.message.guild.voice_client
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


""" -------------------------------------------- Error Handling -------------------------------------------- """


@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("User not found", delete_after=4)


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("User not found", delete_after=4)


@move.error
async def move_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("User not found", delete_after=4)


@handicaplevel.error
async def handicaplevel_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("User not found", delete_after=4)


bot.run(token)
