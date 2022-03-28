print (" .:: Pengulangan Bersarang ::. \n")

baris = int(input("Masukkan Batas Perulangan = "))
print()

for x in range(baris, 0, -1):
    print('.' * (x - 1), end="")
    print(x, end="")
    print()