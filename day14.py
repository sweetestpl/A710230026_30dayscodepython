def hitung_bmi(berat, tinggi_cm):
    
    tinggi_m = tinggi_cm / 100  # Konversi tinggi dari cm ke meter
    bmi = berat / (tinggi_m ** 2)
    return bmi

def kategori_bmi(bmi):
   
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

def main():
    try:
        berat = float(input("Masukkan berat badan Anda (kg): "))
        tinggi_cm = float(input("Masukkan tinggi badan Anda (cm): "))
        
        bmi = hitung_bmi(berat, tinggi_cm)
        kategori = kategori_bmi(bmi)
        
        print(f"BMI Anda adalah: {bmi:.2f}")
        print(f"Kategori BMI Anda adalah: {kategori}")
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka yang benar.")

if __name__ == "__main__":
    main()
