# Inisialisasi list dengan beberapa angka
daftar_angka = [1, 2, 3, 4, 5]

# Fungsi untuk menghitung jumlah angka dalam list
def hitung_jumlah(angka_list):
    jumlah = 0
    for angka in angka_list:
        jumlah += angka
    return jumlah

# Menampilkan daftar angka dan jumlahnya
print("Daftar Angka:", daftar_angka)
print("Jumlah Angka:", hitung_jumlah(daftar_angka))