from tkinter import *
from tkinter import filedialog
import os
from selenium import webdriver


def changedir():
    folder.set(filedialog.askdirectory())
    if len(folder.get()) != 0:
        curdir.config(text="Current directory : " + folder.get())
    else:
        curdir.config(text="Current directory : " + os.getcwd())


def down():
    driver = webdriver.Edge()
    driver.get(url.get())
    links = driver.find_elements_by_tag_name("a")
    songs = []
    for link in links:
        if (
            link.get_attribute("class")
            == "yt-simple-endpoint style-scope yt-formatted-string"
        ):
            songs.append(link.get_attribute("href"))
    driver.close()
    print(len(songs[1:]))
    for song in songs[1:]:
        os.system(
            'yt-dlp -o "'
            + folder.get()
            + '/%(title)s.%(ext)s" --extract-audio --audio-format mp3 '
            + song
        )
    url.delete(0, END)
    url.insert(0, "")


gui = Tk(className="Download albums from Youtube Music")
gui.geometry("600x125")

folder = StringVar()

Label(gui, text="URL : ").place(x=5, y=10)
url = Entry(gui, width=75)
url.place(x=50, y=10)
curdir = Label(gui, text="Current directory : " + os.getcwd())
curdir.place(x=5, y=40)
chdir = Button(
    gui, text="Change Directory", width=20, height=1, command=changedir
).place(x=425, y=40)
conv = Button(gui, text="Download", width=10, height=1, command=down).place(x=250, y=75)

gui.mainloop()
