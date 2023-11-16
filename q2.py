def unicode_conversion(input_string):
    unicode_list = [ord(char) for char in input_string]
    return unicode_list

def find_longest_word(input_string):
    words = input_string.split()
    longest_word = max(words, key=len)
    return longest_word

# Ввод строки текста
user_input = input("Введите строку текста: ")

# Преобразование символов в Unicode-коды
unicode_list = unicode_conversion(user_input)
print(f"Unicode-коды символов: {unicode_list}")

# Поиск самого длинного слова
longest_word = find_longest_word(user_input)
print(f"Самое длинное слово: {longest_word}")