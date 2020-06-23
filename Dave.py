import discord
from discord.ext import commands
from discord.utils import find
from discord import Game
import json
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching,name="Netflix"))
    print('Bot is online')
##############################################################################################################

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="〖✋〗welcome")
    embed=discord.Embed(
        title='New Member',
        description=f'Welcome to **Dylsters Hangout** {member.mention}. Remember to read <#722719157061287956> before chatting.'
    )

    embed.set_footer(text='Made by Dylster#4482')
    await channel.send(embed=embed)

    role = discord.utils.get(member.guild.roles, name="😀― Fans")
    await member.add_roles(role)

@client.command()
async def source(ctx):
    embed=discord.Embed(
        title='Source code',
        description='View my source code [here![()',
    )

    embed.set_footer(text='Made by Dylster#4482')
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    embed=discord.Embed(
        title='🏓Pong!',
        description=f'{round(client.latency * 1000)}ms',
    )

    embed.set_footer(text='Made by Dylster#4482')
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, member: discord.Member=None, *, reason=None):
    if not member:
        embed = discord.Embed(
        title = '',
        description = f'❌ Please mention someone...',
        )

        embed.set_image(url='')
        embed.set_footer(text=f'Requested By {ctx.author.name}')

        await ctx.send(embed=embed)
        return
    await member.kick(reason=reason)

    embed = discord.Embed(
        title = '',
        description = f'✅{member.mention} Has been kicked from the server.',
    )

    embed.set_image(url='')
    embed.set_footer(text=f'Requested By {ctx.author.name}')

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, *, reason=None):
    if not member:
        embed = discord.Embed(
        title = '',
        description = f'❌ Please mention someone...',
        )

        embed.set_image(url='')
        embed.set_footer(text=f'Requested By {ctx.author.name}')

        await ctx.send(embed=embed)
        return
    await member.ban(reason=reason)

    embed = discord.Embed(
        title = '',
        description = f'✅{member.mention} Has been banned from the server.',
    )

    embed.set_image(url='')
    embed.set_footer(text=f'Requested By {ctx.author.name}')

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        embed = discord.Embed(
        title = '',
        description = f':x: Please mention someone...',
        )

        embed.set_image(url='')
        embed.set_footer(text=f'Requested By {ctx.author.name}')

        await ctx.send(embed=embed)
        return

    await member.remove_roles(role)

    embed = discord.Embed(
        title = '',
        description = f':white_check_mark:{member.mention} Has been Unmuted.',
    )

    embed.set_image(url='')
    embed.set_footer(text=f'Requested By {ctx.author.name}')

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        embed=discord.Embed(
            title='',
            description=':x: Please mention someone',
        )

        embed.set_footer(text=f'Requested By {ctx.author.name}')
        await ctx.send(embed=embed)
        return

    await member.add_roles(role)
   
    embed=discord.Embed(
            title='',
            description=f':white_check_mark: {member.mention} Has been muted',
        )

    embed.set_footer(text=f'Requested by {ctx.author.name}')
    
    await ctx.send(embed=embed)

##################
client.run('NzI0NjAxNjYyOTMyNzc5MDI5.XvCk1g.Aqnwqn1WMlya2TOnCb_gdyV1Yys')