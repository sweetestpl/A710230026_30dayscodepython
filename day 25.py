import random

def generate_random_numbers(count, min_value=1, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(count)]

def sort_numbers(numbers):
    return sorted(numbers)

def display_numbers(numbers, title=""):
    print(f"\n{title}:")
    for number in numbers:
        print(number, end=" ")
    print()

def main():
    print("Selamat datang di aplikasi pengurutan angka random!")
    count = int(input("Masukkan jumlah angka random yang ingin dibuat: "))
    min_value = int(input("Masukkan nilai terkecil dari rentang angka random: "))
    max_value = int(input("Masukkan nilai terbesar dari rentang angka random: "))
    
    random_numbers = generate_random_numbers(count, min_value, max_value)
    sorted_numbers = sort_numbers(random_numbers)
    
    print("\nAngka Random sebelum diurutkan:")
    display_numbers(random_numbers, "Angka Random")
    
    print("\nAngka Random setelah diurutkan:")
    display_numbers(sorted_numbers, "Angka Random yang sudah diurutkan")

if __name__ == "__main__":
    main()
