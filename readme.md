## Overview

Simple Discord bot for dicerolling, offers a digital solution to any faced dice and numerous other use-cases that may be needed in either D&D. It also offers a group 1-100 roller helping divid

## Install

Dependencies can be installed into a virtual environment, with pip, using the commands

```
python3 -m venv <virtual_env_name>
pip install -r requirements.txt
```

## Usage

Requires an API key from Discord Developer Portal for usage inside of the `os.getenv['API_KEY']` and a channel ID for the appropriate channel messages are to be placed into, this is retrieved via `os.getenv['CHANNEL_ID']` as part of running the client.

Within the channels the commands are:

* `!newvote movie 1, movie 2, movie 3, ...` starts a new vote, only those with the role of 'Admin' can begin a vote.
* `!vote X Y Z` allows people to vote after a new vote has begun, the values correspond to the numerical value within list that is presented by the bot. Votes are weighted in order: the first vote is worth 3 points, the second is worth 2, and the last vote is worth 1.
* `!changevote X Y Z` someone can change their vote if it has already been cast, reusing `!vote` would stop them duplicating the vote.
* `!standings` will display the current points for each movie.
* `!endvote` will end the vote casting and write the movie with the highest number of points into the channel.

## Deployment

A simple deployment is achieved through a t2.micro Ubuntu instance on AWS. The Python file is run via tmux first, so that the process does not stop upon closing the SSH session. There is an argument for running it as a daemon, but this is not too important.