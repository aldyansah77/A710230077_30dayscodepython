# Meminta pengguna untuk memasukkan sebuah bilangan
bilangan = int(input("Masukkan sebuah bilangan: "))

# Menampilkan faktor dari bilangan yang dimasukkan
print("Faktor dari", bilangan, "adalah:")

# Menggunakan perulangan for untuk mencari faktor bilangan
for i in range(1, bilangan + 1):
    if bilangan % i == 0:
        print(i)