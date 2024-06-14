# menyimpan informasi siswa
siswa_1 = ("tono", 18, "lelaki", "kelas 12")
siswa_2 = ("tini", 17, "perempuan", "kelas 11")
siswa_3 = ("yanto", 18, "lelaki", "kelas 12")
siswa_4 = ("yanti", 17, "perempuan", "kelas 11")

# Fungsi untuk menampilkan informasi siswa
def tampilkan_info_siswa(siswa):
    print("Nama:", siswa[0])
    print("Usia:", siswa[1])
    print("Jenis Kelamin:", siswa[2])
    print("Tingkat:", siswa[3])
    print()

# Tampilkan informasi siswa
print("Informasi Siswa:")
tampilkan_info_siswa(siswa_1)
tampilkan_info_siswa(siswa_2)
tampilkan_info_siswa(siswa_3)
tampilkan_info_siswa(siswa_4)
