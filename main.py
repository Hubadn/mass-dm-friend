import discord
import json

self_bot = discord.Client()

with open("./config.json", "r") as config:
    get = json.load(config)
    token = get["token"]
    message = get["message"]

@self_bot.event
async def on_ready():
  print("mass-dm-friend is running")

  print(f"longin as : {self_bot.name} ")

  for user in self_bot.user.friends:
    try:

      await user.send(message)

      print(f"Successfully message sent to: {user.name}")
    except:
       print(f"Failed to send message to: {user.name}")
  print(f"{self_bot.user.name} hass finished mdming!")

self_bot.run(token, bot=False)
