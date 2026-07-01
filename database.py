import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("erp.db")
        self.cursor = self.conn.cursor()
        self.tablolari_olustur()

    def tablolari_olustur(self):

        # Müşteriler
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS musteriler(
            id INTEGER PRIMARY KEY,
            ad TEXT,
            telefon TEXT,
            mail TEXT,
            bakiye REAL
        )
        """)

        # Ürünler
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS urunler(
            id INTEGER PRIMARY KEY,
            ad TEXT,
            fiyat REAL,
            stok INTEGER
        )
        """)

        # Siparişler
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS siparisler(
            id INTEGER PRIMARY KEY,
            musteri_id INTEGER,
            urun_id INTEGER,
            adet INTEGER,
            toplam REAL
        )
        """)

        # Kullanıcılar
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT UNIQUE,
            sifre TEXT
        )
        """)

        self.conn.commit()

    # ---------------- MÜŞTERİ ----------------

    def musteri_ekle(self, musteri):

        self.cursor.execute("""
        INSERT INTO musteriler
        VALUES(?,?,?,?,?)
        """,
        (
            musteri.id,
            musteri.ad,
            musteri.telefon,
            musteri.mail,
            musteri.bakiye
        ))

        self.conn.commit()

    def musterileri_listele(self):

        self.cursor.execute("SELECT * FROM musteriler")

        return self.cursor.fetchall()

    def musteri_sil(self, id):

        self.cursor.execute(
            "DELETE FROM musteriler WHERE id=?",
            (id,)
        )

        self.conn.commit()

    def musteri_guncelle(self,musteri):

        self.cursor.execute("""

        UPDATE musteriler
        SET
        ad=?,
        telefon=?,
        mail=?,
        bakiye=?

        WHERE id=?

        """,

        (
            musteri.ad,
            musteri.telefon,
            musteri.mail,
            musteri.bakiye,
            musteri.id
        ))

        self.conn.commit()

    # ---------------- ÜRÜN ----------------

    def urun_ekle(self, urun):

        self.cursor.execute("""
        INSERT INTO urunler
        VALUES(?,?,?,?)
        """,
        (
            urun.id,
            urun.ad,
            urun.fiyat,
            urun.stok
        ))

        self.conn.commit()

    def urunleri_listele(self):

        self.cursor.execute("SELECT * FROM urunler")

        return self.cursor.fetchall()

    def urun_sil(self,id):

        self.cursor.execute(
            "DELETE FROM urunler WHERE id=?",
            (id,)
        )

        self.conn.commit()

    def urun_guncelle(self,urun):

        self.cursor.execute("""

        UPDATE urunler
        SET
        ad=?,
        fiyat=?,
        stok=?

        WHERE id=?

        """,

        (
            urun.ad,
            urun.fiyat,
            urun.stok,
            urun.id
        ))

        self.conn.commit()

    # ---------------- SİPARİŞ ----------------

    def siparis_ekle(self,siparis):

        self.cursor.execute("""

        INSERT INTO siparisler
        VALUES(?,?,?,?,?)

        """,

        (
            siparis.id,
            siparis.musteri.id,
            siparis.urun.id,
            siparis.adet,
            siparis.toplam
        ))

        self.conn.commit()

    def siparisleri_listele(self):

        self.cursor.execute(
            "SELECT * FROM siparisler"
        )

        return self.cursor.fetchall()

    # ---------------- KULLANICI ----------------

    def kullanici_ekle(self,kullanici,sifre):

        self.cursor.execute("""

        INSERT INTO kullanicilar(kullanici_adi,sifre)
        VALUES(?,?)

        """,

        (
            kullanici,
            sifre
        ))

        self.conn.commit()

    def kullanici_getir(self,kullanici):

        self.cursor.execute("""

        SELECT *
        FROM kullanicilar
        WHERE kullanici_adi=?

        """,

        (
            kullanici,
        ))

        return self.cursor.fetchone()

    def kapat(self):
        self.conn.close()

    def musteri_ara(self, id):
        self.cursor.execute(
            "SELECT * FROM musteriler WHERE id=?",
            (id,)
        )

        return self.cursor.fetchone()

    def urun_ara(self, id):
        self.cursor.execute(
            "SELECT * FROM urunler WHERE id=?",
            (id,)
        )

        return self.cursor.fetchone()

 