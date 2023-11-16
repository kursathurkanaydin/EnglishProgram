import os 
import time
import random
i=1
wordsEnglish2=list()
wordsTurkish2=list()
with open("ingilizce kelimeler ve türkçeleri2.txt","r+",encoding="utf-8") as file:
    wordsEnglish=file.readlines()
    for word in wordsEnglish:
        word=word.lower()
        word=word.replace("\n","")
        wordsEnglish2.append(word)
with open("türkçe.txt","r+",encoding="utf-8") as dosya:
    wordsTurkish=dosya.readlines()
    for kelime in wordsTurkish:
        kelime=kelime.lower()
        kelime=kelime.replace("\n","")
        kelime=kelime.split(", ")
        wordsTurkish2.append(kelime[0])
print(
    """***İngilizce kelime bilgisi test etme programına hoş geldiniz***
        Programdan Çıkmak için q tuşunu giriniz
        Cevabı Görmek için c tuşunu giriniz
        Kelimeler önünüze rastgele olarak gelecektir doğru cevabı kelimelerin karşısına yazınız.
                                            ***BAŞARILAR***
    """)
while(i<2):
    random_sayi = random.randint(0, len(wordsEnglish2)-1)
    def bitir():
        global i
        i=2
    while True:
        #print(wordsEnglish[random_sayi])
        #print(wordsTurkish[random_sayi])
        cevap=str(input(f"{wordsEnglish2[random_sayi]}: "))
        cevap=cevap.lower()

        if(cevap==wordsTurkish2[random_sayi]):
            print("Doğru")
            time.sleep(0.25)
            break
        elif(cevap=="q"):
            bitir()
            break
        elif(cevap=="c"):
            print(f"cevap: {wordsTurkish2[random_sayi]}")
            time.sleep(0.25)
            break
        else:
            print("Yanlış.Tekrar deneyiniz: ")
print("Program sonlanıyor...")
time.sleep(1)