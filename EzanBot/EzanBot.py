import discord
from discord.ext import commands
from datetime import datetime
import youtube_dl
from time import time, sleep
import asyncio
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
client = commands.Bot(command_prefix = '$')

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

async def ezanSpielen():
    print('moin')
    while True:
        sleep(5 - time() % 5)
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        if current_time == '04:30' or current_time == '06:10' or current_time == '13:10' or current_time == '16:55' or current_time == '20:00' or current_time == '21:30' or current_time == '17:10':
            print("penis")
            channel = client.get_channel(787098685552590896)
            voicechannel = await channel.connect()
            voicechannel.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source= r"C:\Users\meozo\Desktop\EzanBot\EzanMusic.mp3"))
        @client.command()
        async def gönn(ctx):
            channel = client.get_channel(787098685552590896)
            voicechannel = await channel.connect()
            voicechannel.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source= r"C:\Users\meozo\Desktop\EzanBot\EzanMusic.mp3"))
            #voicechannel.play(discord.FFmpegPCMAudio('EzanMusic.mp3'))
            #voice_client = client.guild.voice_client(channel)
            #player = await voice_client.create_ytdl_player('https://www.youtube.com/watch?v=HlWPAUqqYTs')
            #players[server.id] = player
            #player.start()
        #@client.command()
        #async def heehee(ctx):
        #    channel = client.get_channel(787098685552590896)
        #    voicechannel = await channel.connect()
        #    voicechannel.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source= r"C:\Users\meozo\Desktop\EzanBot\hee hee.mp3"))

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    general_channel = client.get_channel(787091121062150186)

    await ezanSpielen()


#run client on server
client.run('ODM1MTc0NDIzMjc1MzcyNjM2.YILmyw.NuHsENAQ3w7uOGpMn2MzPMT0rc8')