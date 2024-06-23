#meminta inputan nama depan
nama_depan = input('masukkan nama depan : ')
#meminta inputan nama belakang
nama_belakang = input('masukkan nama belakang : ')
#meminta inputan nim
nim = input('masukkan nim : ')

#menggabungkan nama depan dan belakang
nama_lengkap = [nama_depan,nama_belakang]
print('nama lengkap :',' '.join(nama_lengkap))
nama_lengkap = nama_depan +" "+nama_belakang

#print output
kata1 = 'pendidikan teknik informatika'
print(kata1.center(50))
print()
print('nama : ' , nama_lengkap)
print('nim : ' , nim)
print('fakultas keguruan dan ilmu pendidikan')
print()
kata2 = 'universitas muhammadiyah surakarta'
kapital = kata2.upper()
print(kapital.center(50))