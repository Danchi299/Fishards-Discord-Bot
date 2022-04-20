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

#-----------------------------------------------------------------------------------#
#                                                                                   #
#                           ╔══════════════════════════════╗                        #
#                           ║                              ║                        #
#                           ║Coding is it's own kind of art║                        #
#                           ║                              ║                        #
#                           ║           Fish-art           ║                        #
#                           ║                              ║                        #
#                           ╚══════════════════════════════╝                        #
#                                                                                   #
#                                   ========     ======                             #
#                                   =========   ========                            #
#                                 ======================                            #
#                             :==++++======================                         #
#                           --=++++++++++++++++++++++++=====                        #
#                           +++++++++++++++++++++++++++=====                        #
#                        :+++++++++++++++++++++++++++++++++=                        #
#                      :-=++++++++++++++**********+++++++++=                        #
#                      =++++++++++++++**##########**+++++++=                        #
#                    ::=+++++++++++++*####******####+++++++=                        #
#                    ++++++++++++++++*####+====*####+++++++=                        #
#                    ++++++++++++++++*####*++++*####+++++++=                        #
#                    +++++++++++++++++**##########**+++++++=                        #
#                    +++++++++++++++++++**********+++++++++=                        #
#                    ++++++++++++++++++++++++++++++++++++++=                        #
#                    ++++++++++++++++++++++++++++++++++++++=                        #
#                    ++++++++++++++++++++++++++++++++++++++=                        #
#                    ++++++++++++++++++++++++++++++++++++++=                        #
#                    +++++++++++++++++++++++++++++++++++++=                         #
#                    ++++++++++++++++++++++++++++++++++++=                          #
#                    +++++++++++++++++++++++++++++++++++=                           #
#                    ++++++++++++++++++++++++++++++++++=                            #
#                    +++++++++++++++++++++++++++++++++=                             #
#                     ++++++++++++++++++++++++++++++=                               #
#                     ++++++++++++++++++++++++++++++=                               #
#                     +++++++++++++++++++++++++++++++++++++++                       #
#                 -++++++++++++++++++++++++++++++++++++++++++=                      #
#              .==++++++++++++++++++++++++++++++++++++++++++=                       #
#              =+++++++++++++++++++++++++++++++++++++++++++++=                      #
#       .+++++++++++++++++++++++++        +++++++++++++++++++=                      #
#        .+++++++++++++++++++++++            ++++++++++++++++=                      #
#         .+++++++++++++++++++                        .++++++=                      #
#           .-+++++++++++++                            ..++++=                      #
#                                                                                   #
#-----------------------------------------------------------------------------------#

#Global Variables

bot = commands.Bot(command_prefix = "-")
bot.queue = []
bot.queueing = 0
bot.read_channel = {''}
bot.voices = {404650697183723530: 'en'}


global classes, elements_emoji

# List of all element emojis
elements_emoji = [
'<:fire_element:848956850875793440>',
'<:water_element:848956903270121483>',
'<:earth_element:848956867357966346>',
'<:arcane_element:848956818516082698>',
'<:goo_element:848956888153849857>',
]

# List of all element combinations with names
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
"024": "Brawlin' Bob",
"034": "Franz Flammenwerfer",
"123": "Slippery Sam",
"124": "Camping Carl",
"134": "Snipin Snyder",
"234": "Hidin' Harry",

"1234": "Fireless Fred",
"0234": "Waterless Walter",
"0134": "Earthless Eric",
"0124": "Arcanaless Angela",
"0123": "Gooless Gary",
    
"01234": "Sensei",
}

bot.langs = {
"af": "Afrikaans",
"ar": "Arabic",
"bg": "Bulgarian",
"bn": "Bengali",
"bs": "Bosnian",
"ca": "Catalan",
"cs": "Czech",
"cy": "Welsh",
"da": "Danish",
"de": "German",
"el": "Greek",
"en": "English",
"eo": "Esperanto",
"es": "Spanish",
"et": "Estonian",
"fi": "Finnish",
"fr": "French",
"gu": "Gujarati",
"hi": "Hindi",
"hr": "Croatian",
"hu": "Hungarian",
"hy": "Armenian",
"id": "Indonesian",
"is": "Icelandic",
"it": "Italian",
"ja": "Japanese",
"jw": "Javanese",
"km": "Khmer",
"kn": "Kannada",
"ko": "Korean",
"la": "Latin",
"lv": "Latvian",
"mk": "Macedonian",
"ml": "Malayalam",
"mr": "Marathi",
"my": "Myanmar (Burmese)",
"ne": "Nepali",
"nl": "Dutch",
"no": "Norwegian",
"pl": "Polish",
"pt": "Portuguese",
"ro": "Romanian",
"ru": "Russian",
"si": "Sinhala",
"sk": "Slovak",
"sq": "Albanian",
"sr": "Serbian",
"su": "Sundanese",
"sv": "Swedish",
"sw": "Swahili",
"ta": "Tamil",
"te": "Telugu",
"th": "Thai",
"tl": "Filipino",
"tr": "Turkish",
"uk": "Ukrainian",
"ur": "Urdu",
"vi": "Vietnamese",
"zh-CN": "Chinese"
}


#-------------------------------------------------------------------------------------------

#Functions

def Player_Count(): #returns amount of people currently playing Fishards
    
    headers = {"Client-ID": "F07D7ED5C43A695B3EBB01C28B6A18E5"}
    appId = '1637140' #Fishards
    url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=' + appId
    game_players = requests.get(url, headers=headers)#request people currently playing the game

    return (str(game_players.json()['response']['player_count']))


async def status(activity): #Change Bot Status Message
    
    if not activity: #if no arguments passed, choose randomly from list
        activity = bot.Activity[random.randint(0, len(bot.Activity)-1)]
    
    activity, text = activity.split('|')
        
    if activity == "P": #Playing
        await bot.change_presence(activity=discord.Game(name = text))
    elif activity == "S": #Streaming
        await bot.change_presence(activity=discord.Streaming(name = text, url = "https://www.twitch.tv/rivernotchgamestudio"))
    elif activity == "L": #Listening
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name = text))
    elif activity == "W": #Watching
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = text))

#-------------------------------------------------------------------------------------------

#Commands
    
@bot.command(aliases=['coin','flop'], description='''
flips a coin and gives you heads or tails
''')
async def flip(ctx):
    coin = random.getrandbits(1) #Roll Number Between 0 and 1
    
    if coin: #if 1 its head
        await ctx.channel.send("Wizard Heads")
    else:
        await ctx.channel.send("Fish Tails")
        
@bot.command(pass_context=True, description='''
gives you random number between 1 and 6
''')
async def roll(ctx, sides: int = 6):
    if sides < 1: sides = 1
    roll = random.randint(1, sides)#roll a number between 1 and intidure
    await ctx.send(f'Fish God of Randomenss Rolled You a {roll}!')

@bot.command(description='''
Displays current count of players in Fishards
''')
async def players(ctx):
    await ctx.channel.send(f'Current Player Count: {Player_Count()}')

@bot.command(aliases=['suggestion', 'suggest', 'pool', 'vote'], description='''
Makes a poll which people can vote in
''')
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

@bot.command(aliases=['randclass','randomelement','randelement','randelem','randomspell','randspell', 'r'], description='''
Gives you random class, spell or element
''')
async def randomclass(ctx, amount: int = 3, elements = None):
    global classes, elements_emoji
    
    #check if variable is in acceptable range, else make it acceptable
    if amount > 5: amount = 5
    elif amount < 1: amount = 1
    
    #find first space in message and add everything after it to variable
    #because passing variables trough commands is wired
    elements = ctx.message.content
    elements = elements[elements.find(" "):]
    elements = elements[elements.find(" "):]
    
    #split emojis into list
    elements = elements.replace('><', '> <')
    elements = elements.split()
    
    #remove dublicates if its a class
    if amount > 2:
        elements = list(dict.fromkeys(elements))
    
    #variables
    text = ''
    fclass = []
    breaker = 0
    amount_decrease = 0
    
    #convert emojis into number ids
    for element in elements:
        num = -1
        for emoji in elements_emoji:
            num += 1
            if element == emoji:
                fclass.append(num) #save element numbers to list
                amount_decrease += 1
                if not amount: breaker = 1; break 
        if breaker: break
    
    #make a list of random numbers between 0 and 4
    for i in range(amount-amount_decrease):    
        while 1:
            num = random.randint(0,4)
            if num in fclass and amount > 2: #check if numbe was already rolled | unless we are randomizing spell
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

@bot.command(aliases=['defind','search','class','spell','name','f'], description='''
Displays name of class, spell or element
''')
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
        num = -1
        for emoji in elements_emoji:
            num += 1
            if element == emoji:
                fclass += str(num) #save element numbers to variable

    #Send Class Name if it exist
    try: await ctx.channel.send(f'{classes[fclass]} {old_text}')  
    except KeyError: await ctx.channel.send(f"{old_text} Not Found")

@bot.command(description='''
Sends link to Fishards Wikipedia
''')
async def wiki(ctx, page: str = 'Home'):
    await ctx.channel.send('https://fishards.fandom.com/wiki/'+page)
    
#-------------------------------------------------------------------------------------------
    
@bot.command()
async def join(ctx):
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
  if voice and voice.is_connected(): await voice.disconnect()
  
  if ctx.author.voice: voice = ctx.author.voice.channel
  else: voice = 0

  if voice:
    await voice.connect()
    await ctx.channel.send(f"Joined {voice}")
  else: await ctx.channel.send("You Are Not In A Voice Channel")

@bot.command()
async def leave(ctx):
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
  if voice and voice.is_connected(): await voice.disconnect()
  else: await ctx.channel.send("Not Connected To Voice Channel")

@bot.command()
async def stop(ctx, num: int = 1):
    
    if num < 0: num = 1
    elif num > len(bot.queue) or not num:
        num = 0
        bot.queue = []
    
    for i in range(num - 1): bot.queue.pop(0)
    
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_playing(): voice.stop()


@bot.command()
async def tts(ctx, text):
    text = text.lower()
    
    if text in ['2', 'all']:
        for channel in ctx.guild.text_channels:
            bot.read_channel.add(channel) 
        await ctx.send('Global TTS ON')
        
        
    elif text in ['1', 'on']:
        bot.read_channel.add(ctx.channel)
        await ctx.send(f"TTS ON in {ctx.channel}")
        
        
    elif text in ['0', 'off']:
        try:
            bot.read_channel.remove(ctx.channel)
            await ctx.send(f"TTS OFF in {ctx.channel}")
        except Exception as e: 
            await ctx.send(f"TTS Was NOT ON in {ctx.channel}")
            
            
    elif text in ['-1', 'clear', 'stop']:
        bot.read_channel = {''}
        await ctx.send("TTS OFF")


@bot.command(aliases = ['lang'])
async def language(ctx, text: str = 'en'):

    if text in bot.langs:
        bot.voices[ctx.author.id] = text
        await ctx.send(f'Set Your Language as {text.upper()}')
        
    else:
        await ctx.send(f'{text.upper()} Is Not a Correct Code')
    
#-------------------------------------------------------------------------------------------

#Events

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    TimedStatus.start()

    
@bot.event
async def on_message(ctx):
    if not ctx.author.bot:
    
        if ctx.content != None:
        
            if ctx.content[0] != prefix and ctx.channel in bot.read_channel:
            
                if discord.utils.get(bot.voice_clients, guild=ctx.guild):
                    bot.queue.append((ctx.content, ctx.author.id))
                    play_queue(ctx)
                
                else:
                    await ctx.channel.send('Not Connected To Voice Chat\nTurning OFF TTS')
                    bot.read_channel = {''}
        
        await bot.process_commands(ctx)

            
bot.savePlayers = '-1'
@tasks.loop(minutes = 1)
async def TimedStatus(): #Change Status to a Random one Each Hour
    players = Player_Count()
    if players != bot.savePlayers:
        bot.savePlayers = players
        text = f'with {players} Players in Fishards'
        await bot.change_presence(activity=discord.Game(name = text))
            
#-------------------------------------------------------------------------------------------

bot.run(os.environ['TOKEN'])
