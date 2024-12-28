import json, numpy as np, sounddevice as sd
from icecream import ic

with open('sound.json') as f:
    sounds = json.load(f)

ic(len(sounds))

def CreateSound(n: int):
    sound = sounds[n-1]
    sample = 44100              # Standard audio sample rate
    ic(sound['frq'], sound['effect'])
    ic(f"{sound['duration']*60} mins")
    t = np.linspace(0, sound['duration'], int(sample * sound["duration"]), endpoint=False)

    if sound['rightEar']>0:
        right = 0.5*np.sin(2*np.pi*sound['rightEar']*t)
        left = 0.5*np.sin(2*np.pi*sound['leftEar']*t)
    else:
        left = right = 0.5*np.sin(2*np.pi*sound['leftEar']*t)
    
    steroOut = np.column_stack((left, right))

    sd.play(steroOut, sample, blocking=True)
    sd.wait()

def Menu():
    ic("\nAvailable Frequencies and Their Effects:")
    for i, sound in enumerate(sounds, start=1):
        print(f"{i}. {sound['frq']} - Effect: {sound['effect']}")

Menu()
while (s:=input("Enter (1\\2\\3\\4\\5\\6\\7\\8\\9\\10\\ 'n' ): ")) != 'n':
    if int(s) in list(range(1, 11)):
        CreateSound(int(s))
    elif s.lower() == 'n':
        break
    else:
        ic("Enter valid number")
    Menu()