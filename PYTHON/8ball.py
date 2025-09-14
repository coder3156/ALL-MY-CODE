import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='8ball')
async def eight_ball(ctx, *, question: str):
    responses = ['Yes', 'No', 'Maybe', 'Absolutely', 'Never', 'Ask again later']
    answer = random.choice(responses)
    await ctx.send(f'🎱 Question: {question}\nAnswer: {answer}')

bot.run('YOUR_BOT_TOKEN')
