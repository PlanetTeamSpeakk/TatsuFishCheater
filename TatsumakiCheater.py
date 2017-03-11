try:
    import discord
except:
    print("Discord.py is not installed, installing it now...")
    from subprocess import check_output
    check_output("pip3 install discord.py", shell=True)
    try:
        import discord
        print("Successfully installed discord.py")
    except:
        import sys
        sys.exit("Discord.py could not be installed, exiting.")
        
from discord.ext import commands
bot = commands.Bot(command_prefix="s!", self_bot=True)
from asyncio import sleep

print("MAKE SURE THAT YOU DO NOT HAVE OAUTH2 ENABLED!!!")
email = input("What's your Discord email address?\n> ")
while "@" not in email:
    email = input("That's not a valid email, try again.\n> ")
password = input("What's your Discord password?\n> ")
print("\n" * 666666)
print("Starting...")

@bot.event
async def on_ready():
    print("Bot started! Now type s!cheattatsufish anywhere where Tatsumaki is to start cheating u lil scum.")
    
@bot.command()
async def cheattatsufish():
    await bot.say("**Tatsu cheating started. To stop, kill the process.**")
    counter = 0
    while True:
        await bot.say("~fish")
        counter += 1
        if counter >= 10:
            await sleep(6)
            await bot.say("~fish sell garbage")
            await sleep(6)
            await bot.say("~fish sell common")
            await sleep(6)
            await bot.say("~fish sell uncommon")
            await sleep(6)
            await bot.say("~fish redeem octopus")
            counter = 0
        await sleep(35)
        
bot.run(email, password)