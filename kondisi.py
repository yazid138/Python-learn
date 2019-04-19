#!/bin/python3

nilai = int(input("Berapa nilaimu: "))
if nilai > 11:
    print("Masukan nilai Kembali: ")
elif nilai > 7:
    print("Selamat Kamu Lulus!")
else:
    print("Kamu harus ikut Ujian lagi!")

umur = input("berapa umur kamu? ")
aku = "bocah" if int(umur) < 10 else "dewasa"#ternary
print (aku)
    
# Kondisi IF
# if (umur < 10):
#     print("bocah")
# else:
#     print("dewasa")

jawab = input("Apakah kamu Jomblo: [Y/n]")
if jawab == "n" or jawab == "N":
    jawaban = False
else:
    jawaban = True
jomblo = jawaban
status = ("Menikah", "Single")[jomblo]
print (status)