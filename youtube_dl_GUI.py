from tkinter import *
from tkinter import filedialog
from os import *


def changedir():
    folder.set(filedialog.askdirectory())
    if(len(folder.get()) != 0):
        curdir.config(text="Current directory : " + folder.get())
    else:
        curdir.config(text="Current directory : " + getcwd())


def convert():
    if(flag.get()):
        if(len(folder.get()) == 0):
            if(rename.get()):
                """print("MP4 Same dir diff name")"""
                system("youtube-dl -f mp4 -o \"" +
                       name.get() + ".mp4\" " + url.get())
            else:
                """print("MP4 Same dir same name")"""
                system("youtube-dl -f mp4 -o \"%(title)s.%(ext)s\" " + url.get())
        else:
            if(rename.get()):
                """print("MP4 Diff dir diff name")"""
                system("youtube-dl -f mp4 -o \"" + folder.get() +
                       "/" + name.get() + ".mp4\" " + url.get())
            else:
                """print("MP4 Diff dir same name")"""
                system("youtube-dl -f mp4 -o \"" + folder.get() +
                       "/%(title)s.%(ext)s\" " + url.get())
    else:
        if(len(folder.get()) == 0):
            if(rename.get()):
                """print("MP3 Same dir diff name")"""
                system("youtube-dl -o \"" + name.get() +
                       ".mp3\" --extract-audio --audio-format mp3 " + url.get())
            else:
                """print("MP3 Same dir same name")"""
                system(
                    "youtube-dl -o \"%(title)s.%(ext)s\" --extract-audio --audio-format mp3 " + url.get())
        else:
            if(rename.get()):
                """print("MP3 Diff dir diff name")"""
                system("youtube-dl -o \"" + folder.get() + "/" + name.get() +
                       ".mp3\" --extract-audio --audio-format mp3 " + url.get())
            else:
                """print("MP3 Diff dir same name")"""
                system("youtube-dl -o \"" + folder.get() +
                       "/%(title)s.%(ext)s\" --extract-audio --audio-format mp3 " + url.get())
    url.delete(0, END)
    url.insert(0, "")
    name.delete(0, END)
    name.insert(0, "")


gui = Tk(className="Convert Youtube video to mp3 or mp4")
gui.geometry("600x200")

flag = BooleanVar()
rename = BooleanVar()
folder = StringVar()

Label(gui, font=("Ariel", 10), text="Select mp3/mp4 : ").place(x=5, y=7)
Radiobutton(gui, text="MP3", variable=flag, value='False',
            indicatoron=0, height=1, width=10, command=lambda: f.config(text=".mp3")).place(x=125, y=5)
Radiobutton(gui, text="MP4", variable=flag, value='True',
            indicatoron=0, height=1, width=10, command=lambda: f.config(text=".mp4")).place(x=225, y=5)

Label(gui, text="URL : ").place(x=5, y=40)
url = Entry(gui, width=75)
url.place(x=50, y=40)

Checkbutton(gui, text="Specify a name for your file", variable=rename,
            onvalue='True', offvalue='False', height=1, width=50).place(x=-100, y=60)
Label(gui, text="Name of the file : ").place(x=5, y=90)
name = Entry(gui, width=50)
name.place(x=110, y=90)
f = Label(gui, text=".mp3", width=5, height=1)
f.place(x=410, y=90)

curdir = Label(gui, text="Current directory : " + getcwd())
curdir.place(x=5, y=120)

chdir = Button(gui, text="Change Directory", width=20,
               height=1, command=changedir).place(x=425, y=115)

conv = Button(gui, text="Convert", width=10, height=1,
              command=convert).place(x=250, y=150)

gui.mainloop()
