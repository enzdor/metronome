import tkinter as tk
from playsound import playsound
import time

root = tk.Tk()
canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

def playmetronome():
    newLabel = tk.Label(frame, text=speed.get())
    newLabel.pack()
    newLabel2 = tk.Label(frame, text=time.ctime())
    newLabel2.pack()
    total_seconds = int(speed.get())
    while total_seconds > 0:
        print(total_seconds)
        time.sleep(1)
        total_seconds -= 1
    print('done')


play = tk.Button(frame, text='play', bg='green', command=playmetronome)
play.pack()

speed = tk.Entry(frame, bg='red')
speed.pack()

root.mainloop()