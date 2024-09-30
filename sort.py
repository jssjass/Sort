import random
import string

def generate_random_text(word_count=10):
    words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(word_count)]
    return ' '.join(words)

def get_input():
    return input("Введите текст или нажмите 'g' для генерации случайного текста: ")

def process_text(text):
    return sorted(text.split(), key=len)

def display_result(sorted_words):
    print("Отсортированные слова по возрастанию длины:")
    for word in sorted_words:
        print(word)

def main_menu():
    pass
