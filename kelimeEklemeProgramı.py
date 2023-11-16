import os
import time
def kelimeEkle(english,turkish):
    file.seek(0)
    file.write(english+": "+turkish+"\n")
while True:
    with open("ingilizce kelimeler ve türkçeleri.txt","a",encoding="utf-8")as file:
        os.system('cls')
        print("Uygulamadan çıkmak için q tuşuna basınız...")
        kelimeEnglish=input("Kelimenin İngilizcesi: ")
        if(kelimeEnglish=="q" or kelimeEnglish=="Q"):
            print("Uygulamadan Çıkılıyor....")
            time.sleep(1)
            break
        kelimeTurkish=input("Kelimenin Türkçesi: ")
        kelimeEkle(kelimeEnglish,kelimeTurkish)
