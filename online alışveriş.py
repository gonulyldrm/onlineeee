print("online alışveriş")

kullaniciadi1="aaa"
sifre1="111"
editor1="bbb"
sifre2="222"

urunlerrr = {"oyuncak araba": "100tl", "elbise": "200tl", "ayakkabı": "1500tl"}

def editorgiris():
    c =input("ediör kullanıcıadı:")
    d =input("sifre:")

    if editor1 == c and sifre2 == d:
        print("editör giriş basarılı")
        islemler()

    else:
        editorgiris()


def islemler():
    k=int(input(""" [1]ekle    [3]guncelle"""))
    if k==3:
        hangisi=input("degerini degiştirmek isteniğin nesne:")
        deger=input("degeri")
        urunlerrr[hangisi]=deger
        print(urunlerrr)

    if k==1:
        key=input("nesne:")
        value=input("degeri:")
        urunlerrr[key]=value
        print(urunlerrr)







def giris():
    a=input("kullanıcı ad:")
    b=input("sifre:")
    if kullaniciadi1 == a and sifre1 == b:
        print("giris basarılı")
        urunler()

    else:
        print("hatalı gırış tekrar deneyın...")
        giris()


def urunler():
    urunbilgi = []
    sepet = []
    a = input("aradıgınız nesne:")

    if a not in urunlerrr.keys():
        print("aradıgınız nesne sitemizde bulunmamaktadır...")
        urunler()

    if a in urunlerrr.keys():
        urunbilgi.append(a)
        print("ürün bilgileri:", urunbilgi)
        b = input("e veya h  (sepette eklensin mi):")
        if b == "e":
            sepet.append(a)
            print("sepet",sepet)
            g = input("e veya h (sepet onaylansınmı)")

            if g == "e":
                t = input("kredi kartı:")
                r= input("sifre:")
                m = input("kart tarihi")
                print("ürün kaydı yapıldı en yakın subeden teslım alabılırsınız")
            else:
                urunler()

#print(editorgiris())
print(giris())