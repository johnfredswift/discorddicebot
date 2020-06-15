import discord
from discord.ext import commands
import roll


client = commands.Bot(command_prefix = '!')
voters = {}

@client.event
async def on_ready():
    print("Bot bis beady!")
    
@client.command()
async def b(ctx, *inputs):
    message = ""
    if len(inputs) == 0:
        message = 'Bello Bere!'
    else:
        message = ' '.join(inputs)
    await ctx.send(message)

@client.command(aliases=['roll'])
async def _roll(ctx, *inputs):
    await ctx.send(roll.parseInput(inputs, ""))

@client.command()
async def sum(ctx, *inputs):
    await ctx.send(roll.parseInput(inputs, "sum"))

@client.command()
async def endgrouproll(ctx, *inputs):
    if voters == False:
        await ctx.send("There is no active roll group, roll groups can be created with !newgrouprole")
    else:
        await ctx.send("Rolling has ended!")
        del voters[""]
        sortVoters = sorted(voters.items(), key=lambda x: x[1], reverse=True)
        output = '\n'
        await ctx.send(sortVoters[0][0] + " has won with a score of " + str(sortVoters[0][1]))
        for i in sortVoters[1:]:
            output += str(i[0]) + " rolled a " + str(i[1]) + '\n'
        await ctx.send(output)
        voters.clear()
    
@client.command()
async def newgrouproll(ctx):
    if len(voters) > 1:
        await ctx.send("There is an active roll group, please close with !endgrouprole first")
    else:
        voters.clear()
        voters[""] = 0
        await ctx.send("Rolling has started! You can vote with the !grouproll")

        
@client.command()
async def grouproll(ctx):
    if (len(voters) < 1):
        await ctx.send("No active vote, please start a group vote with !newgrouproll")
    else:
        author = ctx.message.author.name
        if not (author in voters):
            voters[author] = roll.roll100()
        else:
            await ctx.send(f"{author} has already rolled!")


botToken = open("token.txt")
client.run(botToken.read())