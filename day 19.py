def hitung_luas_persegi_panjang():
    while True:
        try:
            # Meminta input panjang dari pengguna
            panjang = float(input("Masukkan panjang persegi panjang: "))
            if panjang <= 0:
                print("Panjang harus lebih besar dari 0. Silakan masukkan nilai yang valid.")
                continue
            
            # Meminta input lebar dari pengguna
            lebar = float(input("Masukkan lebar persegi panjang: "))
            if lebar <= 0:
                print("Lebar harus lebih besar dari 0. Silakan masukkan nilai yang valid.")
                continue
            
            # Hitung luas persegi panjang
            luas = panjang * lebar
            
            # Tampilkan hasil
            print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
            
            break  # Keluar dari loop setelah berhasil menghitung luas
            
        except ValueError:
            print("Masukkan harus berupa angka. Silakan coba lagi.")

# Panggil fungsi untuk menjalankan program
hitung_luas_persegi_panjang()
