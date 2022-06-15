import discord
import json
from discord.ext import commands
from keep_alive import keep_alive

#imports of cogs

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
    owner_id="744986260795556013",
    description="Im a bot yo ahahahah"
)



bot.change_presence(activity=discord.Game("with balls"))


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

extensions = [
    'cogs.core',
    'cogs.music'
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

f = open('config.json')
data = json.load(f)

bot.run(data["TOKEN"])