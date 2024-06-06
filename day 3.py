def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Selamat datang di Kalkulator Suhu!")
    print("Pilih opsi yang Anda inginkan:")
    print("1. Konversi Celsius ke Fahrenheit")
    print("2. Konversi Fahrenheit ke Celsius")
    print("3. Konversi Celsius ke Kelvin")
    print("4. Konversi Kelvin ke Celsius")
    print("5. Konversi Fahrenheit ke Kelvin")
    print("6. Konversi Kelvin ke Fahrenheit")

    option = input("Masukkan nomor opsi: ")

    if option == "1":
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        print("Suhu dalam Fahrenheit adalah:", celsius_to_fahrenheit(celsius), "F")
    elif option == "2":
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        print("Suhu dalam Celsius adalah:", fahrenheit_to_celsius(fahrenheit), "°C")
    elif option == "3":
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        print("Suhu dalam Kelvin adalah:", celsius_to_kelvin(celsius), "K")
    elif option == "4":
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        print("Suhu dalam Celsius adalah:", kelvin_to_celsius(kelvin), "°C")
    elif option == "5":
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        print("Suhu dalam Kelvin adalah:", fahrenheit_to_kelvin(fahrenheit), "K")
    elif option == "6":
        kelvin = float(input("Masukkan suhu dalam Kelvin: "))
        print("Suhu dalam Fahrenheit adalah:", kelvin_to_fahrenheit(kelvin), "F")
    else:
        print("Opsi yang dimasukkan tidak valid. Silakan masukkan nomor opsi yang benar.")

if __name__ == "__main__":
    main()
