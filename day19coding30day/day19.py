#Definisi kelas 'Kotak'
class Kotak:
    def __init__(self, panjang, lebar, tinggi):
        self._panjang = panjang 
        self._lebar = lebar   
        self._tinggi = tinggi  
    
    def hitung_volume(self):
        return self._panjang * self._lebar * self._tinggi
    
    #Properti untuk mendapatkan panjang
    @property
    def panjang(self):
        return self._panjang
    
    #untuk mengatur panjang (setter)
    @panjang.setter
    def panjang(self, value):
        if value > 0:
            self._panjang = value
        else:
            print("Panjang harus lebih besar dari 0")

def main():
    kotak1 = Kotak(2, 3, 4)
    
    print(f"Panjang kotak1: {kotak1.panjang}")
    kotak1.panjang = 5
    print(f"Panjang kotak1 setelah diubah: {kotak1.panjang}")
    
    volume = kotak1.hitung_volume()
    print(f"Volume kotak1: {volume}")

if __name__ == "__main__":
    main()
