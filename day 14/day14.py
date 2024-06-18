#Definisikan sebuah class 
class Hewan:
    def __init__(self, jenis, suara):
        self.jenis = jenis  
        self.suara = suara  
    
    def bersuara(self):
        return f'{self.jenis} bersuara: {self.suara}'

#Membuat objek pertama dari class Hewan
hewan1 = Hewan('Kucing', 'Meong')

#Memanggil method bersuara dari objek hewan1
print(hewan1.bersuara())  

#Membuat objek kedua dari class Hewan
hewan2 = Hewan('Anjing', 'Guk guk')

#Memanggil method bersuara dari objek hewan2
print(hewan2.bersuara())  
