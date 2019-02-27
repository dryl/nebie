def hello():
    print('соси хуй')
    
from tkinter import *
tk = Tk()
btn = Button(tk, text="нажми меня",command=hello)
btn.pack()

