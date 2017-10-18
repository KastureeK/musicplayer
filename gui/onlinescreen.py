from Tkinter import *
from Controls import onlinecontrol
from Tkinter import PhotoImage
from PIL import ImageTk
from PIL import Image

class onlinescreen:
    def makescreen(self,master,ob):
        self.framei = Frame(master)
        master.geometry("480x260")
        self.framei["bg"] = "navy blue"
        self.framei.pack()

        global artist, songname, album, genre

        artist = StringVar()
        songname = StringVar()
        album = StringVar()
        genre = StringVar()

        self.listi = onlinecontrol.getmeta()
        indextmp =  onlinecontrol.getindex()

        onlinecontrol.getlist()

        self.artistlabel = Label(self.framei, textvar=artist, anchor="center", font=("Helvetica", 14), bg="navy blue", fg="white")
        self.genrelabel = Label(self.framei, textvar=genre, anchor="center", font=("Helvetica", 14), bg="navy blue", fg="white")
        self.albumlabel = Label(self.framei, textvar=album, anchor="center", font=("Helvetica", 14), bg="navy blue", fg="white")
        self.Songnamelabel = Label(self.framei, textvar=songname, anchor="center", font=("Helvetica", 16, "bold"),bg="navy blue", fg="white")

        add_fileicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/addsong.gif")
        add_directoryicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/adddir.gif")
        playicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/play.gif")
        pauseicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/pause.gif")
        stopicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/stop.gif")
        resumeicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/resume.gif")
        previousicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/previous.gif")
        nexticon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/next.gif")
        shuffleicon = ImageTk.PhotoImage(file="C:/Users/Harshit Soni/Desktop/python/music/icons/shuffle.gif")

        self.button1 = Button(self.framei, text="Play", command=lambda: onlinecontrol.play(ob))
        self.button2 = Button(self.framei, text="Pause", command=onlinecontrol.pause)
        self.button3 = Button(self.framei, text="Stop", command=onlinecontrol.stop)
        self.button4 = Button(self.framei, text="Resume", command=onlinecontrol.resume)
        self.button5 = Button(self.framei, text="Next", command=onlinecontrol.nextsong)
        self.button6 = Button(self.framei, text="Previous", padx=20, pady=20, command=onlinecontrol.previous)
        # self.button7 = Button(self.framei, text="Browse", command=onlinecontrol.getlist)
        self.button8 = Button(self.framei, text="Shuffle & Play", command=onlinecontrol.shuffleandplay)
        # self.button9 = Button(self.framei, text="Play Selected Song", command=onlinecontrol.playselected)

        #self.button9.config(image=add_fileicon)
        #self.button7.config(image=add_directoryicon)
        self.button1.config(image=playicon)
        self.button2.config(image=pauseicon)
        self.button3.config(image=stopicon)
        self.button4.config(image=resumeicon)
        self.button6.config(image=previousicon)
        self.button5.config(image=nexticon)
        self.button8.config(image=shuffleicon)

        #self.button9.image = add_fileicon
        #self.button7.image = add_directoryicon
        self.button1.image = playicon
        self.button2.image = pauseicon
        self.button3.image = stopicon
        self.button4.image = resumeicon
        self.button6.image = previousicon
        self.button5.image = nexticon
        self.button8.image = shuffleicon

        self.button1.grid(row=1, column=1)
        self.button2.grid(row=1, column=4)
        self.button3.grid(row=2, column=2)
        self.button4.grid(row=1, column=3)
        self.button5.grid(row=1, column=5)
        self.button6.grid(row=1, column=2)
        #self.button7.grid(row=2, column=3)
        self.button8.grid(row=2, column=4)
        #self.button9.grid(row=2, column=5)

        self.artistlabel.grid(row=5, columnspan = 6)
        self.genrelabel.grid(row=6, columnspan = 6)
        self.albumlabel.grid(row=7, columnspan = 6)
        self.Songnamelabel.grid(row=0, columnspan = 6)


    def updateval(self,index):
        self.setval(index)

    def setval(self,indextmp):
        global artist, songname, album, genre
        artist.set("Artist:" + self.listi[indextmp][1])
        album.set("Album:" + self.listi[indextmp][3])
        genre.set("Genre" + self.listi[indextmp][2])
        songname.set("Song Name:" + self.listi[indextmp][0])

if __name__=="__main__":    
    root = Tk()
    root.title("MUSIC RECOMMENDATION SYSTEM")
    
    #make_label(framei, img)
    root.iconbitmap(default="C:/Users/Harshit Soni/Desktop/python/music/icons/music.ico")
    root.geometry("380x280")
    root.configure(background="powder blue")
    ob = onlinescreen()
    ob.makescreen(root)
    root.mainloop()
