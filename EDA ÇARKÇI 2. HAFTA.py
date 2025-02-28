

from requests import get
from pprint import pprint

link = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=5b849e51c956479db38368cb3f8114c0"

donut = get(url=link)
veri_seti = donut.json()
pprint(veri_seti)

""" Wall Street dergisinin son 6 ayındaki basımlarındaki yayınlarının olduğu bir veri seti formatı indirildi."""

"""
    ÖDEVİN DETAYLARI:

-Fonksiyonlarla CRUD işlemleri yapılacak.
-Bu fonksiyonlar main fonksiyonu adı altında toplanacaktır.

"""


def karsilama():  # Kullanıcı karşılayan ve kısa açıklama yapan bir giriş tasarlandı.

    print("Hoşgeldiniz!\nBurada Wall Street dergisinin son altı ayına erişim sağlayabileceksiniz.")
    print(
        "Aşağıda belirtilen işlemleri yapabilirsiniz:\n1.Tam tarihe göre arama\n2.Basım ayına göre arama\n3.Yazara göre arama\n4.Basım url'sine erişim\n5.Çıkış")


def tarih_girdi(veriseti, tarih):
    for element in veriseti["articles"]:
        if tarih in element['publishedAt']:
            print(f"İstediğiniz makalenin yazarı: {element['author']}\n Makalenin içeriği: {element['content']}")
            return
    print("Yazılan girişte herhangi bir basım bulunmamaktadır.")


def ay_girdi(veriseti, ay):
    for element in veriseti["articles"]:
        if ay in element['publishedAt']:
            print(f"İstediğiniz makalenin yazarı: {element['author']}\n Makalenin içeriği: {element['content']}")
            return
    print("Yazılan girişte herhangi bir basım bulunmamaktadır.")


def yazar_girdi(veriseti, yazar):
    for element in veriseti["articles"]:
        if yazar in element['author']:
            print(f"İstediğiniz makale: {element['title']}\n Makalenin basım tarihi:{element['publishedAt']}")
            return
    print("İlgili yazara ait basım bulunamadı.")


def url_alma(veriseti):
    makale = input("İstenilen makalenin başlığını giriniz:")
    for element in veriseti["articles"]:
        if makale in element["title"]:
            print(element["url"])
            return
    print("Aradığınız makale bulunamadı.")


def kullanici_islemi(islem):
    if islem == "1":
        tarih = input("yıl-ay-gün formatı ile istediğiniz tarihi giriniz:")
        tarih_girdi(veri_seti, tarih)
    elif islem == "2":
        ay = input("İstediğiniz ayı giriniz:")
        ay_girdi(veri_seti, ay)
    elif islem == "3":
        yazar = input("İstediğiniz yazarı giriniz:")
        yazar_girdi(veri_seti, yazar)
    else:
        url_alma(veri_seti)


def main():
    karsilama()
    islem = input("Lütfen istediğiniz işlemi giriniz:")
    if islem == "5":
        print("İyi günler dileriz.Çıkış yapılıyor...")

    elif islem == "1" or islem == "2" or islem == "3" or islem == "4":
        while islem in ["1", "2", "3", "4"]:
            kullanici_islemi(islem)
            islem = input("Lütfen istediğiniz işlemi giriniz:")
            if islem == "5":
                print("İyi günler dileriz.Çıkış yapılıyor...")
    else:
        print("Lütfen geçerli bir işlem giriniz!")


main()
