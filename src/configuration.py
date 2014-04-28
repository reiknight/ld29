# -*- coding: utf-8 -*-
import os

from constants import *

class Configuration():
    def __init__(self):
        self.music_enabled = True
        self.state = MENU_STATE

def save_score(score):
    with open("save/save.sav", "w") as f:
        f.write(str(score))
    
def load_score():
    if os.path.exists("save/save.sav"):
        with open("save/save.sav", "r") as f:
            return int(f.readline())
            
def has_saved_game():
   return os.path.exists("save/save.sav")