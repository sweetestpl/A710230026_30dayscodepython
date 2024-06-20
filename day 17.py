import string

def cek_palindrom(kata):
    # Menghapus tanda baca dan mengubah ke huruf kecil
    kata = kata.lower()
    kata = ''.join(ch for ch in kata if ch not in string.punctuation)
    
    # Mengecek palindrom
    if kata == kata[::-1]:
        return True
    else:
        return False

# Membaca input dari pengguna
input_kata = input("Masukkan kata atau frase: ")

# Memisahkan input menjadi kata/frasa
list_kata = input_kata.split()

# Menggabungkan kembali jika ada lebih dari satu kata
if len(list_kata) > 1:
    input_kata = ''.join(list_kata)

# Memanggil fungsi untuk mengecek palindrom
if cek_palindrom(input_kata):
    print(f"'{input_kata}' adalah palindrom.")
else:
    print(f"'{input_kata}' bukan palindrom.")
