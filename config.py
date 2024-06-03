# Imports
from datetime import datetime
import time
import json


# Game Mode
GAME_MODE = 'arena'  #farm/arena

# Img Directory
IMG_DIR = '/Users/xavierserranochico/Development/tarochi_play/img/'
        
# PyAutoGui Settings
CURSOR_SPEED = 1
SECONDS = 60
MENU_SPEED = .99
CLICK_SPEED = .47
SWAP_SPEED = 15


# Setting Varibale Threshold
CAPTURE_HEALTH_LESS_THAN = 25
HEALTH_LESS_THAN = 80
CAPTURE_PERCENT= 85
MATCH_PERCENT = 80

# PushOver End Point parameters
PUSHOVER_URL = 'https://api.pushover.net/1/messages.json'
TOKEN = 'askas5xqo63nryexenypnbd6i3b2nm'
USER = 'uu4wkwbd3kkfo3zewu8technn74b5x'
EMAIL = 'te9cu2o2m7@pomail.net'

# Error Message Handler
ERROR_MESSAGE = {
    "token": TOKEN,
    "user": USER,
    "priority": 1,
    "message": "Error - Check PushOver API"
    }


# Common OCR corrections
CORRECTIONS = {
        'O': '0', 'o': '0', 'Q': '0', 'D': '0','m': '0',
        'I': '1', 'l': '1', 'T': '1', 'i': '1', 'L': '1',
        'Z': '2', 'z': '2',
        'S': '5', 's': '5',
        'B': '8',
        'g': '9', 'q': '9'
    }

CAPTURE_LIST = [
    "AEROZUL",
    "AQUARUFF",
    "AQUARUFFLE",
    "TANKIROS",
    "BURRABUN",
    "VERDASTALL",
    "CRABATINE",
    "ECHOVANE",
    "FINFLARE",
    "GALAXOAD",
    "GUARDIONE",
    "GLIMMORE",
    "SPECTRARAFFE",
    "SPIKEGON",
    "GALESPARROW",
    "PRISMALEO",
    "CHARGER",
    "VINEMIN",
    "COSMOSY",
    "GLINTALON",
    "EXPHERACLE",
    "FROSTRITE",
    "DRACOLEAF",
    "VERDRAKE",
    "INFERNOURS",
    "MOLTERROCK",
    "NOXPIKE",
    "AURADRAKE",
    "SHELLIFROS",
    "ARBOREALITH",
    "AURORURS",
    "FLORAWING",
    "GALEACORN",
    "GOLEPHANT",
    "LUMIVIX",
    "MECHADON",
    "RUBYFIRE",
    "STORMBRA",
    "TERRATORTLE",
    
    #"STELLAVIAN"
]


   