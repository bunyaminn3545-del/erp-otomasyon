class Musteri:

    def __init__(self, id, ad, telefon, mail, bakiye=0):

        self.id = id
        self.ad = ad
        self.telefon = telefon
        self.mail = mail
        self.bakiye = bakiye

    def bakiye_ekle(self, miktar):
        self.bakiye += miktar

    def bakiye_cikar(self, miktar):
        self.bakiye -= miktar

    def telefon_degistir(self, telefon):
        self.telefon = telefon

    def mail_degistir(self, mail):
        self.mail = mail

    def bilgi_goster(self):

        print("---------------")
        print(f"ID      : {self.id}")
        print(f"Ad      : {self.ad}")
        print(f"Telefon : {self.telefon}")
        print(f"Mail    : {self.mail}")
        print(f"Bakiye  : {self.bakiye}")