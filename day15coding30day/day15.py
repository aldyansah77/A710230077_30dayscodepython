import math
class Lingkaran:
    def __init__(self, radius):
        self.radius = radius

    def hitung_luas(self):
        return math.pi * self.radius ** 2

    def hitung_keliling(self):
        return 2 * math.pi * self.radius

#Membuat objek dari kelas Lingkaran
lingkaran1 = Lingkaran(5)
lingkaran2 = Lingkaran(3)

#Memanggil metode untuk menghitung luas dan keliling lingkaran
luas1 = lingkaran1.hitung_luas()
keliling1 = lingkaran1.hitung_keliling()

luas2 = lingkaran2.hitung_luas()
keliling2 = lingkaran2.hitung_keliling()

#Menampilkan hasil perhitungan
print(f"Luas lingkaran 1: {luas1:.2f}")
print(f"Keliling lingkaran 1: {keliling1:.2f}")

print(f"Luas lingkaran 2: {luas2:.2f}")
print(f"Keliling lingkaran 2: {keliling2:.2f}")