import hashlib


class Login:

    def sifrele(self, sifre):

        return hashlib.sha256(
            sifre.encode()
        ).hexdigest()

    def giris(self, db):

        print("====== GİRİŞ ======")

        kullanici = input("Kullanıcı Adı : ")

        sifre = input("Şifre : ")

        sifre = self.sifrele(sifre)

        bilgi = db.kullanici_getir(kullanici)

        if bilgi is None:

            print("Kullanıcı bulunamadı.")

            return False

        if bilgi[2] == sifre:

            print("Giriş başarılı.")

            return True

        print("Şifre yanlış.")

        return False