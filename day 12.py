# Fungsi untuk operasi penjumlahan
def tambah(a, b):
    return a + b

# Fungsi untuk operasi pengurangan
def kurang(a, b):
    return a - b

# Fungsi untuk operasi perkalian
def kali(a, b):
    return a * b

# Fungsi untuk operasi pembagian
def bagi(a, b):
    # Tambahkan penanganan untuk pembagian dengan nol
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol"
    else:
        return a / b

# Fungsi utama kalkulator
def kalkulator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(angka1, "+", angka2, "=", tambah(angka1, angka2))
    elif pilihan == '2':
        print(angka1, "-", angka2, "=", kurang(angka1, angka2))
    elif pilihan == '3':
        print(angka1, "*", angka2, "=", kali(angka1, angka2))
    elif pilihan == '4':
        print(angka1, "/", angka2, "=", bagi(angka1, angka2))
    else:
        print("Input tidak valid")

# Panggil fungsi kalkulator
kalkulator()
