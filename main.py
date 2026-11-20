import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ["utility_commandes"]:
            await self.load_extension(f'cogs.{extension}')
bot = MonBot(command_prefix="%", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("le bot est en ligne")

    try:

        synced = await bot.tree.sync()
        print(f"syncro: {len(synced)}")

    except Exception as e:
        print("e")


token = os.getenv('DISCORD_TOKEN')
bot.run(str(token))