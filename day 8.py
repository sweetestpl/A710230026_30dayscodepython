class Mobil:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model

    def move(self):
        print(f"Mobil {self.merk} {self.model} berjalan di jalan raya.")

class Pesawat:
    def __init__(self, maskapai, jenis):
        self.maskapai = maskapai
        self.jenis = jenis

    def move(self):
        print(f"Pesawat {self.maskapai} {self.jenis} terbang di udara.")

class Kapal:
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    def move(self):
        print(f"Kapal {self.nama} {self.tipe} berlayar di laut.")

def create_mobil():
    merk = input("Masukkan merk mobil: ")
    model = input("Masukkan model mobil: ")
    return Mobil(merk, model)

def create_pesawat():
    maskapai = input("Masukkan nama maskapai: ")
    jenis = input("Masukkan jenis pesawat: ")
    return Pesawat(maskapai, jenis)

def create_kapal():
    nama = input("Masukkan nama kapal: ")
    tipe = input("Masukkan tipe kapal: ")
    return Kapal(nama, tipe)

def main():
    while True:
        print("Pilih jenis kendaraan:")
        print("1. Mobil")
        print("2. Pesawat")
        print("3. Kapal")
        print("4. Keluar")
        
        choice = input("Masukkan pilihan (1/2/3/4): ")
        
        if choice == '1':
            mobil = create_mobil()
            mobil.move()
        elif choice == '2':
            pesawat = create_pesawat()
            pesawat.move()
        elif choice == '3':
            kapal = create_kapal()
            kapal.move()
        elif choice == '4':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
