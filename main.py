import requests
import discord
from discord.ext.commands import Bot
TOKEN = 'Your_Discord_Bot_Token'
client = discord.Bot()
@client.event
async def on_ready():
    print("on_ready")
@client.slash_command()
async def url_shortener(ctx,url):
    pointt='https://api-ssl.bitly.com/v3/shorten'
    access_token = 'Your_Bitly_API_Token'
    payloads={
        'access_token': access_token,
        'longurl':url
    }
    r = requests.get(pointt,params=payloads).json()['data']['url']
    await ctx.respond(r)
client.run(TOKEN)
