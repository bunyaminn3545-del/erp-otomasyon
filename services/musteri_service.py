from models.musteri import Musteri


class MusteriService:

    def musteri_olustur(self):

        print("\n===== YENİ MÜŞTERİ =====")

        id = int(input("ID: "))
        ad = input("Ad: ")
        telefon = input("Telefon: ")
        mail = input("Mail: ")
        bakiye = float(input("Bakiye: "))

        return Musteri(
            id,
            ad,
            telefon,
            mail,
            bakiye
        )

    def listele(self, db):

        musteriler = db.musterileri_listele()

        print("\n========== MÜŞTERİLER ==========")

        if len(musteriler) == 0:
            print("Kayıt bulunamadı.")
            return

        for musteri in musteriler:

            print("----------------------------")
            print("ID :", musteri[0])
            print("Ad :", musteri[1])
            print("Telefon :", musteri[2])
            print("Mail :", musteri[3])
            print("Bakiye :", musteri[4])

    def sil(self, db):

        id = int(input("Silinecek müşteri ID : "))

        db.musteri_sil(id)

        print("Müşteri silindi.")

    def musteri_sil(self, db):

        id = int(input("Silinecek müşteri ID: "))

        db.musteri_sil(id)

        print("Müşteri silindi.")

    def guncelle(self, db):

        print("\n===== MÜŞTERİ GÜNCELLE =====")

        id = int(input("ID : "))
        ad = input("Yeni Ad : ")
        telefon = input("Yeni Telefon : ")
        mail = input("Yeni Mail : ")
        bakiye = float(input("Yeni Bakiye : "))

        musteri = Musteri(
            id,
            ad,
            telefon,
            mail,
            bakiye
        )

        db.musteri_guncelle(musteri)

        print("Müşteri güncellendi.")

    def ara(self, db):

        id = int(input("Müşteri ID : "))

        musteri = db.musteri_ara(id)

        if musteri:

            print("\n===== MÜŞTERİ =====")
            print("ID :", musteri[0])
            print("Ad :", musteri[1])
            print("Telefon :", musteri[2])
            print("Mail :", musteri[3])
            print("Bakiye :", musteri[4])

        else:

            print("Müşteri bulunamadı.")