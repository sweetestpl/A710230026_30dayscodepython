# Buku Telepon

buku_telepon = {}

def tambah_kontak(nama, nomor):
    buku_telepon[nama] = nomor
    print(f"Kontak {nama} dengan nomor {nomor} berhasil ditambahkan.")

def cari_kontak(nama):
    if nama in buku_telepon:
        print(f"Nomor telepon {nama} adalah {buku_telepon[nama]}")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

def hapus_kontak(nama):
    if nama in buku_telepon:
        del buku_telepon[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

def tampilkan_semua_kontak():
    if buku_telepon:
        print("Daftar Kontak:")
        for nama, nomor in buku_telepon.items():
            print(f"{nama}: {nomor}")
    else:
        print("Buku telepon kosong.")

def menu():
    print("Selamat datang di Buku Telepon")
    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Tampilkan Semua Kontak")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4/5): ")
        
        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nomor = input("Masukkan nomor telepon: ")
            tambah_kontak(nama, nomor)
        elif pilihan == "2":
            nama = input("Masukkan nama yang ingin dicari: ")
            cari_kontak(nama)
        elif pilihan == "3":
            nama = input("Masukkan nama yang ingin dihapus: ")
            hapus_kontak(nama)
        elif pilihan == "4":
            tampilkan_semua_kontak()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan Buku Telepon. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
