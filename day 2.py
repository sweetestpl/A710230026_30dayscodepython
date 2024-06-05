def minta_input():
  """
  Meminta input bilangan bulat dari pengguna.
  Jika input tidak valid, meminta ulang hingga valid.
  """
  while True:
      try:
          angka = int(input("Masukkan bilangan bulat: "))
          return angka
      except ValueError:
          print("Input yang dimasukkan tidak valid! Silakan masukkan bilangan bulat.")

def hitung_kuadrat(angka):
  """
  Menghitung pangkat dua dari bilangan bulat yang diberikan.
  """
  return angka ** 2

def main():
  """
  Fungsi utama yang menjalankan program.
  """
  jumlah_input = 5  # Jumlah input yang diminta dari pengguna
  hasil_kuadrat = []

  for i in range(jumlah_input):
      print(f"Input ke-{i+1}")
      angka = minta_input()
      kuadrat = hitung_kuadrat(angka)
      hasil_kuadrat.append((angka, kuadrat))
      print(f"Hasil pangkat dua dari {angka} adalah {kuadrat}\n")

  print("Ringkasan Hasil:")
  for angka, kuadrat in hasil_kuadrat:
      print(f"{angka} -> {kuadrat}")

if _name_ == "_main_":