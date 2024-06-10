def cek_bilangan_prima(n):
    """Fungsi untuk mengecek apakah sebuah bilangan adalah bilangan prima atau bukan."""
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    # Mengecek bilangan dari 3 hingga akar kuadrat dari n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Contoh penggunaan
bilangan = int(input("Masukkan sebuah bilangan: "))
if cek_bilangan_prima(bilangan):
    print(f"{bilangan} adalah bilangan prima.")
else:
    print(f"{bilangan} bukan bilangan prima.")
