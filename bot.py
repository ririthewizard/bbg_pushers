import os
import sys
import interactions
from dotenv import dotenv_values, find_dotenv, load_dotenv
from stravalib import Client

config = dotenv_values(".env")

strava_client_id = 152444
strava_client_secret = str(config["STRAVA_CLIENT_SECRET"])
strava_client = Client() 
url = strava_client.authorization_url(
    client_id=152444,
    redirect_uri="http://localhost/authorization",
)

token_response = strava_client.exchange_code_for_token(
    client_id=strava_client_id,
    client_secret=strava_client_secret,
    code="7251c81f7ea195db7895030874b3c5fc4a2fcfed")


guild_id = os.getenv("GUILD_ID")
bot_token = os.getenv("BOT_TOKEN")
bot = interactions.Client(intents=interactions.Intents.DEFAULT) 

@interactions.listen()
async def on_ready():
    print("Ready")
    print(f"Logged in as {bot.user}")

@interactions.listen()
async def on_message_create(event):
    print(f"Message received: {event.message.jump_url}")


@interactions.slash_command(name="howdy", description="Howdy howdy howdy!", scopes=[1117995178171564143])
async def howdy_command(ctx: interactions.SlashContext):
    await ctx.send("Howdy!")


print(url)
bot.start(bot_token)

