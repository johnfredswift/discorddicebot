
## Overview

Simple Discord bot for dicerolling, offers a digital solution to any faced dice and numerous other use-cases that may be needed in either D&D. It also offers a group 1-100 roller similar to the !roll command within World of Warcraft.


## Usage

Requires an API key from Discord Developer Portal for usage inside of the `os.getenv['API_KEY']`. This is placed within a "token.txt" file in the same folder as the bot.py file. This is a crude solution to hiding the API token from Github but serves the usecase at the moment.

Within the channels the commands are:
(x is any positive integer number)

* `!roll` rolls a random number between 1 and 100 
* `!roll x` displays x. This is used in conjuction of other varibles to give sums of complete dice sets
* `!roll dx` rolls 1 dice of x faces.
* `!roll xdy` rolls x dice of y faces
* `!roll 1d2 3 d4` rolls 1 2-sided dice, displays 3 and rolls 1 4-sided dice. This is just an example and it will work with any variations of the commands given and display them by the dice, what they rolled and the total sum of the single command
* `!newgrouproll` creates a group roll. Only one may be active at a time across a server. This is designed to help a group of members of a discord resolve a winner of a situation in an unbias and speedy fashion.
* `!grouproll` Each user can use this command once while a grouproll is active. This will roll a number between 1 and 100 and store it till the grouproll has ended.
* `!endgrouproll` ends the currently group roll. On ending a winner is shown aswell as all participants in decreasing scores, including what roll they achieved.

Output is displayed within the same channel the command was typed
## Deployment

There are no deployment plans at the moment, within devolpment it is ran through terminal. Should this be deployed it could be done through a AWS instance or another cloud soultion with relative ease.