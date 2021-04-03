import discord
from discord.ext import commands

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await channel.guild.fetch_member(payload.user_id)
        if message.author.id == 172002275412279296 and payload.emoji.name == "🍆":
            unv = message.guild.get_role(824438341918654476)
            mem = message.guild.get_role(824439001695125555)

            if unv in user.roles:
                print("Verifying roles")
                await user.remove_roles(unv)
                await user.add_roles(mem)
                print("Done.")



def setup(bot):
    bot.add_cog(Verify(bot))
