# Discord.py is smoooooooooooooosh!!!!!
import discord
from discord.ext import commands
import asyncio
import os # .env読み込みスターズ。
# AI is cooooooooooooooooooooool!!!!!
import pya3rt

class Talk_Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot #botを受け取る。
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:  # ボットのメッセージをハネる
            return
        if message.channel.id == 663043626418569256:
            client = pya3rt.TalkClient(os.environ['TALK_API_KEY'])
            content = client.talk(message.content)['results'][0]['reply']
            await message.channel.send(content) # 返信メッセージを送信

def setup(bot):
    bot.add_cog(Talk_Bot(bot))