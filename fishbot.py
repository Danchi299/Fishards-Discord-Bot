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

global classes, elements_emoji

classes = {
"0":"Fire",
"1":"Water",
"2":"Earth",
"3":"Arcane",
"4":"Goo",

"00":"Fireball",
"01":"Push",
"02":"Meteor",
"03":"Fireblast",
"04":"Goo Flame",
"11":"Frost Ray",
"12":"Dive",
"13":"Frost Orb",
"14":"Heal",
"22":"Rock Dash",
"23":"Invincibility",
"24":"Totem",
"33":"Arcane Shield",
"34":"Goo Beam",
"44":"Grab",

"012": "Classic Fishard",
"013": "Skillshot Simon",
"014": "Baby Fancy",
"023": "Huntin' Henry",
"024": "Camping Carl",
"034": "Franz Flammenwerfer",
"123": "Slippery Sam",
"124": "Camping Carl",
"134": "Snipin Snyder",
"234": "Hidin' Harry",

"0123": "Lasting Bender",
"0124": "Explosive Michael",
"0134": "Troublesome Jessy",
"0234": "Scary Walter",
"1234": "Crazy Fred",
    
"01234": "Sensei",
}

elements_emoji = [
'<:fire_element:848956850875793440>',
'<:water_element:848956903270121483>',
'<:earth_element:848956867357966346>',
'<:arcane_element:848956818516082698>',
'<:goo_element:848956888153849857>',
]

#-------------------------------------------------------------------------------------------

#Functions

def Player_Count():
    
    headers = {"Client-ID": "F07D7ED5C43A695B3EBB01C28B6A18E5"}
    appId = '1637140' #Fishards
    url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=' + appId
    game_players = requests.get(url, headers=headers)#request people currently playing the game

    return (str(game_players.json()['response']['player_count']))

#-------------------------------------------------------------------------------------------

#Commands
    
@bot.command(aliases=['coin','flop'])
async def flip(ctx):
    coin = random.getrandbits(1) #Roll Number Between 0 and 1
    
    if coin: #if 1 its head
        await ctx.channel.send("Wizard Heads")
    else:
        await ctx.channel.send("Fish Tails")
        
@bot.command(pass_context=True)
async def roll(ctx, sides: int = 6):
    if sides < 1: sides = 1
    roll = random.randint(1, sides)#roll a number between 1 and intidure
    await ctx.send(f'Fish God of Randomenss Rolled You a {roll}!')

@bot.command()
async def players(ctx):
    await ctx.channel.send(f'Current Player Count: {Player_Count()}')

@bot.command(aliases=['suggestion', 'suggest', 'pool', 'vote'])
async def poll(ctx, text):
             
        #find first space in message and add everything after it to variable
        #because passing variables trough commands is wired
        text = ctx.message.content
        text = text[text.find(" "):] 
        
        Embed = discord.Embed(colour = 0xFF0000)
        Embed.set_author(name=f'Poll by {ctx.message.author}', icon_url = f'{ctx.author.avatar_url}')
        Embed.add_field(name = 'They are asking: ', value = f'{text.title()}')
        
        message = await ctx.channel.send(embed=Embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')

@bot.command(aliases=['randclass','randomelement','randelement','randelem','randomspell','randspell', 'r'])
async def randomclass(ctx, amount: int = 3):
    global classes, elements_emoji
    
    #check if variable is in acceptable range, else make it acceptable
    if amount > 5: amount = 5
    elif amount < 1: amount = 1
    
    text = ''
    fclass = []
    
    #make a list of random numbers from 0 to 4
    for i in range(amount):    
        while 1:
            num = random.randint(0,4)
            if num in fclass and amount > 2: #check if number was already rolled
                None
            else:
                fclass.append(num) #add number to the list of numbers
                break
    
    fclass.sort() #sort numbers so they are in right element order
    
    #add class name to message
    fclass_str = ''
    for i in fclass: #convert list to str of numbers
        fclass_str += str(i)
        
    try: #find class in global classes
        text += classes[fclass_str] + " "
        if amount > 2: text += '\n'
    except KeyError: None

    #make a message with emojis out of number list
    for element in fclass: 
        text  += elements_emoji[element] 
    
    await ctx.channel.send(text)

#prints class/spell name based on sent emojis
@bot.command(aliases=['defind','search','class','spell','name','f'])
async def find(ctx, text: str = '<:fire_element:848956850875793440><:water_element:848956903270121483><:earth_element:848956867357966346>'):
    global elements_emoji, classes
    
    #find first space in message and add everything after it to variable
    #because passing variables trough commands is wired
    text = ctx.message.content
    text = text[text.find(" "):]
    
    old_text = text.replace(" ", "")
    
    #split emojis into list
    text = text.replace('><', '> <')

    text = text.split()
    
    fclass = ''
    
    #complare emojis from list with saved emoji list\
    for element in text:
        i = -1
        for emoji in elements_emoji:
            i += 1
            if element == emoji:
                fclass += str(i) #save element numbers to variable

    #Send Class Name if it exist
    try: await ctx.channel.send(f'{classes[fclass]} {old_text}')  
    except KeyError: await ctx.channel.send(f"{old_text} Not Found")

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
