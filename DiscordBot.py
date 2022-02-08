# importing the required library
import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module. There are a number of utility commands being showcased here.'''

# this is to use inorder to activate the commands
bot = commands.Bot(command_prefix='', description=description)

# This command will print out the good morning
@bot.command()
async def Gm(ctx, member):
    await ctx.send(f'good morning {member}, hope you have a wonderful day')

# on_ready will print out a message once i've been logged in
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# this commands add's two integers
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


# This will repeat the message in content multiple times
@bot.command()
async def repeat(ctx, times: int, content='BOT'):
    if(times > 4):
        return await ctx.send('Stop trying This Quinn!')
    else:
        for i in range(times):
            await ctx.send(content)

# Activate a message when someone joined
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

# Says if the user(subcommand) is cool
@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

# This command will print a certatin message if the cool function subcommand is a bot
@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

# This command will print a certatin message if the cool function subcommand is opai me lol
@cool.command(name='opai')
async def _bot(ctx):
    await ctx.send('Yes, ubay is cool.')

# This command will print a certatin message if the cool function subcommand is ubay me lol
@cool.command(name='ubay')
async def _bot(ctx):
    await ctx.send('Yes, ubay is cool.')

# This command will clear a max of 4 messages at a time
@bot.command(name = 'clear', help='this command will clear msgs')
async def clear(ctx, amount=2):
    if(amount > 4):
        return await ctx.send('You have exceeded the limit buddy, DONT TRY AGAIN!')
    else:
        await ctx.channel.purge(limit=amount)

# This command is a mini-8ball
@bot.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
   responses = ['As I see it, yes.',
              'Ask again later.',
              'Better not tell you now.',
              'Cannot predict now.',
              'Concentrate and ask again.',
              'Don’t count on it.',
              'It is certain.',
              'It is decidedly so.',
              'Most likely.',
              'My reply is no.',
              'My sources say no.',
              'Outlook not so good.',
              'Outlook good.',
              'Reply hazy, try again.',
              'Signs point to yes.',
              'Very doubtful.',
              'Without a doubt.',
              'Yes.',
              'Yes – definitely.',
              'You may rely on it.']
   await ctx.send(f'```Question: {question},\nAnswer: {random.choice(responses)}```')


# This command will print out to the screen the tasks we need to have done during the next week
@bot.command()
async def weekdue(ctx):
    await ctx.send(f' ```\t\t\t\t\tCONTENT COULD BE CHANGED IN DAILY 👏\nWed:           -math 2 Problem Sheet 1 q4     -due 03/02/2021.\nThursday:      -python lab                    -due 4/02/2020 before 6:00pm.\nFriday:        -C lab                         -due 5/02/2020 before 11:50pm.\nSunday:        -python Quiz 3                 -due 7/02/2020 before 11:59pm.``` ')

# This command will print out to the screen the tasks we need to have done during the week
@bot.command()
async def Nextweekdue(ctx):
    await ctx.send(f' ```\t\t\t\t\tCONTENT COULD BE CHANGED IN DAILY 👏\n\nWed:           -math 2 Problem Sheet 2        -due 10/02/2021.\nWed:           -STAT Class test 10 February   -11:00AM - 11:50AM           \nFriday:        -C lab week 3                  -due 5/02/2020 before 11:50pm.\nSunday:        -python Quiz 4                 -due 14/02/2020 before 11:59pm.\nSunday:        -Math 1 Webwork                 -due 14/02/2020 before 11:59pm.``` ')

@bot.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send('Hello! {0.author.mention} whats up!'.format(message))

    if message.content.startswith('Gm'):
        await message.channel.send('good morning  {0.author.mention}, hope you have a wonderful day'.format(message))

    if message.content.startswith('Gf'):
        await message.channel.send('good afternoon  {0.author.mention}, hope you have a wonderful day'.format(message))

    if message.content.startswith('week due'):
        await message.channel.send(' \t\t\t\tlisten {0.author.mention} carefully ```\n\t\t\t\t\tCONTENT COULD BE CHANGED IN DAILY 👏\nWed:           -math 2 Problem Sheet 1 q4     -due 03/02/2021.\nThursday:      -python lab                    -due 4/02/2020 before 6:00pm.\nFriday:        -C lab                         -due 5/02/2020 before 11:50pm.\nSunday:        -python Quiz 3                 -due 7/02/2020 before 11:59pm.``` '.format(message))
    
    if message.content.startswith('asta3frallah'):
        await message.channel.send('asta3frallah asta3frallah asta3frallah asta3frallah asta3frallah')
# run the bot with the login token
bot.run('YOUR_TOKEN')
