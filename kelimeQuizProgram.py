import os 
import time
import random
i=1
words=list()
wordsEnglish=list()
wordsTurkish=list()
dosya=open("ingilizce kelimeler ve türkçeleri.txt","r+",encoding="utf-8")
words=dosya.readlines()
for word in words:
    word=word.lower()
    word=word.replace("\n","")
    word=word.split(": ")
    wordsEnglish.append(word[0])
    wordsTurkish.append(word[1])
print(
    """***İngilizce kelime bilgisi test etme programına hoş geldiniz***
        Programdan Çıkmak için q tuşunu giriniz
        Cevabı Görmek için c tuşunu giriniz
        Kelimeler önünüze rastgele olarak gelecektir doğru cevabı kelimelerin karşısına yazınız.
                                            ***BAŞARILAR***
    """)
while(i<2):
    random_sayi = random.randint(0, len(wordsEnglish)-1)
    def bitir():
        global i
        i=2
        
        
   
    while True:
        #print(wordsEnglish[random_sayi])
        #print(wordsTurkish[random_sayi])
        cevap=str(input(f"{wordsEnglish[random_sayi]}: "))
        cevap=cevap.lower()

        if(cevap==wordsTurkish[random_sayi]):
            print("Doğru")
            time.sleep(0.25)
            break
        elif(cevap=="q"):
            bitir()
            break
        elif(cevap=="c"):
            print(f"cevap: {wordsTurkish[random_sayi]}")
            time.sleep(0.25)
            break
        else:
            print("Yanlış.Tekrar deneyiniz: ")
print("Program sonlanıyor...")
time.sleep(1)