import base64
import binascii
import webbrowser
import os
import time
from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import json
import requests
import pyperclip
import winsound

os.system('color')



with open('webhook.json') as json_file:
    data = json.load(json_file)
    for p in data['data']:
        webhook_url = p['webhook']
        accessToken = p['accessToken']
        


print(colored("*************************************" , 'magenta'))
print(colored("---------   Basic Decode  ----------" , 'red'))
print(colored("-------      zuna#1703      --------" , 'red'))
print(colored("*************************************" , 'magenta'))
print(colored("DISCLAIMER: Using the auto-invite-joiner may cause your account to be banned.\n" , 'red'))


auswahl = int(input(colored("1. Base64 \n2. Base32 \n4. Hex-Code \n Your choice: ", 'blue')))
invite = str(input("Discord Invite? y/n    "))

if auswahl == 1:
    encoded64 = str(input(colored("Enter your Base64 Code:  ", 'green')))

    sol64 = base64.b64decode(encoded64).decode('utf-8')

    print(sol64)
    pyperclip.copy(sol64)

    print("\nCode copied to your clipboard!\n")


    if invite == 'y':
        
        inviteCode = (sol64.split("discord")[1]).split("/")[1]
        
        headers = {
                'authorization': accessToken
                }
        
        data = {
                            "code": inviteCode,
                            "new_member": "true"
                        }


        r = requests.post("https://discordapp.com/api/v6/invites/"+inviteCode,json=data,headers=headers)
        print(colored("Successfully joined the server!\n"), 'blue')
        
        webhook = DiscordWebhook(url=webhook_url)

        embed = DiscordEmbed(title='You opened an invite!', color=4886754)

        embed.set_author(name='SimplerDecode', url='https://twitter.com/akamaicookie', icon_url='https://images-ext-2.discordapp.net/external/j_rSYII522rRzIVVaeWFNDghqP9zNL8Q3PD0DbyQhyY/%3Fwidth%3D671%26height%3D671/https/media.discordapp.net/attachments/719857127362920448/721781682885099600/Celer_Restocks_Salute.png')


        webhook.add_embed(embed)

        response = webhook.execute()

        

if auswahl == 2:
    encoded32 = str(input(colored("Enter your Base32 Code:  ", 'green')))
    
    sol32 = base64.b32decode(encoded32).decode('utf-8')

    print(sol32)
    pyperclip.copy(sol32)

    print("\nCode copied to your clipboard!\n")
    if invite == 'y':
        inviteCode = (sol32.split("discord")[1]).split("/")[1]
        
        headers = {
                'authorization': accessToken
                }
        
        data = {
                            "code": inviteCode,
                            "new_member": "true"
                        }


        r = requests.post("https://discordapp.com/api/v6/invites/"+inviteCode,json=data,headers=headers)
        print(colored("Successfully joined the server!\n"), 'blue')
        
        webhook = DiscordWebhook(url=webhook_url)

        embed = DiscordEmbed(title='You opened an invite!', color=4886754)

        embed.set_author(name='CelerDecode', url='https://twitter.com/CelerRestocks', icon_url='https://images-ext-2.discordapp.net/external/j_rSYII522rRzIVVaeWFNDghqP9zNL8Q3PD0DbyQhyY/%3Fwidth%3D671%26height%3D671/https/media.discordapp.net/attachments/719857127362920448/721781682885099600/Celer_Restocks_Salute.png')


        webhook.add_embed(embed)

        response = webhook.execute()


if auswahl == 4:
    encodedhex = str(input(colored("Enter your Hex-Code:  ", 'green')))

    sol_hex = bytearray.fromhex(encodedhex).decode()

    print("Your decoded Hex-Code: " + sol_hex)

    pyperclip.copy(sol_hex)

    print("\nCode copied to your clipboard!\n")


    if invite == 'y':
        inviteCode = (sol_hex.split("discord")[1]).split("/")[1]
        
        headers = {
                'authorization': accessToken
                }
        
        data = {
                            "code": inviteCode,
                            "new_member": "true"
                        }


        r = requests.post("https://discordapp.com/api/v6/invites/"+inviteCode,json=data,headers=headers)
        
        print(colored("Successfully joined the server!\n"), 'blue')

        webhook = DiscordWebhook(url=webhook_url)

        embed = DiscordEmbed(title='You opened an invite!', color=4886754)

        embed.set_author(name='SimpleDecode', url='https://twitter.com/akamaicookie', icon_url='https://images-ext-2.discordapp.net/external/j_rSYII522rRzIVVaeWFNDghqP9zNL8Q3PD0DbyQhyY/%3Fwidth%3D671%26height%3D671/https/media.discordapp.net/attachments/719857127362920448/721781682885099600/Celer_Restocks_Salute.png')


        webhook.add_embed(embed)

        response = webhook.execute()


print(colored("DM zuna#1703 if you have any questions!", 'green'))
print(Style.DIM + "\nYou can exit this window now.")






