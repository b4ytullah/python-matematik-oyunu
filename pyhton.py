import math
import random
import time

print("MATEMATİK OYUNUNA HOŞ GELDİNİZ")
print("1 - KOLAY")
print("2 - ORTA")
print("3 - ZOR")

zorluk = input("Lütfen oyunun zorluk modunu seçiniz : ")
print("")

puan = 0
sayi1 = 0
sayi2 = 0
sayi3 = 0

if zorluk == "1":
    print("-------------------------KURALLAR----------------------------")
    print("Doğru bilinen soru 1 puan kazandırırken, yanlış bilinen soru 3 puan kaybettirir.")
    print("Puan durumu 5 olunca oyun biter.")
    print("-------------------------------------------------------------")
    puandegeri = 5
elif zorluk == "2":
    puandegeri = 10
    print("-------------------------KURALLAR----------------------------")
    print("Doğru bilinen soru 1 puan kazandırırken, yanlış bilinen soru 3 puan kaybettirir.")
    print("Puan durumu 10 olunca oyun biter.")
    print("-------------------------------------------------------------")
elif zorluk == "3":
    puandegeri = 20
    print("-------------------------KURALLAR----------------------------")
    print("Doğru bilinen soru 1 puan kazandırırken, yanlış bilinen soru 3 puan kaybettirir.")
    print("Puan durumu 20 olunca oyun biter.")
    print("------------------------------------------------------------")

while puan < puandegeri:
    # zorluk seçimi
    if zorluk == "1":
        s1 = random.randint(1, 10)
        s2 = random.randint(1, 10)
        faktsayi = random.randint(1,5)
    elif zorluk == "2":
        s1 = random.randint(1, 50)
        s2 = random.randint(1, 50)
        faktsayi = random.randint(1, 10)
    elif zorluk == "3":
        faktsayi = random.randint(1, 50)
        s1 = random.randint(1, 100)
        s2 = random.randint(1, 100)
    else:
        print("Lütfen geçerli bir zorluk derecesi giriniz..")

    while sayi1 == s1 and sayi2 == s2 or faktsayi == sayi3: #aynı sorularının sorulmaması için
        if zorluk == "1":
            s1 = random.randint(1, 10)
            s2 = random.randint(1, 10)
            faktsayi = random.randint(1,5)
        elif zorluk == "2":
            s1 = random.randint(1, 50)
            s2 = random.randint(1, 50)
            faktsayi = random.randint(1, 10)
        elif zorluk == "3":
            faktsayi = random.randint(1, 50)
            s1 = random.randint(1, 100)
            s2 = random.randint(1, 100)
        else:
            print("Lütfen geçerli bir zorluk derecesi giriniz..")


    print("Puan durumu : ",puan)
    print("")

    islem = random.randint(1,4)

    print("Soru belirleniyor..")
    print("")
    time.sleep(1) #2 saniye delay

    #aynı soruları mı soruyor?
    sayi1 = s1
    sayi2 = s2
    sayi3 = faktsayi

    if islem == 1: #toplama işlemi
        print("--Toplama İşlemi--")
        print("Lütfen",s1,"+",s2,"İşleminin sonucu giriniz")
        sonuc = int(input("Cevap : "))
        snc = s1 + s2
        if snc == sonuc:
            print("Doğru cevap verdiniz. Tebrikler!")
            time.sleep(1)
            puan = puan + 1
        else:
            print("Verdiğiniz cevap yanlışdır. Doğru cevap :",snc)
            time.sleep(1)
            puan = puan - 3

    elif islem == 2: #Çıkarma işlemi
        print("--Çıkarma İşlemi--")
        print("Lütfen",s1,"-",s2,"İşleminin sonucunu giriniz")
        sonuc = int(input("Cevap : "))
        snc = s1 - s2
        if snc == sonuc:
            print("Doğru cevap verdiniz. Tebrikler!")
            time.sleep(1)
            puan = puan + 1
        else:
            print("Verdiğiniz cevap yanlışdır. Doğru cevap :",snc)
            time.sleep(1)
            puan = puan - 3

    elif islem == 3: #çarpma işlemi
        print("--Çarpma İşlemi--")
        print("Lütfen",s1,"x",s2,"İşleminin sonucu giriniz")
        sonuc = int(input("Cevap : "))
        snc = s1 * s2
        if snc == sonuc:
            print("Doğru cevap verdiniz. Tebrikler!")
            time.sleep(1)
            puan = puan + 1
        else:
            print("Verdiğiniz cevap yanlışdır. Doğru cevap :",snc)
            time.sleep(1)
            puan = puan - 3

    elif islem == 4: #faktöriyel
        print("--Faktöriyel İşlemi--")
        print("Lütfen",faktsayi,"!","İşleminin sonucunu giriniz")
        sonuc = int(input("Cevap : "))
        snc = math.factorial(faktsayi)
        if snc == sonuc:
            print("Doğru cevap verdiniz. Tebrikler!")
            time.sleep(1)
            puan = puan + 1
        else:
            print("Verdiğiniz cevap yanlışdır. Doğru cevap :",snc)
            time.sleep(1)
            puan = puan - 3

if puandegeri == 5:
    print("5 puan yaparak oyunu bitirdiniz. TEBRİKLER")
elif puandegeri == 10:
    print("10 puan yaparak oyunu bitirdiniz. TEBRİKLER")
else:
    print("20 puan yaparak oyunu bitirdiniz. TEBRİKLER")