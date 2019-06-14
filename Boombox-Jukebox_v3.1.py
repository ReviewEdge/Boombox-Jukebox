#! /usr/bin/python3

import time
import os
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
# Screen Drawing Imports:
import pprint
import requests
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from PIL import ImageFont, ImageDraw



# BOOMBOX-JUKEBOX
# Version: 3.1
# Released: 4/13/2019
# Author: Logan Richardson
# Updated: 6/1/2019

# Update Info: added song
# (single) screen display,
# re-implemented art display,
# changed post new song cooldown
# to 4 seconds

# Spotify API:

# Gives Spotify credentials:
username = "xxxxx"
scope = "user-read-currently-playing"

# Gives developer app credential:
ID = "xxxxx"
SECRET = "xxxxx"
URI = "http://google.com/"

# Erase cache and prompt for user permission:
try:
    token = util.prompt_for_user_token(username, scope, ID, SECRET, URI)  # add scope
except (AttributeError, JSONDecodeError):
    os.remove(".cache-" + username)
    token = util.prompt_for_user_token(username, scope, ID, SECRET, URI)  # add scope

# Creates Spotify Object
sp = spotipy.Spotify(auth=token)

# Functions to get current music information:
def get_art_url():
    return sp.current_user_playing_track()['item']['album']['images'][0]["url"]


def get_song():
    return sp.currently_playing()["item"]["name"]


def get_artist():
    return sp.currently_playing()["item"]["artists"][0]["name"]


# Function to display song and artist:

serial = i2c(port=1, address=0x3C)

#serial_1 = i2c(port = 1, address = 0x78)
#serial_2 = i2c(port = 1, address = 0x7A)


device = ssd1306(serial, rotate=0)

#device_1 = ssd1306(serial_1, rotate=0)
#device_2 = ssd1306(serial_2, rotate=0)


def display_song_and_artist(song, artist):
    screen_display = song + "\n" + "- " + artist
    with canvas(device) as draw:
        draw.text((0, 0), screen_display, fill="white")




# Terminal Commands:
# Sets up Pi audio:
os.system("sudo amixer cset numid=1 100%")
os.system("sudo amixer cset numid=3 1")

# Sets up browser settings:
os.system("xset s noblank; xset s off; xset -dpms")
os.system("unclutter -idle 7 -root &")
os.system("sed -i 's/\"exited_cleanly\":false/\"exited_cleanly\":true/' /home/pi/.config/chromium/Default/Preferences")
os.system(
    "sed -i 's/\"exit_type\":\"Crashed\"/\"exit_type\":\"Normal\"/' /home/pi/.config/chromium/Default/Preferences")



# Runs processes

displayed_art_url = get_art_url()

displayed_song = get_song()

run = 1
while 1:
    latest_art_url = get_art_url()

    latest_song = get_song()
    latest_artist = get_artist()

    # Starts browser for first time
    if run == 1:
        print("first time")
        displayed_art_url = latest_art_url

        os.system(
            "/usr/bin/chromium-browser --noerrdialogs --disable-infobars --start-fullscreen " + latest_art_url + " &")

        # Changes song display:
        displayed_song = latest_song
        display_song_and_artist(latest_song,latest_artist)

        run = 2
        time.sleep(2)

    # Updates (art and song) if art display is out of sync with current ART:
    elif latest_art_url != displayed_art_url:
        displayed_art_url = latest_art_url

        displayed_song = latest_song
        display_song_and_artist(latest_song, latest_artist)

        os.system("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --start-fullscreen " + latest_art_url)

        # Opens window a second time to make full screen
        os.system("/usr/bin/chromium-browser --noerrdialogs --disable-infobars --start-fullscreen " + latest_art_url)

        # extra wait time, assumes song was just changed
        time.sleep(5)

    # Updates (just song) if song display is out of sync with current SONG:
    elif latest_song != displayed_song:
        displayed_song = latest_song
        display_song_and_artist(latest_song, latest_artist)

        # extra wait time, assumes song was just changed
        time.sleep(4)

    # Waits if in sync
    else:
        time.sleep(3)







