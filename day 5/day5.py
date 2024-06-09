# Membuat diskon tarif sepak bola
tahun_lahir = int(input("Masukukan tahun kelahiran penonton: "))
tahun_sekarang = 2024

# Menghitung usia
usia = tahun_sekarang - tahun_lahir

# Input harga tiket sepak bola
harga_tiket = int(input("Masukan harga tiket sepak bola: "))

# Tentukan diskon berdasarkan usia
if usia >= 3 and usia <= 7:
    diskon = 1.0 # Diskon 100%
elif usia >= 8 and usia <= 13:
    diskon = 0.5 # Disakon 50%
else:
    diskon = 0.0 # Tidak di berikan diskon

# Menghitung harga setelah diskon
harga_setelah_diskon = harga_tiket * (1 - diskon)

# Tampilkan hasil
print(f"Usia penonton: {usia} tahun")
print("Diskon:", int(diskon * 100), "%")
print("Harga tiket setelah diskon: Rp.", int(harga_setelah_diskon))