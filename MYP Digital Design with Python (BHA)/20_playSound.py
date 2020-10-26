"""
NAME: Mr. Poirier
DATE: September 2, 2015
PURPOSE: Defines the playSound function
"""

import subprocess

def playSound(soundfile):
    subprocess.call(["afplay", soundfile])


