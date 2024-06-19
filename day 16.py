def balik_kata(kata):
    # Menggunakan metode slicing untuk membalikkan string
    kata_terbalik = kata[::-1]
    return kata_terbalik

def main():
    print("Program MemBalikkan Kata")
    print("========================")
    
    while True:
        kata_input = input("Masukkan kata yang ingin dibalikkan (kosong untuk keluar): ")
        
        # Validasi input
        if kata_input.strip() == "":
            print("Program selesai.")
            break
        
        # Memanggil fungsi untuk membalikkan kata
        hasil_balik = balik_kata(kata_input)
        
        # Menampilkan hasil
        print("Kata setelah dibalik:", hasil_balik)
        print()

if __name__ == "__main__":
    main()
