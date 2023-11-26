def unique_characters(input_string):
    unique_chars = []
    for char in input_string:
        if char not in unique_chars and char != ' ':  # Tekrar eden karakterleri ve boşlukları hariç tutar
            unique_chars.append(char)
    return unique_chars

# Örnek metin
text = "merhaba dunya"

# Benzersiz karakterleri bulma
result = unique_characters(text)

# Sonucu listeleme
print("Benzersiz karakterler:", result)
