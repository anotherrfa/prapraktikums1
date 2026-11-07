#tupple
# y=(1,2,"aki","aki","asin","asir")
# print(y)

# print(y[0])
# print(y[-1])


# #set
# rombel_it = {1,2,3,4,4,5}
# print(rombel_it)
# # print(rombel_it[0])


#dictionary
# data_mahasigma = {
# "key" : "value",
# "nama":"nadia",
# "npm": 6666,
# "prodi": "sastra mesin",

# }
# print(data_mahasigma["nama"])
# print(data_mahasigma["prodi"])

#operation dictonary
#panjang dictionary
#lendict = len(data_mahasigma)
#print(lendict)
#menegecek key dalam dictonary
# key = "nadia"
# checkkey = key in data_mahasigma
# print(f"apakah {key} ada di data_mahasigma:{checkkey}")
#mengakses value 
#print(data_mahasigma.get("prodi")) 
# #mengupdate data 
# data_mahasigma["nama"] = 'ikan' #mengubah
# data_mahasigma["jurusan"] = 1
# print(data_mahasigma)
# #menghapus data
# del data_mahasigma["prodi"]# menghapus
# print(data_mahasigma)

#perulangan dictonary
# jenis_ikan = {
#     "le":"lele",
#     'la':"nila",
#     "der":"wader",
#     "ceng":"uceng"
# }
# # for ikan in jenis_ikan:
# #     print(ikan)
#   # operator untuk mengambil item
# keys = jenis_ikan.keys()
# print(keys)
# for key in jenis_ikan.keys():
#   print( jenis_ikan.get(key)) 

# values= jenis_ikan.values()
# print(values)
# for values in jenis_ikan.values():
#   print(values) 

# items = jenis_ikan.items() 
# print(items) 
# for item in jenis_ikan.items(): 
#  print(item) 
# for key,value in jenis_ikan.items(): 
#  print(f"key = {key}, value = {value}") 

##! penugasan 
# 1. Tuple
# a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri Anda: ("Nama", "NIM", "Prodi"). 
#jawab:
data_mahasiwa = ("Nama:nadia","Nim: 00067","prodi:sastra mesin"
)
print(data_mahasiwa)
print(f"progam diatas adalah contoh data tuple data diri mahasiswa bernama nadia anak sastra mesin.")
#b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya. 
print(data_mahasiwa[1])
print(data_mahasiwa[2])
print(f"dari data tuple kita dapat menampilkan indeks berdasarkan urutan letak data ,seperti nim berada pada indeks ke 1 dan prodi di indeks ke 2")
#c.c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi 
data_mahasiwa[2]="Teknologi Informasi"
print(data_mahasiwa[2])
#hasilnya akan eror karena data tuple tidak dapat di ubah(immutable)
#d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali! 
# d. Set dari barisan angka
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("nilai_angka:", nilai_angka)
# yang terjadi pada angka 4 dan 10 yang ditulis dua kali hanya akan disimpan satu kali,karena set otomatis menghapus duplikat dan urutan pada set tidak ter urut.
#2. Manipulasi Dictionary
#  a. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut: - "nim": "240101" - "nama": "Budi Santoso" - "prodi": "Teknologi Informasi" 
#  b. Ubah nilai "prodi" menjadi "Sastra Mesin " sekaligus menambahkan key baru "angkatan" dengan nilai 2026.
#   c. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar.
#===== LATIHAN 2: MANIPULASI DICTIONARY =====
print("\n=== Latihan 2 ===")

# # a. Buat dictionary
 data_mahasiswa2 = {
     "nim": "240101",
     "nama": "Budi Santoso",
     "prodi": "Teknologi Informasi",
 }
 print(data_mahasiswa2)
# # b. Ubah prodi + tambah angkatan
 data_mahasiswa2["prodi"] = "Sastra Mesin"
 data_mahasiswa2["angkatan"] = 2026
 print(data_mahasiswa2)
# # c. Hapus nim, tampilkan hasil akhir
 del data_mahasiswa2["nim"]
 print(data_mahasiswa2)

# 3. Perulangan pada Dictionary 
# a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000} 
# b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000"
#  c. Tampilkan total belanja 
# ===== LATIHAN 3: PERULANGAN DICTIONARY =====
print("\n=== Latihan 3 ===")

# a. Dictionary keranjang
keranjang = {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}
print(keranjang)
# b. Tampilkan tiap barang dan harga
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
# c. Total belanja
total = 0
for harga in keranjang.values():
    total += harga
print(f"Total belanja: Rp {total}")
