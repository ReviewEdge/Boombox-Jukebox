#! /usr/bin/python3

import os


# TOOLBAR
# Version: 1.2
# Released: 6/4/2019
# Author: Logan Richardson
# Updated: 6/4/2019


# Sets up browser settings:
os.system("xset s noblank; xset s off; xset -dpms")
os.system("unclutter -idle 7 -root &")


# os.system("sed -i 's/\"exited_cleanly\":false/\"exited_cleanly\":true/' /home/pi/.config/chromium/Default/Preferences")
# os.system("sed -i 's/\"exit_type\":\"Crashed\"/\"exit_type\":\"Normal\"/' /home/pi/.config/chromium/Default/Preferences")


def jukebox():
    print("Running Jukebox...")
    os.system("./Boombox-Jukebox_v3.1.py &")


def youtube():
    print("Opening YouTube...")
    os.system("chromium-browser --start-fullscreen youtube.com/playlist?list=PLA1lSvz1-osAeZSLC6Ro41Z9vGmkrUujD &")


def chromium():
    print("Opening Chromium...")
    os.system("chromium-browser &")


def file_explorer():
    print("Opening File Explorer...")
    os.system("pcmanfm &")


def thonny():
    print("Opening Thonny (Python Editor)...")
    os.system("thonny &")


def terminal():
    print("Opening Terminal...")
    os.system("gnome-terminal & disown &")


def settings():
    print("Opening Settings...")


def min():
    print("Minimizing...")
    os.system("xdotool windowminimize $(xdotool getactivewindow)")


# Minimizes the Toolbar window on startup:
min()

x = "on"
while x != "off":
    x = input("Enter: 'j' 'y' 'c' 'f' 't' 's' '?' 'min' 'off'\n").lower()

    if x == "j":
        jukebox()

    if x == "y":
        youtube()

    if x == "c":
        chromium()

    if x == "f":
        file_explorer()

    if x == "p":
        thonny()

    if x == 't':
        terminal()

    if x == "s":
        settings()

    if x == "min":
        min()

    if x == "?":
        print("'j': Opens Jukebox Program\n'y': Opens a YouTube Tab in Chromium\n'c': Opens a Chromium Window")
        print(
            "'f': Opens File Explorer\n'p': Opens Thonny Python Editor\n't': Opens New Terminal Window\n's': Opens Settings\n'min': Minimizes the Toolbar Window\n'off' Ends the Toolbar Program")

# Add spotify controls

