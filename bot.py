#these are the imports

#imports the discord.py library
import discord

#imports the library needed to read the .env file which stores the TOKEN of the bot
import os

#imports the command extension which can be used with native python functions
from discord.ext import commands
from discord.ext.commands import guild_only

import time
import random
import asyncio

#the intents used in your bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#same as a cliet which establishes a connection with the Discord API but bot has more functionality
bot = commands.Bot(intents=intents, command_prefix='g ')

#an function which tells us that we have successfully made a connection
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def pingcount(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await ctx.channel.send(content = 'Pong! {:.2f}ms'.format(duration))
    



@bot.command(
    help = 'will reply with \'pong\' and that will tell you how fast the bot is replying',
    brief = 'says pong'
)
async def ping(ctx):
    await ctx.channel.send('pong')


@bot.command(
    help = 'why do you need help for this you r-word',
    brief = 'just says hello bruv'
)
async def hello(ctx):
    await ctx.channel.send('hello there!!')


@bot.command(
    help = 'you say hiphip and the bot replys with hooray',
    brief = 'says hooray'
)
async def hiphip(ctx):
    await ctx.channel.send('hoorayyy!!!!')


@bot.command(
    help = '''This is a math function which will do math for you(cause ofc you gotta be dumb)
    you can add, subtract, multiply, divide and ask for the remainder of a division
    The format is \"g math {number1} {arithmetic operator sign} {number2}\"
    Example: /"g math 2 + 2/"''',
    brief = 'Does math stuff'
)
async def math(ctx, number1 : int, operator, number2 : int):

    match operator:
        case '+':
            await ctx.channel.send(f"It\'s {number1+number2}")

        case '-':
            await ctx.channel.send(f"That will be {number1-number2}")

        case '*':
            await ctx.channel.send(f"It is {number1*number2}")

        case '/':
            await ctx.channel.send(f"That will be {number1/number2}")

        case '%':
            await ctx.channel.send(f"That is {number1%number2}")


@bot.command(
    help = 'Squares a number you enter/nThe format is "g square {your number}"',
    brief = 'Squares numbers'
)
async def square(ctx, number1 : int):
    await ctx.channel.send(f"The square is {number1*number1}\ndumbass")


@bot.command(
    help = 'the bot will be rude and will demotivate you :)',
    brief = 'try it and look for yo self, credit goes to Anna :)'
)
async def whoisbitchless(ctx):
    await ctx.channel.send("you, you are bitchless")


@bot.command(
    help = 'will say a random number\nthe format is \"g number\"',
    brief = 'gives a random number'
)
async def number(ctx):
    await ctx.channel.send(f"Here\'s a random number\n{random.randint(0, 20)}")


@bot.command()
async def timer(ctx, seconds : int):
    if seconds > 60:
        await ctx.channel.send("The timer can not go more than 60seconds!!")
    else:
        await ctx.channel.send(f"Timer set for {seconds} second(s)")
        await asyncio.sleep(seconds)
        await ctx.channel.send("Time is up!!")


@bot.command()
async def kick(ctx, id:int):
    user = await bot.fetch_user(id)
    await ctx.guild.kick(user)
    await ctx.channel.send(f"{user} has been kicked. that\'ll teach \'em!!")


@bot.command(
    help = 'bans people\nformat is \"g ban {user\'s ID}\"',
    brief = 'bans people'
)
@guild_only()
async def ban(ctx, id:int):
    user = await bot.fetch_user(id)
    await ctx.guild.ban(user)
    await ctx.channel.send(f"{user} has been banned.")


@bot.command(
    help = 'unbans people\nformat is \"g unban {user\'s ID}\"',
    breif = 'unbans people'
)
@guild_only()
async def trollunban(ctx, id:int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.channel.send(f"{user} was unbanned. better behave now!!")
    await ctx.channel.send("just kidding")
    await ctx.guild.ban(user)
    await ctx.channel.send("sucks to be you, banned xD")


@bot.command()
@guild_only()
async def unban(ctx, id:int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.channel.send(f"{user} was unbanned, and no, i am not trolling. they are unbanned")


@bot.command()
async def buymenitro(ctx):
    await ctx.channel.send("i will ban your stanky little ass if you say that one more time")


@bot.event
async def on_member_join(member):
    await member.send("""this is a test message.""")





bot.run(os.getenv('TOKEN'))