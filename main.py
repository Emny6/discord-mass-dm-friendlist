import discord
import colorama
import os
import json
import datetime
from colorama import Fore

class utils:
    def rename(name):
        os.system(f'title MASS DM FRIENDS LIST - {name} - @zeeckt')
def banner():
        print(f" ")
        print(f" ")
        print(f"{Fore.CYAN}          ╔═══════════════════════════════════════════════╗{Fore.RESET}")
        print(f"{Fore.CYAN}          ║   ╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔╦╗  ╔═╗╦═╗╦╔═╗╔╗╔╔╦╗╔═╗   ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ║   ║║║╠═╣╚═╗╚═╗   ║║║║║  ╠╣ ╠╦╝║║╣ ║║║ ║║╚═╗   ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ║   ╩ ╩╩ ╩╚═╝╚═╝  ═╩╝╩ ╩  ╚  ╩╚═╩╚═╝╝╚╝═╩╝╚═╝   ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ║                 ~ Developed by zeeckt.        ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ╚═══════════════════════════════════════════════╝{Fore.RESET}")
        print(f" ")
        print(f" ")
banner()
token = input(f"{Fore.LIGHTWHITE_EX} [+] Insert token: ")
message = input(f"{Fore.LIGHTWHITE_EX} [+] Insert message: ")
dateTimeObj = datetime.datetime.now()
timestampStr = dateTimeObj.strftime("%H:%M:%S")
os.system('cls')
def banner():
        print(f" ")
        print(f" ")
        print(f"{Fore.CYAN}          ╔═══════════════════════════════════════════════╗{Fore.RESET}")
        print(f"{Fore.CYAN}          ║   ╔╦╗╔═╗╔═╗╔═╗  ╔╦╗╔╦╗  ╔═╗╦═╗╦╔═╗╔╗╔╔╦╗╔═╗   ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ║   ║║║╠═╣╚═╗╚═╗   ║║║║║  ╠╣ ╠╦╝║║╣ ║║║ ║║╚═╗   ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ║   ╩ ╩╩ ╩╚═╝╚═╝  ═╩╝╩ ╩  ╚  ╩╚═╩╚═╝╝╚╝═╩╝╚═╝   ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ║                 ~ Developed by zeeckt.        ║{Fore.RESET}")
        print(f"{Fore.CYAN}          ╚═══════════════════════════════════════════════╝{Fore.RESET}")
        print(f" ")
        print(f" ")
banner()

mdmbot = discord.Client()

@mdmbot.event
async def on_connect():

  for user in mdmbot.user.friends:
    try:

      await user.send(message)

      print(f" {Fore.LIGHTGREEN_EX}[{timestampStr}] [+] The message was successfully sent to: {user.name} {Fore.RESET}")
    except:
       print(f" {Fore.RED}[{timestampStr}] [-] Unable to send message to: {user.name} {Fore.RESET}")

mdmbot.run(token, bot=False)