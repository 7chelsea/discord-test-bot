import discord
from discord.ext import commands

import random
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='token.env')
token = os.getenv('token')

bot = commands.Bot('^^')

@bot.command()
async def test(ctx):
    await ctx.send('hello there')

@bot.command()
async def cmds(ctx):
    await ctx.send('to use the calculator... ^^solve')
    await ctx.send('to apply 13% tax... ^^hst')
    await ctx.send('to roll a dice... ^^roll')

@bot.command()
async def solve(ctx, x: float, sign: str, y: float):
    if sign == '+':
        solution = x + y
    elif sign == '-':
        solution = x - y
    elif sign == '*':
        solution = x * y
    elif sign == '/':
        solution = x / y
    else:
        await ctx.send('this operation is not supported, try again')
    await ctx.send(str(solution))

@bot.command()
async def hst(ctx, x:float):
    total = x * 1.13
    await ctx.send(str(total))

@bot.command()
async def roll(ctx):
    result = random.randint(1,6)
    await ctx.send(int(result))

bot.run(token)