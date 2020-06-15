import discord
import random
from discord.ext import commands

#parseInput returns either result of a d100 or a list of dice rolls and there original dice faces
def parseInput(inputs, type):

    listInputs = list(inputs)
    diceOutputs = []
    if len(listInputs) == 0:
        return random.randrange(99) + 1
    else:
        for x in inputs:
            if not('d' in x):
                diceOutputs.append(x)
            else:
                if x[0] == 'd':
                    x = '1' + x
                quant, faces = x.split('d')
                diceSet = []
                for _ in range(int(quant)):
                    currentDice = [faces, rollx(faces)]
                    diceSet.append(currentDice)
                diceOutputs.append(diceSet)
        return diceOutputs
                    


        # return rollX(listInputs, type)

def roll100():
    return random.randrange(99) + 1


def rollx(faces):
    return random.randrange(int(faces)) + 1



