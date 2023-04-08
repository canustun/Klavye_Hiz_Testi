#product by canustun
from random import choice,randint
from tkinter import *

kelimeler=["beyhude","müteşekkir","canhıraş","armağan","bakım","haya","yıl","iç","yüz","iki","insan","hayat","atmak","küçük","zorluk","okul","yemek","tat","bebek","iktidar","devlet","kral","reis","hoca","destan","bülbül","gül","demir","sağlam","polat","can","furkan","ahmet","öğrenci","telefon","kutu","kalp","zaman","namaz","ürün","doğru","tutma","için","birlikte","söylemek","veya","konya","napıyosun","marya","fare","kedicik","klavyeci","simitci","yunus","balık","sigara","ateş","yanık","baloncuk","patlatmak","ısırmak","kaleci","gol","basket","kırıldı","üzüldü","muslera","bayıldı","yığıldı","uzanmak","yatmak","uyumak","yurt","felsefe","ortam","toplum","birlik","nato","asya","ingilizce"]
renk=["green","silver","gold","brown","pink","black","orange","white","red","blue","yellow"]

def kelime_gönder():
    return kelimeler.pop(randint(0,len(kelimeler)-1))

skorlistesi=open("skor_listesi.txt","a+")
harf_deposu,puan,süre=kelime_gönder(),0,15

pencere=Tk()
pencere.title("Klavye Hız Test Oyunu")
pencere.geometry("400x400")
def rekor():
    skorlistesi.seek(0)
    rekor_puan['text']="En Sonuncu Rekor Puan : "+skorlistesi.read()

def yenile_komutları():
    global puan,süre,harf_deposu,kelimeler
    süre,puan=60,0
    rekor()
    kelimeler=["beyhude","müteşekkir","canhıraş","armağan","bakım","haya","yıl","iç","yüz","iki","insan","hayat","atmak","küçük","zorluk","okul","yemek","tat","bebek","iktidar","devlet","kral","reis","hoca","destan","bülbül","gül","demir","sağlam","polat","can","furkan","ahmet","öğrenci","telefon","kutu","kalp","zaman","namaz","ürün","doğru","tutma","için","birlikte","söylemek","veya","konya","napıyosun","marya","fare","kedicik","klavyeci","simitci","yunus","balık","sigara","ateş","yanık","baloncuk","patlatmak","ısırmak","kaleci","gol","basket","kırıldı","üzüldü","muslera","bayıldı","yığıldı","uzanmak","yatmak","uyumak","yurt","felsefe","ortam","toplum","birlik","nato","asya","ingilizce"]
    harf_deposu=kelime_gönder()
    kelime['text']="Kelime : "+harf_deposu
    kelimeyaz.delete(0,'end')
    süre_göster['text']="Kalan Süre : "+str(süre)
    puan_goster['text']="Puan : "+str(puan)
    
def azalış():
    global süre,puan
    if süre<=0:
        skorlistesi.seek(0)
        deneme=str(skorlistesi.readlines())[2:-2]
        
        if puan>int(deneme):
            with open("skor_listesi.txt","w+") as skor2:
                skor2.write(str(puan))
            rekor()
        puan=0
        puan_goster['text']="Puan : 0"
        süre_göster['text']="Süre Bitti !"
    else:
        süre-=1
        süre_göster['text']="Kalan Süre : "+str(süre)
    pencere.after(1000,azalış)
    
def kelime_üretici():
 global harf_deposu,süre,puan
 
 if süre>0 and kelimeyaz.get()==harf_deposu:
    harf_deposu=""
    puan+=1
    süre+=1
    puan_goster['text']="Puan : "+str(puan)
    harf_deposu=kelime_gönder()
    kelime['text']="Kelime : "+harf_deposu
    kelimeyaz.delete(0,'end')
         
 pencere.after(80,kelime_üretici)



Label(text="Product By CanÜstün",bg="orange",width=20).pack()

süre_göster=Label(text="Kalan Süre : "+str(süre))
süre_göster.pack()

yenile_tuşu=Button(text="⟳ Yenile ⟳",bg="gray",fg="white")
yenile_tuşu.config(command = yenile_komutları)
yenile_tuşu.pack()

kelime=Label(text="Kelime : "+harf_deposu,bg="pink")
kelime.pack(pady=10)

puan_goster=Label(text="Puan : "+str(puan))
puan_goster.pack()

kelimeyaz=Entry()
kelimeyaz.pack()

rekor_puan=Label(text="En Sonuncu Rekor Puan : "+skorlistesi.read())
rekor_puan.pack()

çıkış=Button(text="Çıkış",bg="red")
çıkış.config(command = exit)
çıkış.pack(pady=20)

kelime_üretici()
pencere.after(1000,azalış)
pencere.mainloop()

skorlistesi.close()
