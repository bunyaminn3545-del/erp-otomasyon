from models.urun import Urun


class UrunService:

    def urun_olustur(self):

        print("\n===== YENİ ÜRÜN =====")

        id = int(input("ID: "))
        ad = input("Ürün Adı: ")
        fiyat = float(input("Fiyat: "))
        stok = int(input("Stok: "))

        return Urun(
            id,
            ad,
            fiyat,
            stok
        )

    def listele(self, db):

        urunler = db.urunleri_listele()

        print("\n========== ÜRÜNLER ==========")

        if len(urunler) == 0:
            print("Kayıt bulunamadı.")
            return

        for urun in urunler:

            print("----------------------------")
            print("ID :", urun[0])
            print("Ad :", urun[1])
            print("Fiyat :", urun[2])
            print("Stok :", urun[3])

    def sil(self, db):

        id = int(input("Silinecek ürün ID : "))

        db.urun_sil(id)

        print("Ürün silindi.")

    def guncelle(self, db):

        print("\n===== ÜRÜN GÜNCELLE =====")

        id = int(input("ID : "))
        ad = input("Yeni Ürün Adı : ")
        fiyat = float(input("Yeni Fiyat : "))
        stok = int(input("Yeni Stok : "))

        urun = Urun(
            id,
            ad,
            fiyat,
            stok
        )

        db.urun_guncelle(urun)

        print("Ürün güncellendi.")