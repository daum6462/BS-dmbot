import discord
import asyncio
import datetime

client = discord.Client()

__TOKEN__ = 'OTA4NTUxMTM2MDYyMDg3MTY5.YY3YLg.SyEwj-R1zKL6CLym-wg9Vql9dKg'
titlke = '보안최강 AINWIN'

@client.event
async def on_ready():
    print("봇이 정상상적으로 실행 되었습니다")
    #game = discord.Game('뒷메돌리기')
    #await client.change_presence(status=discord.Status.online, activity=game)

#!디엠 {할말}
@client.event
async def on_message(message):
    if message.content.startswith('!디엠'):
        for i in message.guild.members:
            if i.bot:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id ==897471888043937792:
                 if message.author.guild_permissions.manage_messages:897471888043937792
                        embed = discord.Embed(title=tile, description=msg, colour=discord.Colour.gold(), timestamp=message.created_at, title="보안최강 AINWIN
                        embed .add_field
                        #embed.set_footer(text="맨 밑에 들어갈 내용")
                        await i.send(embed=embed)
                        print(f'{i} 전송')
                except:
                    pass


client.run('OTA4NTUxMTM2MDYyMDg3MTY5.YY3YLg.SyEwj-R1zKL6CLym-wg9Vql9dKg')
