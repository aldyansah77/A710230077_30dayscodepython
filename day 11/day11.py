# menyimpan informasi buku
buku = {
    'judul': 'bukuku',
    'pengarang': 'tono',
    'tahun': 2023
}

# Menampilkan informasi buku
print("Informasi Buku:")
print(f"Judul: {buku['judul']}")
print(f"Pengarang: {buku['pengarang']}")
print(f"Tahun Terbit: {buku['tahun']}")

# Mengubah tahun terbit buku
buku['tahun'] = 2024
print("\nSetelah diubah:")
print(f"Tahun Terbit: {buku['tahun']}")

# Menambahkan informasi penerbit
buku['penerbit'] = 'Penerbit buku'
print("\nSetelah ditambahkan:")
print(f"Penerbit: {buku['penerbit']}")

# Menghapus informasi penerbit
del buku['penerbit']
print("\nSetelah dihapus:")
print(buku)
