# Discord.py is smoooooooooooooosh!!!!!
import discord
from discord.ext import tasks, commands
import asyncio
import os # .env読み込みスターズ。
import json

def json_load(path):
    with open(path, "r") as f:
        f = str(f).replace("'", '"').replace('True', 'true').replace('False', 'false')
        return json.loads(f)

class Server_Stats(commands.Cog):
    def __init__(self, airlinia):
        self.bot = airlinia #botを受け取る。
        self.datas = json_load("./data/pokemon.json")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        datas = self.datas
        server = member.guild
        datas["all"] = len(server.members)
        datas["member"] = len([member for member in server.members if not member.bot])
        datas["bot"] = len([member for member in server.members if member.bot])
        with open("./data/pokemon.json", "w") as file:
            json.dump(file, datas, indent=4)
        await channel_name_edit()

    @commands.Cog.listener()
    async def on_message(self, message):
        datas = self.datas
        server = message.guild
        if message.author.bot:  # ボットのメッセージをハネる
            return
        datas["message"] += 1
        with open("./data/pokemon.json", "w") as file:
            json.dump(file, datas, indent=4)
        await channel_name_edit()

    @commands.Cog.listener()
    async def on_member_updata(self, before, after):
        datas = self.datas
        server = after.guild
        datas["online"] = len([member for member in server.members if member.status.online])
        datas["idle"] = len([member for member in server.members if member.status.idle])
        datas["dnd"] = len([member for member in server.members if member.status.dnd])
        datas["offline"] = len([member for member in server.members if member.status.offline])
        with open("./data/pokemon.json", "w") as file:
            json.dump(file, datas, indent=4)
        await channel_name_edit()

    async def channel_name_edit():
        datas = self.datas
        self.all_channel : discord.VoiceChannel = self.bot.get_channel(663297143909515274)
        self.member_channel : discord.VoiceChannel = self.bot.get_channel(663297196531253249)
        self.bot_channel : discord.VoiceChannel = self.bot.get_channel(663297233453842452)
        self.online_channel : discord.VoiceChannel = self.bot.get_channel(663297268455309332)
        self.idle_channel : discord.VoiceChannel = self.bot.get_channel(664160147886833678)
        self.dnd_channel : discord.VoiceChannel = self.bot.get_channel(664160201125003295)
        self.offline_channel : discord.VoiceChannel = self.bot.get_channel(663297305847398421)
        self.message_channel : discord.VoiceChannel = self.bot.get_channel(663297421417119754)
        self.time_channel : discord.VoiceChannel = self.bot.get_channel(663297453621116988)
        # await self.all_channel.edit(name=f"all : {datas["all"]}")
        # await self.member_channel.edit(name=f"member : {datas["member"]}")
        # await self.bot_channel.edit(name=f"bot : {datas["bot"]}")
        await self.online_channel.edit(name=f"online : {datas["online"]}")
        await self.idle_channel.edit(name=f"idle : {datas["idle"]}")
        await self.dnd_channel.edit(name=f"dnd : {datas["dnd"]}")
        await self.offline_channel.edit(name=f"offline : {datas["offline"]}")
        # await self.message_channel.edit(name=f"message : {datas["message"]}")
        # await self.time.all_channel.edit(name=f"time : {datas["time"]}")

def setup(airlinia):
    airlinia.add_cog(Server_Stats(airlinia))
