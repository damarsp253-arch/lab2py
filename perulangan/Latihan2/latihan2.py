# Latihan 2: Bilangan acak < 0.5
n = int(input("Masukkan jumlah n: "))
count = 0

while count < n:
    angka = random.random(1)
    if angka < 0.5:
        print(angka)
        count += 1