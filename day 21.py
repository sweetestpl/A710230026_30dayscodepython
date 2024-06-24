def hitung_frekuensi_karakter(string):
    # Menggunakan dictionary untuk menyimpan frekuensi setiap karakter
    frekuensi = {}

    # Mengubah string menjadi lowercase agar case insensitive
    string = string.lower()

    # Mengiterasi setiap karakter dalam string
    for karakter in string:
        # Mengabaikan spasi
        if karakter == ' ':
            continue
        # Menambahkan karakter ke dictionary atau mengupdate jumlahnya
        if karakter in frekuensi:
            frekuensi[karakter] += 1
        else:
            frekuensi[karakter] = 1

    return frekuensi

def cetak_frekuensi(frekuensi):
    # Mencetak hasil frekuensi setiap karakter
    print("Frekuensi setiap karakter:")
    for karakter in sorted(frekuensi):
        print(f"{karakter}: {frekuensi[karakter]}")

    # Mencari karakter-karakter yang tidak muncul dalam string
    print("\nKarakter yang tidak muncul dalam string:")
    for ascii_code in range(256):
        karakter = chr(ascii_code)
        if karakter.isalpha() and karakter not in frekuensi:
            print(karakter)

# Contoh penggunaan:
input_string = "Hello World"
hasil_frekuensi = hitung_frekuensi_karakter(input_string)

print("String:", input_string)
cetak_frekuensi(hasil_frekuensi)
