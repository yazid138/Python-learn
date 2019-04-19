#!/bin/python3

# perulangan For

# bentuk Umum
ulang = 5

for i in range(ulang):
    print("Perulangan Ke-"+str(i))
#list pada python
item = ['kopi', 'susu', 'teh']

for isi in item:
    print(isi)

# Perulanagn While
jawab = input("Apakah kamu ingin perulangan: [Y/n]")
if jawab == 'n' or jawab == 'N':
    jawaban = False
else:
    jawaban = True
hitung = 0

while(jawaban):
    hitung += 1
    print("Perulangan Ke-"+str(hitung))
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break

print ("Total perulangan: " + str(hitung))