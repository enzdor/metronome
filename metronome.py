import tkinter as tk
import time
import pygame

root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1, relheight=1)

playing = 1

def playmetronome():
    pygame.mixer.init()
    newLabel = tk.Label(frame, text=speed.get())
    newLabel.pack()
    newLabel2 = tk.Label(frame, text=time.ctime())
    newLabel2.pack()
    bpm =  (60 / int(speed.get())) - 0.002
    print(bpm)
    while playing > 0:
        pygame.mixer.Sound('./sounds/Tic.mp3').play()
        time.sleep(bpm)
    print('done')


play = tk.Button(frame, text='play', command=playmetronome)
play.pack()

speed = tk.Entry(frame)
speed.pack()

root.mainloop()