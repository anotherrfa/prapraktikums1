# import datetime


# mahasiswa1 = {
#     'nama'      : 'Ucup Surucup',
#     'nim'       : '19022001', # int -> (11 digit),
#     'sks_lulus' : 130,
#     'beasiswa'  : False,
#     # 'lahir'     : datetime.datetime(tahun,tanggal,bulan) -> format penulisan mengikuti pemilik library
#     'lahir'     : datetime.datetime(2001,4,10)

# }

# mahasiswa2 = {
#     'nama'      : 'Azan Maghrib',
#     'nim'       : '19022002', # int -> (11 digit),
#     'sks_lulus' : 90,
#     'beasiswa'  : True,
#     'lahir'     : datetime.datetime(2002,10,10)

# }

# mahasiswa3 = {
#     'nama'      : 'Slamet Dunia Akhirat',
#     'nim'       : '19022003',
#     'sks_lulus' : 100,
#     'beasiswa'  : False,
#     'lahir'     : datetime.datetime(1977,5,10)

# }

# data_mahasiswa = {
#     'MAH001'  : mahasiswa1,
#     'MAH002'  : mahasiswa2,
#     'MAH003'  : mahasiswa3,
# }

# print(f'{'KEY':<8} {'NAMA':<25} {'NIM' :<10} {'SKS ':<6} {'BEASISWA ':<10} {'LAHIR ':<6}')
# print('-'*70)

# for k in data_mahasiswa:
#   KEY = k

#   NAMA = data_mahasiswa[KEY]['nama']
#   NIM = data_mahasiswa[KEY]['nim']
#   SKS = data_mahasiswa[KEY]['sks_lulus']
#   BEASISWA = data_mahasiswa[KEY]['beasiswa']
#   LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

#   print(f'{KEY:<8} {NAMA:<25} {NIM :<10} {SKS :<6} {BEASISWA :^10} {LAHIR :<6}')

#11.2
# import datetime
# mahasiswa_template = {
#     'nama': 'nama',
#     'nim': '00000000',
#     'sks_lulus': 0,
#     'lahir': datetime.datetime(1111, 1, 11)
# }
# print(f"{'SELAMAT DATANG':^20}")
# print(f"{'DATA MAHASISWA':^20}")
# print("-"*20)
# mahasiswa = dict.fromkeys(mahasiswa_template.keys())
# mahasiswa_template.keys()

# mahasiswa['nama'] = input("Nama Mahasiswa: ")
# mahasiswa['nim'] = input("NIM Mahasiswa: ")
# mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
# TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
# BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
# TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
# mahasiswa['lahir'] = datetime.datetime(
#     TAHUN_LAHIR,
#     BULAN_LAHIR,
#     TANGGAL_LAHIR
# )
# print(mahasiswa)

# #progam 11.3
# import datetime
# import os 
# import string
# import random

# mahasiswa_template = {
#     'nama': 'nama',
#     'nim': '00000000',
#     'sks_lulus': 0,
#     'lahir': datetime.datetime(1111, 1, 11)
# }
# data_mahasiswa = {}
# while True:
#     os.system("cls")
#     print(f"{'SELAMAT DATANG':^20}")
#     print(f"{'DATA MAHASISWA':^20}")
#     print("-"*20)

#     mahasiswa = dict.fromkeys(mahasiswa_template.keys())
#     mahasiswa['nama'] = input("Nama Mahasiswa: ")
#     mahasiswa['nim'] = input("NIM Mahasiswa: ")
#     mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
#     TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
#     BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
#     TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))

#     mahasiswa['lahir'] = datetime.datetime(
#     TAHUN_LAHIR,
#     BULAN_LAHIR,
#     TANGGAL_LAHIR
# )
#     KEY = ''.join(
#     (random.choice(string.ascii_uppercase) for i in range(6))
# )
#     data_mahasiswa.update({KEY: mahasiswa})
#     print(
#     f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} "
#     f"{'SKS Lulus':<10} {'Tanggal Lahir':<10}"
# )
#     print('-'*60)
#     for mahasiswa in data_mahasiswa:
#       KEY = mahasiswa

#     NAMA = data_mahasiswa[KEY]['nama']
#     NIM = data_mahasiswa[KEY]['nim']
#     SKS = data_mahasiswa[KEY]['sks_lulus']
#     LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

#     print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
#     is_done = input("Mau tambah lagi bro (y/n)? ")
#     if is_done == "n":
#       break
#     print("\nAkhir dari program, terima kasih")
#Buatlah program sistem manajemen perpustakaan sederhana 
# (menambahkan dan menampilkan buku baru ke dalam sistem) menggunakan konsep multi-keys dan nesting dictionary dengan format 
# - - - - - - KEYS JUDUL BUKU PENULIS TAHUN TERBIT TANGGAL TERAKHIR PINJAM STATUS (TERSEDIA / TIDAK) #
import datetime
import os
import string
import random

buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0000,
    'terakhir_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'TERSEDIA'
}

data_perpustakaan = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^40}")
    print("-" * 40)

    buku = dict.fromkeys(buku_template.keys())
    buku['judul'] = input("Judul Buku: ")
    buku['penulis'] = input("Penulis: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit (YYYY): "))

    TAHUN = int(input("Tahun Terakhir Pinjam (YYYY): "))
    BULAN = int(input("Bulan Terakhir Pinjam (1-12): "))
    TANGGAL = int(input("Tanggal Terakhir Pinjam (1-31): "))
    buku['terakhir_pinjam'] = datetime.datetime(TAHUN, BULAN, TANGGAL)

    buku['status'] = input("Status (TERSEDIA / TIDAK): ").upper()

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_perpustakaan.update({KEY: buku})

    print(f"\n{'KEYS':<6} {'JUDUL BUKU':<22} {'PENULIS':<16} {'TAHUN':<6} {'TERAKHIR PINJAM':<16} {'STATUS':<10}")
    print("-" * 82)

    for key_buku in data_perpustakaan:
        JUDUL = data_perpustakaan[key_buku]['judul']
        PENULIS = data_perpustakaan[key_buku]['penulis']
        TAHUN_TERBIT = data_perpustakaan[key_buku]['tahun_terbit']
        PINJAM = data_perpustakaan[key_buku]['terakhir_pinjam'].strftime("%x")
        STATUS = data_perpustakaan[key_buku]['status']

        print(f"{key_buku:<6} {JUDUL:<22} {PENULIS:<16} {TAHUN_TERBIT:<6} {PINJAM:^16} {STATUS:<10}")

    print("\n")
    lanjut = input("Tambah data buku lagi (y/n)? ")
    if lanjut.lower() == "n":
        break

print("\nProgram perpustakaan selesai.")
