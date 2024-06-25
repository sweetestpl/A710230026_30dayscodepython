def binary_to_decimal(binary):
    try:
        # Validasi input biner hanya terdiri dari 0 dan 1
        if not all(bit == '0' or bit == '1' for bit in binary):
            raise ValueError("Input harus berupa string biner (hanya mengandung '0' dan '1').")

        decimal = 0
        power = len(binary) - 1
        for digit in binary:
            decimal += int(digit) * (2 ** power)
            power -= 1
        return decimal
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def main():
    while True:
        binary_string = input("Masukkan bilangan biner: ").strip()

        # Keluar dari loop jika pengguna memasukkan 'exit'
        if binary_string.lower() == 'exit':
            print("Terima kasih! Sampai jumpa.")
            break

        decimal_result = binary_to_decimal(binary_string)
        if decimal_result is not None:
            print(f"Nilai desimal dari {binary_string} adalah {decimal_result}")
        else:
            print("Silakan coba lagi.")

if __name__ == "__main__":
    main()
