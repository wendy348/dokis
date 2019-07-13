import discord, random, asyncio
from discord.ext import commands as client
from Cogs.config import conf
#Imports


class Changelog(client.Cog):

    def __init__(self, bot):
         self.b = bot 

    @client.command()
    async def changelog(self,ctx): #dd/mm/yy
        e = discord.Embed(title=f"A beta update! This has been changed at 12/07/2019. Version: {conf.version}",description='''
```

I am almost ready. I just hope Yuri doesn't try to have sex with me. -MC 

```
''', color=conf.norm)
        e.set_author(name=f"The Changelog for {conf.name}.",icon_url=self.b.user.avatar_url)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Changelog(bot))
