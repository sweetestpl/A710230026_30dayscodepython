# Definisikan kelas Induk (Parent Class)
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
        print("Hewan ini bersuara")

# Definisikan kelas Anak (Child Class) yang mewarisi sifat dari kelas Induk
class Kucing(Hewan):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna

    # Override metode bersuara dari kelas Induk
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara: Meow")

# Definisikan kelas Anak (Child Class) lainnya
class Anjing(Hewan):
    def __init__(self, nama, jenis, ukuran):
        super().__init__(nama, jenis)
        self.ukuran = ukuran

    # Override metode bersuara dari kelas Induk
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara: Guk guk")

# Membuat objek dari kelas Anak (Child Class)
kucing1 = Kucing("Meong", "Kucing", "Oren")
print(f"Nama: {kucing1.nama}, Jenis: {kucing1.jenis}, Warna: {kucing1.warna}")
kucing1.bersuara()

# Membuat objek dari kelas Anak (Child Class) lainnya
anjing1 = Anjing("Doggy", "Anjing", "Besar")
print(f"Nama: {anjing1.nama}, Jenis: {anjing1.jenis}, Ukuran: {anjing1.ukuran}")
anjing1.bersuara()
