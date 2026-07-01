class Siparis:

    def __init__(self, id, musteri, urun, adet):

        self.id = id
        self.musteri = musteri
        self.urun = urun
        self.adet = adet

        self.toplam = urun.fiyat * adet

    def siparis_olustur(self):

        self.urun.stok_azalt(self.adet)

        print("\nSipariş oluşturuldu.")

    def bilgi_goster(self):

        print("---------------")
        print(f"Sipariş No : {self.id}")
        print(f"Müşteri    : {self.musteri.ad}")
        print(f"Ürün       : {self.urun.ad}")
        print(f"Adet       : {self.adet}")
        print(f"Toplam     : {self.toplam} TL")