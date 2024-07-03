# Inisialisasi daftar barang beserta harganya
daftar_barang = {
    'apel': 5000,
    'pisang': 3000,
    'jeruk': 7000,
    'melon': 10000,
    'semangka': 12000
}

# Fungsi untuk menampilkan daftar barang
def tampilkan_daftar_barang():
    print("=== DAFTAR BARANG ===")
    for barang, harga in daftar_barang.items():
        print(f"{barang}: Rp {harga}")

# Fungsi untuk menghitung total belanja
def hitung_total_belanja(items):
    total = 0
    for item, qty in items.items():
        if item in daftar_barang:
            total += daftar_barang[item] * qty
    return total

# Program utama
def main():
    keranjang = {}
    
    print("Selamat datang di program kasir!")
    tampilkan_daftar_barang()
    
    while True:
        print("\nMasukkan barang yang dibeli dan jumlahnya (cth: apel 2), atau ketik 'selesai' untuk mengakhiri belanja.")
        masukan = input(">> ")
        
        if masukan.lower() == 'selesai':
            break
        
        try:
            item, qty = masukan.split()
            qty = int(qty)
            
            if item in daftar_barang:
                if item in keranjang:
                    keranjang[item] += qty
                else:
                    keranjang[item] = qty
                print(f"{qty} {item} telah ditambahkan ke keranjang.")
            else:
                print("Barang tidak ditemukan. Masukkan nama barang yang benar.")
        
        except ValueError:
            print("Format masukan salah. Harap masukkan nama barang dan jumlahnya (cth: apel 2).")
    
    # Menampilkan ringkasan belanja
    print("\n=== RINGKASAN BELANJA ===")
    for item, qty in keranjang.items():
        print(f"{item}: {qty} pcs")
    total_belanja = hitung_total_belanja(keranjang)
    print(f"Total belanja: Rp {total_belanja}")

    print("\nTerima kasih telah berbelanja!")

if __name__ == "__main__":
    main()
