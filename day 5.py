def hitung_luas_persegi(sisi):
    return sisi ** 2

def hitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_luas_lingkaran(jari_jari):
    import math
    return math.pi * (jari_jari ** 2)

def main():
    print("Pilih bentuk yang ingin dihitung luasnya:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")

    pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = hitung_luas_persegi(sisi)
        print(f"Luas persegi adalah: {luas}")
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = hitung_luas_persegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang adalah: {luas}")
    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = hitung_luas_segitiga(alas, tinggi)
        print(f"Luas segitiga adalah: {luas}")
    elif pilihan == 4:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = hitung_luas_lingkaran(jari_jari)
        print(f"Luas lingkaran adalah: {luas}")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
