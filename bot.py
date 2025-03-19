import os
import sys
from dotenv.main import dotenv_values
import interactions
from stravalib import Client

config = dotenv_values(".env")

STRAVA_CLIENT_ID = int(str(config["STRAVA_CLIENT_ID"]))
STRAVA_CLIENT_SECRET = str(config["STRAVA_CLIENT_SECRET"])
strava_client = Client() 

print(STRAVA_CLIENT_ID)

if strava_client is None:
    print(ValueError("Strava client empty")) 

#strava_client.refresh_access_token(STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, "f890f0cdb8c1b8c2a93eae4bfeb668f31b9d4d41")

url = strava_client.authorization_url(
    client_id=STRAVA_CLIENT_ID,
    redirect_uri="http://127.0.0.1/authorization",
)
token_response = strava_client.exchange_code_for_token(
    client_id=STRAVA_CLIENT_ID,
    client_secret=STRAVA_CLIENT_SECRET,

    code="174702ccc769b96954a40c83bc4231e85fce1b84"
)
access_token = token_response["access_token"]
refresh_token = token_response['refresh_token']

athlete = strava_client.get_athlete()
print(f"{athlete.firstname}'s token expires at {token_response}")


GUILD_ID = config["GUILD_ID"]
BOT_TOKEN = config["BOT_TOKEN"]

bot = interactions.Client(intents=interactions.Intents.DEFAULT)

@interactions.listen()
async def on_ready():
    print("ready")
    print(f"Logged in as {bot.user}")
@interactions.listen()
async def on_message_create(event):
    print(f"Message received: {event.message.jump_url}")


@interactions.slash_command(name="howdy", description="Howdy howdy howdy!", scopes=[1117995178171564143])
async def howdy_command(ctx: interactions.SlashContext):
    await ctx.send("Howdy!")


print(url)
bot.start(BOT_TOKEN)

