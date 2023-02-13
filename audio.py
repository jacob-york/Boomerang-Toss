# this will be expanded upon to include background music & ambience, multiple sounds played at once, etc.

import winsound
import random


def play(sound):
    winsound.PlaySound(sound, winsound.SND_ASYNC)


menu_sound = "sound_files\\kenny\\menu_sound.wav"
settings_move = "sound_files\\kenny\\settings_move.wav"
select = "sound_files\\kenny\\select.wav"
negative = "sound_files\\kenny\\negative.wav"
reset = "sound_files\\kenny\\click2.wav"

# Random note from a C maj chord. Sounds from my acoustic guitar
hit_sound = f"sound_files\\guitar\\guitarCMaj{random.randint(1, 4)}.wav"

'''
def menu_sound():
    winsound.PlaySound(f"sound_files\\kenny\\switch0{random.randint(1, 3)}.wav", winsound.SND_ASYNC)

def hitsound():  # Random note from a C maj chord. Sounds from my acoustic guitar.
    winsound.PlaySound(f"sound_files\\guitar\\guitarCMaj{random.randint(1, 4)}.wav", winsound.SND_ASYNC)
'''
