from openpyxl import Workbook


class ExcelService:

    def musterileri_excel(self, db):

        wb = Workbook()

        ws = wb.active

        ws.title = "Müşteriler"

        ws.append([
            "ID",
            "Ad",
            "Telefon",
            "Mail",
            "Bakiye"
        ])

        musteriler = db.musterileri_listele()

        for musteri in musteriler:

            ws.append([
                musteri[0],
                musteri[1],
                musteri[2],
                musteri[3],
                musteri[4]
            ])

        wb.save("musteriler.xlsx")

        print("Excel oluşturuldu.")

    def urunleri_excel(self, db):

        wb = Workbook()

        ws = wb.active

        ws.title = "Ürünler"

        ws.append([
            "ID",
            "Ürün",
            "Fiyat",
            "Stok"
        ])

        urunler = db.urunleri_listele()

        for urun in urunler:

            ws.append([
                urun[0],
                urun[1],
                urun[2],
                urun[3]
            ])

        wb.save("urunler.xlsx")

        print("Excel oluşturuldu.")