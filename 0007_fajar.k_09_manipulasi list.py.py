# data_angka = [1,2,3,4]
# print(data_angka)

# data_string = ["ucup","surya"]
# print(data_string)

# data_gado_gado = ["ucup","3","true"]
# print(data_gado_gado)

# # cra cpt memuat list
# data = range(0,10,3)#strt stip step
# print(data)
 
# data_list = list(data)
# print(data_list)

# list = [i**2 for i in range(0,10)]
# print(list)

# list = [i for i in range(0,10) if i%2 == 0]
# print(list)

# list_for_if = [i for i in range(0,10) if i !=5] 
# print(list_for_if) 
# list_for_if = [i for i in range(0, 10) if i % 2 == 0]
# print(list_for_if)
# list_for_if = [i for i in range(0,10) if i  % 2 != 1]
# print(list_for_if)

# manipulasi
# data =["bambang","ucup","asep"]
# #         0         1      2
# #         -3        -2     -1
# dataa = data[-1]
# print(dataa)
# banyak_dat = len(data)
# print(banyak_dat)

#mwnambahkan  data
#insert(possi,item )
# data.insert(1, "joko")
# data = data.insert
# print(data)
#tamabah diakhir
#append
# data.append("ikan")
# print(data)

# #menambahkan list dengan list
# data_baru= ["lutpi","klepon","nami"]
# data.extend(data_baru)
# print(data)

# #merubah data 
# data[2]="jarwo"
# print(data)

# #memghapus data
# data.remove("ucup")
# print(data)

# #menghapus data paling belakang
# data.pop()
# print(data)


# #ambil posisi datA
# data = ["rendi","iqbal","gana","kharil"]
# print(f"data={data}")
# index_Iqbal = data.index("iqbal") 
# index_Gana = data.index("gana") 
# print(f"index si Iqbal = {index_Iqbal}") 
# print(f"index si Gana = {index_Gana}")

#nested list
#----Nested LIST ---

# data_0 = [1,2]
# data_1 = [3,4] 
# data_list_biasa = [1,2,3,4] 
# print(f"list biasa = {data_list_biasa}")
# list_2D = [data_0, data_1, 6,7]
# print(f"list 2D = {list_2D}") 
# # #contoh penggunaan
# peserta_0 = ["Rendi", 25, "Laki-laki"]
# peserta_1 = ["Joni", 10, "Laki-laki"] 
# peserta_2 = ["Eka", 50, "Wanita"] 
# list_peserta = [peserta_0,peserta_1,peserta_2]
# print(f"peserta = {list_peserta}")
# for peserta in list_peserta:
#     print(f"nama\t : {peserta[0]}")
#     print(f"umur\t : {peserta[1]}")
#     print(f"gender\t : {peserta[2]}")



print(f"====penugasan====")
# 1. Diberikan list berikut: kendaraan = ['motor', 'mobil', 'sepeda', 'bus'] 

# a. Tambahkan 'truk' di akhir list 
# b. Sisipkan becak' pada index ke-1
# c. Hapus data yang berada paling belakang dari list tersebut.
# d. Ubah elemen 'sepeda' menjadi 'skuter'.
# e. Tampilkan informasi jumlah total data di dalam list tersebut 
print(f"jawab a:")
kendaraan = ["motor","mobil","sepeda","bus"]
#a=
kendaraan.append("truk")
print(kendaraan)
#b
print(f"jawab b :")
kendaraan.insert(1,"becak")
print(kendaraan)
#c
print(f"jawab c:")
kendaraan.pop ( )
print(kendaraan)
#d
print(f"jawab d:")
kendaraan[-2] = 'sekuter'
print(kendaraan)
#e 
print(f"jawab e:")
total_data = len(kendaraan)
print(total_data)

# 2. Diberikan list berikut: angka = [75, 80, 90, 75, 85, 100, 65]
#  a. Cari tahu di indeks ke berapa skor 100 berada.
#   b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
#    c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar.
#  d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil. 
print(f" jwbn no2\t")
angka = [75, 80, 90, 75, 85, 100, 65] 
#a
indeks_100 = angka.index(100)
print(f"a. Skor 100 berada di indeks ke: {indeks_100}")
#b
banyak_75 = angka.count(75)
print(f"b. Banyak siswa yang mendapat skor 75: {banyak_75}")
#c
angka.sort()
print(f"c. Urutkan dari terkecil ke terbesar: {angka}")
#d
angka.reverse()
print(f"d.urutkan dari terbesar ke terkecil:{angka}")

print(f"jwbn no3\t")
# 3.menu_utama = ["Nasi Goreng", "Mie Ayam"]
#  menu_tambahan = ["Kerupuk", "Es Teh"] 
#  Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut.

# Data menu
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
# Menggabungkan menu_tambahan ke dalam menu_utama
menu_utama.extend(menu_tambahan)
print(menu_utama)

print(f"jwbn no 4:\t")
# 4. Diberikan data nested list berupa informasi nama barang dan harganya:
#  data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]] 
#  a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.
#   b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: "Nama: [nama barang], Harga: [harga]" untuk setiap elemen di dalamnya. 
# Data nested list yang diberikan
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# ==========================================
# a. Menampilkan harga dari "Pensil"
# = "Pensil" berada di baris indeks 1, dan harganya di kolom indeks 1
# ==========================================
harga_pensil = data_barang[1][1]
print(f"Harga dari Pensil adalah: {harga_pensil}")
print("-" * 40) # Pembatas output

# b. 

for barang in data_barang:
    nama = barang[0]
    harga = barang[1]
    print(f"Nama: {nama}, Harga: {harga}")
