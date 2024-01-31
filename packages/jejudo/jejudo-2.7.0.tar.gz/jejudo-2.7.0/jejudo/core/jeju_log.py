import discord
from discord.ext import commands
import logging

logger: logging.Logger = logging.getLogger(__name__)

class log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f'[ system ] Jejudo in enabled bot: {self.bot.user.name}')

