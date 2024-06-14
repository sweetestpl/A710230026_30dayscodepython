class Bentuk:
    def luas(self):
        pass

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return self.panjang * self.lebar

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius
    
    def luas(self):
        return 3.14 * self.radius * self.radius

def hitung_luas(bentuk):
    print("Luas:", bentuk.luas())

# Membuat objek dari kelas yang berbeda
persegi_panjang = PersegiPanjang(5, 4)
lingkaran = Lingkaran(3)

# Memanggil metode luas() dari masing-masing objek
hitung_luas(persegi_panjang)  # Output: Luas: 20
hitung_luas(lingkaran)        # Output: Luas: 28.26 (approx.)
