from tkinter import *
from tkinter import filedialog
import os
import json
import eyed3


def mp3_mode():
    f.config(text=".mp3")
    artist.config(state='normal')
    album.config(state='normal')
    meta_check.config(state=NORMAL)
    meta_check2.config(state=NORMAL)


def mp4_mode():
    f.config(text=".mp4")
    artist.config(state='disabled')
    album.config(state='disabled')
    meta_check.config(state=DISABLED)
    meta_check2.config(state=DISABLED)


def changedir():
    folder.set(filedialog.askdirectory())
    if(len(folder.get()) != 0):
        curdir.config(text="Current directory : " + folder.get())
    else:
        curdir.config(text="Current directory : " + os.getcwd())


def convert():
    if(flag.get()):
        if(len(folder.get()) == 0):
            if(rename.get()):
                # print("MP4 Same dir diff name")
                os.system("youtube-dl -f mp4 -o \"" +
                          name.get() + ".mp4\" " + url.get())
            else:
                # print("MP4 Same dir same name")
                os.system(
                    "youtube-dl -f mp4 -o \"%(title)s.%(ext)s\" " + url.get())
        else:
            if(rename.get()):
                # print("MP4 Diff dir diff name")
                os.system("youtube-dl -f mp4 -o \"" + folder.get() +
                          "/" + name.get() + ".mp4\" " + url.get())
            else:
                # print("MP4 Diff dir same name")
                os.system("youtube-dl -f mp4 -o \"" + folder.get() +
                          "/%(title)s.%(ext)s\" " + url.get())
    else:
        if(mdoff.get()):
            os.system("youtube-dl --write-info-json --skip-download " + url.get())
            os.system("ren *.json metadata.json")
            with open("metadata.json") as json_file:
                md = json.load(json_file)
            if(md["uploader"][-8:] == " - Topic"):
                def_artist = md["uploader"][:-8]
            else:
                def_artist = md["uploader"]
            def_album = md["album"]
            fn = md["title"]

        if(len(folder.get()) == 0):
            if(rename.get()):
                # print("MP3 Same dir diff name")
                os.system("youtube-dl -o \"" + name.get() +
                          ".mp3\" --extract-audio --audio-format mp3 " + url.get())
                if(mdoff.get()):
                    audiofile = eyed3.load(
                        os.getcwd() + "\\" + name.get() + ".mp3")
                    if(edit_metadata.get()):
                        audiofile.tag.artist = artist.get()
                        audiofile.tag.album = album.get()
                    else:
                        audiofile.tag.artist = def_artist
                        audiofile.tag.album = def_album
                    audiofile.tag.save()
            else:
                # print("MP3 Same dir same name")
                os.system(
                    "youtube-dl -o \"%(title)s.%(ext)s\" --extract-audio --audio-format mp3 " + url.get())
                if(mdoff.get()):
                    audiofile = eyed3.load(os.getcwd() + "\\" + fn + ".mp3")
                    if(edit_metadata.get()):
                        audiofile.tag.artist = artist.get()
                        audiofile.tag.album = album.get()
                    else:
                        audiofile.tag.artist = def_artist
                        audiofile.tag.album = def_album
                    audiofile.tag.save()
        else:
            if(rename.get()):
                # print("MP3 Diff dir diff name")
                os.system("youtube-dl -o \"" + folder.get() + "/" + name.get() +
                          ".mp3\" --extract-audio --audio-format mp3 " + url.get())
                if(mdoff.get()):
                    audiofile = eyed3.load(
                        folder.get() + "\\" + name.get() + ".mp3")
                    if(edit_metadata.get()):
                        audiofile.tag.artist = artist.get()
                        audiofile.tag.album = album.get()
                    else:
                        audiofile.tag.artist = def_artist
                        audiofile.tag.album = def_album
                    audiofile.tag.save()
            else:
                # print("MP3 Diff dir same name")
                os.system("youtube-dl -o \"" + folder.get() +
                          "/%(title)s.%(ext)s\" --extract-audio --audio-format mp3 " + url.get())
                if(mdoff.get()):
                    audiofile = eyed3.load(folder.get() + "\\" + fn + ".mp3")
                    if(edit_metadata.get()):
                        audiofile.tag.artist = artist.get()
                        audiofile.tag.album = album.get()
                    else:
                        audiofile.tag.artist = def_artist
                        audiofile.tag.album = def_album
                    audiofile.tag.save()

        os.system("del /f metadata.json")
    url.delete(0, END)
    url.insert(0, "")
    name.delete(0, END)
    name.insert(0, "")


gui = Tk(className="Convert Youtube video to mp3 or mp4")
gui.geometry("600x300")

flag = BooleanVar()
rename = BooleanVar()
folder = StringVar()
edit_metadata = BooleanVar()
mdoff = BooleanVar()

Label(gui, font=("Ariel", 10), text="Select mp3/mp4 : ").place(x=5, y=7)
Radiobutton(gui, text="MP3", variable=flag, value='False',
            indicatoron=0, height=1, width=10, command=mp3_mode).place(x=125, y=5)
Radiobutton(gui, text="MP4", variable=flag, value='True',
            indicatoron=0, height=1, width=10, command=mp4_mode).place(x=225, y=5)

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

curdir = Label(gui, text="Current directory : " + os.getcwd())
curdir.place(x=5, y=120)

chdir = Button(gui, text="Change Directory", width=20,
               height=1, command=changedir).place(x=425, y=115)

conv = Button(gui, text="Convert", width=10, height=1,
              command=convert).place(x=250, y=150)

meta_check = Checkbutton(gui, text="Specify your own metadata for the *.mp3 file", variable=edit_metadata,
                         onvalue='True', offvalue='False', height=1, width=50)
meta_check.place(x=-50, y=180)
meta_check2 = Checkbutton(gui, text="Write metadata to this song", variable=mdoff,
                          onvalue='True', offvalue='False', height=1, width=50)
meta_check2.place(x=250, y=180)

Label(gui, text="Artist : ").place(x=5, y=210)
artist = Entry(gui, width=50)
artist.place(x=50, y=210)
Label(gui, text="Album : ").place(x=5, y=240)
album = Entry(gui, width=50)
album.place(x=60, y=240)

gui.mainloop()
