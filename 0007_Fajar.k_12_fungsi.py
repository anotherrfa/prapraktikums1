# progam12.1
import os
os.system("cls")
# def hello_world():
#     # menampilkan hello world
#     print("hello world")
#     print("slamet kopling ")
#     print("ikan tuna ")

# hello_world()
# def hello_world(nama):
#     print(f"Selamat datang di Dunia, {nama}")

# hello_world("ucup")
# def tambah(angka_1, angka_2):
#     hasil = angka_1 + angka_2
#     print(f"{angka_1} + {angka_2} = {hasil}")

# tambah(1, 8)

# def say_hi(list_peserta):
#     data_peserta = list_peserta.copy()

#     for peserta in data_peserta:
#         print(f"Selamat datang {peserta}")

# kumpulan_mahasiswa = ["Budi", "Tono", "Joko"]

# say_hi(kumpulan_mahasiswa)
# A. Fungsi kuadrat
# def kuadrat(input_angka):
#     output_kuadrat = input_angka ** 2
#     return output_kuadrat

# y = kuadrat(5)
# print(y)
# print(kuadrat(6))
# z=10+kuadrat(7)
# print(z)
# def fungsi_tambah(angka_1, angka_2):
#     return angka_1 + angka_2

# a = fungsi_tambah(10, 8)
# print(a)
# def operasi_matematika(angka_1, angka_2):
#     tambah = angka_1 + angka_2
#     kurang = angka_1 - angka_2
#     kali = angka_1 * angka_2
#     bagi = angka_1 / angka_2

#     return tambah, kurang, kali, bagi

# k, l, m, n = operasi_matematika(9, 5)

# print(f"Hasil tambah = {k}")
# print(f"Hasil kurang = {l}")
# print(f"Hasil kali = {m}")
# print(f"Hasil bagi = {n}")

# def say_hello(nama="Ojul"):
#     print(f"Hello {nama}")

# say_hello("Ucup")
# say_hello()
# def sapa_dia(nama, pesan="Apa kabar?"):
#     print(f"hai {nama}, {pesan}")

# sapa_dia("Nanda", "Selamat pagi")
# sapa_dia("Budi")
# def hitung_pangkat(angka, pangkat):
#     hasil = angka**pangkat
#     return hasil

# print(hitung_pangkat(2, 4))

# hasil = hitung_pangkat(pangkat=3, angka=5)
# print(hasil)

# def faktorial(input_1=1, input_2=2,
#               input_3=3, input_4=4):
#     hasil = input_1 * input_2 * input_3 * input_4
#     return hasil

# print(faktorial())
# print(faktorial(input_3=10))

#Buatlah program dengan input dan fungsi untuk menghitung: 
# a. Luas persegi panjang b. Volume persegi panjang c. Luas lingkaran d. Volume bola
# A. Menghitung luas persegi panjang
def luas_persegi(panjang, lebar):
    return panjang * lebar

p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))

print("Luas =", luas_persegi(p, l))
#B . Menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

p = float(input("Masukkan panjang: "))
l = float(input("Masukkan lebar: "))
t = float(input("Masukkan tinggi: "))

print("Volume =", volume_balok(p, l, t))
#C. menghitung luas lingkaran 
def luas_lingkaran(r):
    if r % 7 == 0:
        return (22/7) * r ** 2
    else:
        return 3.14 * r ** 2
r = float(input("Masukkan jari-jari: "))

print("Luas lingkaran =", luas_lingkaran(r))
#D. menghitung volune bola 
def volume_bola(r):
    return (4/3) * 3.14 * r ** 3

r = float(input("Masukkan jari-jari: "))

print("Volume bola =", volume_bola(r))