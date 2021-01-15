from pytube import YouTube
import vlc
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog
arayuz=Tk()
arayuz.title("DownTube")
arayuz.geometry("850x500")
duraklat=ImageTk.PhotoImage(Image.open("pause.png"))
def videoDownload():

    messagebox.askquestion("İndirme İşlemi", "Video İndirilsin mi?")

    url = YouTube(linkGir.get())
    video = url.streams.first()
    video.download()
    isim = video.title
    soru2=messagebox.askquestion("Video İndirildi", "İzlemek İster misiniz?")


    if soru2 == "yes":
        media = vlc.MediaPlayer(str(isim)+".mp4")
        def dur():
            media.stop()
        oynat = media.play()



        Button(image=duraklat,command= dur).place(x=375,y=350)
        for i in oynat:
            continue


def VideOynatıcı():


    dosya= filedialog.askopenfilename(initialdir="/", title="Yüklenecek Medya",
                                        filetypes=(("", "*.mp4"),))
    media = vlc.MediaPlayer(dosya)
    oynat = media.play()

    def dur():
        media.stop()

    yaz=Label( text="Duraklat", font="Arial 14 bold", fg="red").place(x=365,y=300)
    dugme=Button(image=duraklat,command=dur).place(x=375,y=350)
    for i in oynat:
        continue




def MuzikDown():

    link=linkGir2.get()
    ytub = YouTube(link)

    parcacik = ytub.streams.filter(only_audio=True).first()

    parcacik.download()
    sor = messagebox.askquestion("Mp3 İndirildi","Dinlemek İster misiniz?")
    isim = parcacik.title
    if sor=="yes":
        oynat =vlc.MediaPlayer(str(isim)+".mp3")
        oynat.play()
        Label(text="Duraklat", font="Arial 14 bold", fg="red").place(x=365, y=300)
        Button(image=duraklat, command= lambda : oynat.stop()).place(x=375, y=350)

def MuzikPlay():
    dosya = filedialog.askopenfilename(initialdir="/", title="Yüklenecek Medya",
                                       filetypes=(("", "*.mp3"),))
    muzik = vlc.MediaPlayer(dosya)
    oynat=muzik.play()





    yaz=Label( text="Duraklat", font="Arial 14 bold", fg="red").place(x=365,y=300)
    dugme=Button(image=duraklat,command=lambda : muzik.stop()).place(x=375,y=350)
    for i in oynat:
        continue


Label(text="Güvenli ve Hızlı Youtube Müzikleri ve Videolar İndir!!!",font="Arial 20 bold").place(x=100,y=60)

Label(text="Youtube Video Linki",font="Arial 14 ", fg="red").place(x=20,y=150)
linkGir=Entry(width=50,font="Times 14",fg="blue")
linkGir.place(x= 210,y=150)
Button(text="İndir",bg="green",font="Times 12 bold",fg="orange",width=10,command=videoDownload).place(x=700,y=145)

Label(text="Youtube Müzik Linki",font="Arial 14 ", fg="red").place(x=20,y=190)
linkGir2=Entry(width=50,font="Times 14",fg="blue").place(x= 210,y=190)
Button(text="İndir",bg="green",font="Times 12 bold",fg="orange",width=10,command=MuzikDown).place(x=700,y=185)

Button(text="Video Oynatma",bg="green",font="Times 12 bold",fg="orange",width=10,command=VideOynatıcı).place(x=400,y=250)
Button(text="Mp3 Oynatma",bg="green",font="Times 12 bold",fg="orange",width=10,command=MuzikPlay).place(x=200,y=250)

mainloop()

