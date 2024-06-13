def kilometer_to_meter(kilometer):
    """
    Fungsi untuk mengonversi jarak dari kilometer menjadi meter.

    Args:
        kilometer (float): Jarak dalam kilometer.

    Returns:
        float: Jarak dalam meter.
    """
    meter = kilometer * 1000
    return meter

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    try:
        kilometer = float(input("Masukkan jarak dalam kilometer: "))
        if kilometer < 0:
            print("Jarak tidak bisa negatif.")
            return
        meter = kilometer_to_meter(kilometer)
        print(f"{kilometer} kilometer sama dengan {meter} meter.")
    except ValueError:
        print("Masukkan yang Anda berikan bukan angka yang valid.")

if __name__ == "__main__":
    main()
