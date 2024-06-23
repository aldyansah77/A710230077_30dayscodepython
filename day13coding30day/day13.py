# Definisi class Manusia
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur} tahun")

    def berbicara(self, kata):
        print(f"{self.nama} berkata: '{kata}'")


# Definisi class Mahasiswa yang merupakan subclass dari Manusia
class Mahasiswa(Manusia):
    def __init__(self, nama, umur, jurusan):
        super().__init__(nama, umur)  
        self.jurusan = jurusan

    def belajar(self, subjek):
        print(f"{self.nama} sedang belajar {subjek} di jurusan {self.jurusan}")


#Membuat objek dari class Manusia dan Mahasiswa
orang1 = Manusia("tono", 18)
mahasiswa1 = Mahasiswa("tini", 17, "Informatika")

#Memanggil method dari class Manusia
orang1.info()
orang1.berbicara("Halo, apa kabar?")

#Memanggil method class Manusia, dan class Mahasiswa
mahasiswa1.info()
mahasiswa1.berbicara("Hai!")
mahasiswa1.belajar("Pemrograman")



