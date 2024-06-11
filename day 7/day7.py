# Fungsi untuk mengecek apakah suatu bilangan prima
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Meminta pengguna untuk memasukkan nilai N
N = int(input("Masukkan nilai N: "))

print("Deret bilangan prima:")
# Perulangan for untuk mencetak deret bilangan prima
for i in range(2, N+1):
    if is_prime(i):
        print(i, end=" ")

print("\nDeret bilangan prima (menggunakan while):")
# Perulangan while untuk mencetak deret bilangan prima
num = 2
while num <= N:
    if is_prime(num):
        print(num, end=" ")
    num += 1