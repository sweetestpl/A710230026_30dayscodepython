def faktorial(n):
    """Menghitung faktorial dari bilangan bulat n secara rekursif.
    
    Args:
        n (int): Bilangan bulat yang akan dihitung faktorialnya.
    
    Returns:
        int: Faktorial dari n.
    """
    # Kasus dasar: faktorial dari 0 atau 1 adalah 1
    if n == 0 or n == 1:
        return 1
    # Rekursi: n * faktorial dari (n-1)
    else:
        return n * faktorial(n - 1)

def contoh_penggunaan():
    """Fungsi untuk mendemonstrasikan penggunaan fungsi faktorial."""
    print("Menghitung faktorial dengan fungsi rekursif dalam Python.")
    
    # Meminta input dari pengguna
    n = int(input("Masukkan bilangan bulat untuk menghitung faktorialnya: "))
    
    # Menghitung faktorial menggunakan fungsi rekursif
    hasil = faktorial(n)
    
    # Menampilkan hasil perhitungan faktorial
    print(f"Faktorial dari {n} adalah {hasil}")

def main():
    """Fungsi utama untuk menjalankan program."""
    while True:
        contoh_penggunaan()
        
        # Menanyakan apakah pengguna ingin menghitung faktorial dari bilangan lain
        ulang = input("Apakah Anda ingin menghitung faktorial dari bilangan lain? (y/n): ").strip().lower()
        if ulang != 'y':
            print("Terima kasih telah menggunakan program faktorial. Sampai jumpa!")
            break

# Menjalankan program
if __name__ == "__main__":
    main()
