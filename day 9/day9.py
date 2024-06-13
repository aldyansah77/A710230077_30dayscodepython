class pesawat():
    def __init__(self, jenis, bulan):
        self.jenis = jenis
        self.bulan = bulan

    def tampil(self):
        print(f"pesawat ini berjenis {self.jenis} sudah digunakan {self.bulan} bulan")

pesawat_saya = pesawat("airbus",3)
pesawat_dia = pesawat("boeing",4)

pesawat_saya.tampil()
pesawat_dia.tampil()