import string

def remove_punctuation(text):
    # List semua tanda baca yang ingin dihapus
    punctuation_chars = string.punctuation
    
    # Buat dictionary untuk translate
    translator = str.maketrans('', '', punctuation_chars)
    
    # Menghapus tanda baca menggunakan translate
    text_cleaned = text.translate(translator)
    
    return text_cleaned

def remove_punctuation_regex(text):
    # Menggunakan regular expression untuk menghapus tanda baca
    import re
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

def main():
    # Contoh teks yang akan dihilangkan tanda bacanya
    input_text = "Halo, apa kabar? Saya baik-baik saja! 12345.6789"

    # Menggunakan metode tanpa regular expression
    text_cleaned = remove_punctuation(input_text)
    print("Teks tanpa tanda baca (tanpa regex):")
    print(text_cleaned)

    print()

    # Menggunakan metode dengan regular expression
    text_cleaned_regex = remove_punctuation_regex(input_text)
    print("Teks tanpa tanda baca (dengan regex):")
    print(text_cleaned_regex)

if __name__ == "__main__":
    main()
