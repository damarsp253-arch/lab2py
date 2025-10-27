import random

# Meminta input jumlah bilangan
n = int(input("Masukkan jumlah n: "))

i = 0  # inisialisasi penghitung
while i < n:
    angka = random.random()  # menghasilkan angka acak antara 0.0 - 1.0
    if angka < 0.5:          # hanya menampilkan angka yang lebih kecil dari 0.5
        print(angka)
        i += 1               # hanya dihitung jika memenuhi syarat
# program selesai 
# latihan4.py