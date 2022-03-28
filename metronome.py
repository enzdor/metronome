import time
import pygame

bpm_input = input('BPM:')

def playmetronome():
    pygame.mixer.init()
    bpm =  ((60 / int(bpm_input)) - 0.002)
    alive = True
    while alive == True:
        pygame.mixer.Sound('./sounds/Tic.mp3').play()
        time.sleep(bpm)

playmetronome()

