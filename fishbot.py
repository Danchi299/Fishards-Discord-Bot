print("Loading...")

#Discord
import discord
import discord.utils
from discord.ext import commands
from discord.ext import tasks

#Dependencies
import requests
import random
import os

#-------------------------------------------------------------------------------------------

#Global Variables

bot = commands.Bot(command_prefix = "-")

#-------------------------------------------------------------------------------------------

#Functions

def Player_Count():
    
    headers = {"Client-ID": "F07D7ED5C43A695B3EBB01C28B6A18E5"}
    appId = '1637140'
    url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=' + appId
    game_players = requests.get(url, headers=headers)

    return (str(game_players.json()['response']['player_count']))

#-------------------------------------------------------------------------------------------

#Commands
    
@bot.command(aliases=['coin','flop'])
async def flip(ctx):
    coin = random.getrandbits(1)
    
    if coin:
        await ctx.channel.send("Wizard Heads")
    else:
        await ctx.channel.send("Fish Tails")
        
@bot.command(pass_context=True)
async def roll(ctx, sides: int = 6):
    roll = random.randint(1, sides)
    await ctx.send(f'Fish God of Randomenss Rolled You a {roll}!')

@bot.command()
async def players(ctx):
    await ctx.channel.send(f'Current Player Count: {Player_Count()}')

@bot.command(aliases=['suggestion', 'suggest', 'pool', 'vote'])
async def poll(ctx, text):
        text = ctx.message.content
        text = text[text.find(" "):]
        
        Embed = discord.Embed(colour = 0xFF0000)
        Embed.set_author(name=f'Poll by {ctx.message.author}', icon_url = f'{ctx.author.avatar_url}')
        Embed.add_field(name = 'They are asking: ', value = f'{text.title()}')
        
        message = await ctx.channel.send(embed=Embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')

@bot.command(aliases=['randclass', 'rc'])
async def randomclass(ctx, amount: int = 3):
    
    if amount > 5: amount = 5
    elif amount < 1: amount = 1
    
    elements = [
    '<:fire_element:848956850875793440>',
    '<:water_element:848956903270121483>',
    '<:earth_element:848956867357966346>',
    '<:arcane_element:848956818516082698>',
    '<:goo_element:848956888153849857>',
    ]
    
    text = ''
    fclass = []
    
    for i in range(amount):    
        while 1:
            num = random.randint(0,4)
            if num in fclass:
                None
            else:
                fclass.append(num)
                break
    
    fclass.sort()
    
    for element in fclass:
        text  += elements[element]
    
    await ctx.channel.send(text)

@bot.command()
async def wiki(ctx, page: str = 'Home'):
    await ctx.channel.send('https://fishards.fandom.com/wiki/'+page)
    
#-------------------------------------------------------------------------------------------

#Events

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

'''
@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
'''

#-------------------------------------------------------------------------------------------
    
bot.run(os.environ['TOKEN'])
