from database import Database
from login import Login
from services.musteri_service import MusteriService
from services.urun_service import UrunService
from services.siparis_service import SiparisService
from services.excel_service import ExcelService

db = Database()
login = Login()

try:
    db.kullanici_ekle(
        "admin",
        login.sifrele("123456")
    )
except:
    pass

if not login.giris(db):
    exit()

musteri_service = MusteriService()
urun_service = UrunService()
siparis_service = SiparisService()
excel_service = ExcelService()

while True:

    print("\n===================================")
    print("         ERP OTOMASYONU")
    print("===================================")
    print("1 - Müşteri Ekle")
    print("2 - Müşterileri Listele")
    print("3 - Müşteri Güncelle")
    print("4 - Müşteri Sil")
    print("5 - Ürün Ekle")
    print("6 - Ürünleri Listele")
    print("7 - Ürün Güncelle")
    print("8 - Ürün Sil")
    print("9 - Sipariş Oluştur")
    print("10 - Müşterileri Excel'e Aktar")
    print("11 - Ürünleri Excel'e Aktar")
    print("12 - Çıkış")

    secim = input("\nSeçiminiz : ")

    if secim == "1":

        yeni = musteri_service.musteri_olustur()
        db.musteri_ekle(yeni)
        print("Müşteri başarıyla eklendi.")

    elif secim == "2":

        musteri_service.listele(db)

    elif secim == "3":

        musteri_service.guncelle(db)

    elif secim == "4":

        musteri_service.sil(db)

    elif secim == "5":

        yeni = urun_service.urun_olustur()
        db.urun_ekle(yeni)
        print("Ürün başarıyla eklendi.")

    elif secim == "6":

        urun_service.listele(db)

    elif secim == "7":

        urun_service.guncelle(db)

    elif secim == "8":

        urun_service.sil(db)

    elif secim == "9":

        siparis_service.siparis_olustur(db)

    elif secim == "10":

        excel_service.musterileri_excel(db)

    elif secim == "11":

        excel_service.urunleri_excel(db)

    elif secim == "12":

        db.kapat()
        print("Program kapatıldı.")
        break

    else:

        print("Hatalı seçim yaptınız.")