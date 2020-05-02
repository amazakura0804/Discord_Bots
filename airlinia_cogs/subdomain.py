# Discord.py is smoooooooooooooosh!!!!!
import discord
from discord.ext import commands
import asyncio

import os
from cloudflare_ddns import CloudFlare
import pymongo

class Sub_Domain(commands.Cog):
    def __init__(self, airlinia):
        self.bot = airlinia

        mongo_connection = pymongo.MongoClient("ds161505.mlab.com", 61505, retryWrites=False)
        mongo_db = mongo_connection["heroku_stfrs35p"]
        mongo_db.authenticate("heroku_stfrs35p", os.environ['MONGODB_PASSWORD'])
        self.mongo_coll = mongo_db['subdomain']

        self.cf = CloudFlare("amazakura0804@gmail.com", os.environ["CLOUDFLARE_API_KEY"], "iufs.jp")
        self.cf.sync_dns_from_my_ip()

    @commands.command(name='url')
    async def _url(self, ctx, sub_domain, ip_address):
        # .gov.iufs.jp .news.iufs.jp .年
        result = cf.create_record('A', sub_domain + ".gov.iufs.jp", ip_address)

        x = {}
        x["user"] = ctx.user.id
        await ctx.send(f'短縮URLを作成しました！{data["link"]}') # 返信メッセージを送信

def setup(airlinia):
    airlinia.add_cog(Sub_Domain(airlinia))