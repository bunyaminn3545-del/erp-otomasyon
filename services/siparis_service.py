from models.siparis import Siparis
from models.musteri import Musteri
from models.urun import Urun


class SiparisService:

    def siparis_olustur(self, db):

        print("\n===== SİPARİŞ OLUŞTUR =====")

        siparis_id = int(input("Sipariş ID : "))

        musteri_id = int(input("Müşteri ID : "))

        urun_id = int(input("Ürün ID : "))

        adet = int(input("Adet : "))

        db.cursor.execute(
            "SELECT * FROM musteriler WHERE id=?",
            (musteri_id,)
        )

        musteri_veri = db.cursor.fetchone()

        if musteri_veri is None:

            print("Müşteri bulunamadı.")

            return

        musteri = Musteri(
            musteri_veri[0],
            musteri_veri[1],
            musteri_veri[2],
            musteri_veri[3],
            musteri_veri[4]
        )

        db.cursor.execute(
            "SELECT * FROM urunler WHERE id=?",
            (urun_id,)
        )

        urun_veri = db.cursor.fetchone()

        if urun_veri is None:

            print("Ürün bulunamadı.")

            return

        urun = Urun(
            urun_veri[0],
            urun_veri[1],
            urun_veri[2],
            urun_veri[3]
        )

        if adet > urun.stok:

            print("Yeterli stok yok.")

            return

        siparis = Siparis(
            siparis_id,
            musteri,
            urun,
            adet
        )

        db.siparis_ekle(siparis)

        yeni_stok = urun.stok - adet

        db.cursor.execute(
            "UPDATE urunler SET stok=? WHERE id=?",
            (
                yeni_stok,
                urun.id
            )
        )

        db.conn.commit()

        print("Sipariş başarıyla oluşturuldu.")