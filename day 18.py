def hitung_target_tabungan(target, bulan, suku_bunga):
    """
    Menghitung target tabungan berdasarkan jumlah yang ingin dicapai,
    jumlah bulan, dan suku bunga per bulan (dalam persen).

    Parameter:
    target (float): Jumlah uang yang ingin dicapai.
    bulan (int): Jumlah bulan untuk mencapai target.
    suku_bunga (float): Suku bunga tabungan per bulan (dalam persen).

    Returns:
    float: Jumlah uang yang harus ditabung setiap bulan.
    """

    # Konversi suku bunga dari persen ke desimal
    suku_bunga_decimal = suku_bunga / 100

    # Menghitung jumlah uang yang harus ditabung setiap bulan
    if bulan > 0 and suku_bunga_decimal > 0:
        jumlah = target / (bulan * (1 + suku_bunga_decimal))
        return jumlah
    else:
        return 0

# Input dari pengguna
print("Program Penghitung Target Tabungan")
print("---------------------------------")
target = float(input("Masukkan jumlah uang yang ingin Anda capai: "))
bulan = int(input("Masukkan jumlah bulan untuk mencapai target: "))
suku_bunga = float(input("Masukkan suku bunga tabungan per bulan (dalam persen): "))

# Memanggil fungsi untuk menghitung jumlah yang harus ditabung setiap bulan
jumlah_tabungan_per_bulan = hitung_target_tabungan(target, bulan, suku_bunga)

# Menampilkan hasil
if jumlah_tabungan_per_bulan > 0:
    print(f"Anda perlu menabung sebesar Rp {jumlah_tabungan_per_bulan:.2f} setiap bulan untuk mencapai target tabungan Anda.")
else:
    print("Input tidak valid. Pastikan jumlah bulan dan suku bunga lebih dari nol.")
