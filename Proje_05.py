from sqlite3 import *
from tkinter import *
import time
import datetime
arayuz=Tk()
arayuz.title("Mesajlar.db")

with connect("Mesajlar.db") as veritabanim:
    veri = veritabanim.cursor()
    veri.execute("""CREATE TABLE IF NOT EXISTS GelenKutusu (idNo INTEGER PRIMARY KEY AUTOINCREMENT,
    Gönderen TEXT,Numara INT, Mesaj TEXT,Tarih TEXT)""")

def tablo():
    vakit = time.time()
    tarih = str(datetime.datetime.fromtimestamp(vakit).strftime(" %Y/%m/%d Tarihinde %H.%M.%S Saatinde mesaj Oluşturuldu.."))
    def sillme():
        kayit.destroy()
        kayitSil.destroy()
    isimm = " Gönderici: "+isimal.get()
    veri.execute("INSERT INTO  GelenKutusu(Gönderen,Numara,Mesaj,Tarih) VALUES(?,?,?,?)", (isimm, noal.get(), mesajal.get(),tarih))
    veritabanim.commit()
    kayit=Label(text="Verileriniz \n Kaydedilmiştir",font="Times 22 bold",fg="purple")
    kayit.grid(row=3,column=1)

    kayitSil=Button(text="Yazıyı Sil",command=sillme,font="Times 17 bold",bg="deeppink",fg="black")
    kayitSil.grid(row=4, column=1)
    isimal.delete(0, END)
    noal.delete(0, END)
    mesajal.delete(0, END)
def oku():
    listele.delete(0,END)
    veri.execute("SELECT * from GelenKutusu")
    for x in veri.fetchall():
        listele.insert(0, str(x[0]) + x[1] + x[2] + x[3] + x[4])
def listebos():
    listele.delete(0,END)

def guncel():
    veri.execute("UPDATE GelenKutusu SET Gönderen=?, Numara=? WHERE idNo=?",(gunGir.get(),Gungir1.get(),gunGir2.get()))
    veritabanim.commit()
    for x in veri.fetchall():
        listele.insert(0,str(x[0])+x[1]+x[2]+x[3]+x[4])
def ara():
    listele.delete(0,END)
    veri.execute("SELECT * FROM GelenKutusu WHERE idNo=?",(araGir.get(),))
    for x in veri.fetchall():
        listele.insert(0,str(x[0])+x[1]+x[2]+x[3]+x[4])
def isimara():
    listele.delete(0, END)
    veri.execute("select * from GelenKutusu where Gönderen LIKE ?", ('%' + isimBul.get() + '%',))
    for x in veri.fetchall():
        listele.insert(0, str(x[0]) +" "+ x[1] +" "+ x[2] +" "+ x[3] +" "+ x[4])
def veriSil():
    listele.delete(0, END)
    veri.execute("DELETE FROM GelenKutusu WHERE idNo =? ",(silGir.get(),))

    veritabanim.commit()

gunEti= Label(text="İsim ve Numara Giriniz Ardından ID Numarasını Giriniz",font="Times 17 bold")
gunEti.grid(row=3,column= 2)

gunGir= Entry(font="Times 13 bold")

gunGir.grid(row=4,column= 2)
Gungir1 =Entry(font="Times 13 bold")
Gungir1.grid(row=5,column= 2)

gunGir2 =Entry(font="Times 13 bold")

gunGir2.grid(row=6,column= 2)
gunbut= Button(text="Güncelle",command=guncel,font="Times 17 bold",bg="deeppink",fg="black")
gunbut.grid(row=7,column= 2)

isim_ara=Label(text="Aramak İstediğniz İsmi Giriniz",font="Times 17 bold")
isim_ara.grid(row=8,column=2)
isimBul=Entry(font="Times 13 bold",width=30)
isimBul.grid(row=9,column=2)
isimDug=Button(text="Veriyi Ara",command=isimara,font="Times 17 bold",bg="deeppink",fg="black")
isimDug.grid(row=10, column=2)

araEti=Label(text="Aramak İstediğniz ID Numarasını Giriniz",font="Times 17 bold")
araEti.grid(row=8,column=0)
araGir=Entry(font="Times 13 bold",width=30)
araGir.grid(row=9,column=0)
araBut= Button(text="Veriyi Ara",command=ara,font="Times 17 bold",bg="deeppink",fg="black")
araBut.grid(row=10,column=0)

silEti= Label(text="Silmek İstediğniz ID Numarasını Giriniz",font="Times 17 bold")
silEti.grid(row=0,column= 2)
silGir=Entry(font="Times 13 bold",width=40)
silGir.grid(row=1,column= 2)
silDug= Button(text="Veriyi Sil",command=veriSil,font="Times 17 bold",bg="deeppink",fg="black")
silDug.grid(row=2,column= 2)


isimSor = Label(text="Alttaki Kutucuğa İsim Giriniz",font="Times 17 bold")
isimSor.grid(row=0,column=0)

isimal= Entry(font="Times 13 bold")
isimal.grid(row=1,column=0)

noSor = Label(text="Alttaki Kutucuğa Numaranızı Giriniz",font="Times 17 bold")
noSor.grid(row=2,column=0)
noal= Entry(font="Times 13 bold")
noal.grid(row=3,column=0)

mesajSor = Label(text="Alttaki Kutucuğa Mesajınızı Giriniz",font="Times 17 bold")
mesajSor.grid(row=4,column=0)
mesajal= Entry(font="Times 13 bold",width=40)
mesajal.grid(row=5,column=0)
bas = Button(text="Mesajı Ekle",command=tablo,font="Times 17 bold",bg="deeppink",fg="black")

bas.grid(row=6,column=0)
yazzz= Label(text=" ",font="Times 17 bold")
yazzz.grid(row=3, column=1)
listele=Listbox(font="Times 13 bold",width=60)
listele.grid(row=12, column=2)


buton=Button(text="listele",command=oku,font="Times 17 bold",bg="deeppink",fg="black")
buton.grid(row=13, column=2)
silme= Button(text="Liste İçindekileri Sil",command=listebos,font="Times 17 bold",bg="deeppink",fg="black")
silme.grid(row=14, column=2)
mainloop()
