# Definisi kelas Kendaraan
class Kendaraan:
    def __init__(self, jumlah_roda):
        self.jumlah_roda = jumlah_roda
    
    def deskripsi(self):
        print(f"Kendaraan ini memiliki {self.jumlah_roda} roda.")

# Subclass Mobil yang mewarisi Kendaraan
class Mobil(Kendaraan):
    def __init__(self, jumlah_roda, merk):
        super().__init__(jumlah_roda)
        self.merk = merk
    
    def info(self):
        print(f"Mobil {self.merk} memiliki {self.jumlah_roda} roda.")

# Contoh penggunaan:
kendaraan = Kendaraan(4)
kendaraan.deskripsi()  # Output: Kendaraan ini memiliki 4 roda.

mobil1 = Mobil(4, "Toyota")
mobil1.info()  # Output: Mobil Toyota memiliki 4 roda.

mobil2 = Mobil(2, "Harley Davidson")
mobil2.info()  # Output: Mobil Harley Davidson memiliki 2 roda.
