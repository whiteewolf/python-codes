import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    activity = discord.Game(name="Users Counting", type=2)
    await client.change_presence(status=discord.Status.idle, activity=activity)

client.run("token here")