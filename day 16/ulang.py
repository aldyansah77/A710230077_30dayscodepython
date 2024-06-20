#Definisikan kelas Kendaraan
class Kendaraan:
    def __init__(self, jenis, merk, tahun):
        self.jenis = jenis    
        self.merk = merk     
        self.tahun = tahun    
    
    #Method untuk menampilkan informasi tentang Kendaraan
    def info(self):
        print(f"Jenis: {self.jenis}, Merk: {self.merk}, Tahun: {self.tahun}")

#Membuat objek dari kelas Kendaraan
mobil1 = Kendaraan("Mobil", "Toyota", 2024)
motor1 = Kendaraan("Motor", "Honda", 2023)

# Memanggil method info untuk menampilkan informasi objek
mobil1.info()   
motor1.info()   
