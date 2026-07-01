class Urun:

    def __init__(self, id, ad, fiyat, stok):

        self.id = id
        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok

    def fiyat_degistir(self, fiyat):
        self.fiyat = fiyat

    def stok_arttir(self, adet):
        self.stok += adet

    def stok_azalt(self, adet):

        if adet <= self.stok:
            self.stok -= adet
        else:
            print("Yeterli stok yok.")

    def bilgi_goster(self):

        print("---------------")
        print(f"ID    : {self.id}")
        print(f"Ürün  : {self.ad}")
        print(f"Fiyat : {self.fiyat}")
        print(f"Stok  : {self.stok}")