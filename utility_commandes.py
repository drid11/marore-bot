from discord.ext import commands


class UtilityCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="commandes",description="vois les commandes que tu peux faire")
    async def commandes(self,ctx):
      await ctx.reply("il n'y a pas encore de commandes")
    @commands.hybrid_command(name="aide",description="reçois toutes les informations sur une commande")
    async def aide(self,ctx, *, commande:str):
      if commande=="commandes":
        reponse= "vois la liste des commandes disponibles"
      elif commande=="aide":
        reponse = "reçois toutes les informations sur une commande afin de savoir comment l'utiliser et a quoi elle sert"
      else:
        reponse = "un problème est survenu"
      await ctx.reply(reponse)
async def setup(bot):
    await bot.add_cog(HybrideCogs(bot))

