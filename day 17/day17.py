#Definisi kelas Kucing
class Kucing:
    def __init__(self, nama, umur, warna):
        self.nama = nama
        self.umur = umur
        self.warna = warna
    
    def tidur(self):
        print(f"{self.nama} sedang tidur.")

    def makan(self, makanan):
        print(f"{self.nama} sedang makan {makanan}.")

#Membuat objek dari kelas Kucing
kucing1 = Kucing("caty", 3, "Coklat")
kucing2 = Kucing("catay", 5, "Putih dan Hitam")

#Memanggil metode pada objek kucing
kucing1.tidur()    
kucing2.makan("ikan") 