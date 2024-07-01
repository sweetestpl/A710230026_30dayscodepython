# Definisikan kelas Contact untuk merepresentasikan kontak
class Contact:
    def __init__(self, nama, email, telepon):
        self.nama = nama
        self.email = email
        self.telepon = telepon

    def __str__(self):
        return f"Nama: {self.nama}, Email: {self.email}, Telepon: {self.telepon}"

# Fungsi untuk menyimpan kontak ke dalam file
def simpan_kontak(contacts):
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            file.write(f"{contact.nama},{contact.email},{contact.telepon}\n")

# Fungsi untuk membaca kontak dari file
def baca_kontak():
    contacts = []
    try:
        with open('contacts.txt', 'r') as file:
            for line in file:
                nama, email, telepon = line.strip().split(',')
                contacts.append(Contact(nama, email, telepon))
    except FileNotFoundError:
        print("File kontak tidak ditemukan. Akan membuat file baru saat menyimpan kontak pertama kali.")
    return contacts

# Fungsi untuk menampilkan semua kontak
def tampilkan_kontak(contacts):
    if not contacts:
        print("Belum ada kontak tersimpan.")
    else:
        for contact in contacts:
            print(contact)

# Fungsi untuk menambahkan kontak baru
def tambah_kontak(contacts):
    print("\nMasukkan informasi kontak baru:")
    nama = input("Nama: ")
    email = input("Email: ")
    telepon = input("Telepon: ")
    contacts.append(Contact(nama, email, telepon))
    simpan_kontak(contacts)
    print(f"Kontak {nama} telah ditambahkan.\n")

# Fungsi untuk mencari kontak berdasarkan nama
def cari_kontak(contacts):
    nama_cari = input("Masukkan nama yang ingin dicari: ")
    found = False
    for contact in contacts:
        if contact.nama.lower() == nama_cari.lower():
            print(contact)
            found = True
    if not found:
        print(f"Kontak dengan nama '{nama_cari}' tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    contacts = baca_kontak()
    
    while True:
        print("\n===== Aplikasi Kontak =====")
        print("1. Tampilkan semua kontak")
        print("2. Tambah kontak baru")
        print("3. Cari kontak berdasarkan nama")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            tampilkan_kontak(contacts)
        elif pilihan == '2':
            tambah_kontak(contacts)
        elif pilihan == '3':
            cari_kontak(contacts)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan Aplikasi Kontak.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

if __name__ == '__main__':
    main()
