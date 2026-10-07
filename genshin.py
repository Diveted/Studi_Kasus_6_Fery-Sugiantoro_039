import json
import os

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_data():
    file = open("genshin.json", "r")
    data = json.load(file)
    file.close()

    print("\n=== DATA NILAI MAHASISWA ===")

    if len(data) == 0:
        print("belum ada data.")
    else:
        for mahasiswa in data:
            print("NIM         :", mahasiswa["nim"])
            print("Nama        :", mahasiswa["nama"])
            print("Mata Kuliah :", mahasiswa["mata_kuliah"])
            print("Nilai       :", mahasiswa["nilai"])
            print("-" * 28)

def tambah_data():
    file = open("genshin.json", "r")
    data = json.load(file)
    file.close()

    print("\n=== TAMBAH DATA NILAI ===")

    nim = input("NIM         : ")
    nama = input("Nama        : ")
    mata_kuliah = input("Mata Kuliah : ")
    nilai = input("Nilai       : ")

    data_baru = {
        "nim": nim,
        "nama": nama,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    }

    data.append(data_baru)

    file = open("genshin.json", "w")
    json.dump(data, file, indent=4)
    file.close()

    print("data berhasil ditambahkan")

while True:
    print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        tambah_data()

    elif pilihan == "3":
        bersihkan_layar()
        print("program selesai.")
        break

    else:
        print("pilihan tidak tersedia")