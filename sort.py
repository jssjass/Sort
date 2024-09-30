import random
import string

# Функция для генерации случайного текста
def generate_random_text(word_count=10):
    # Генерируем список случайных слов
    words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8))) for _ in range(word_count)]
    return ' '.join(words)

# Функция для получения ввода от пользователя
def get_input():
    return input("Введите текст или нажмите 'g' для генерации случайного текста: ")

# Функция для обработки текста: разбиваем на слова и сортируем по длине
def process_text(text):
    # Разделяем текст на слова, используя пробелы и знаки препинания
    words = text.split()
    # Убираем знаки препинания и сортируем слова по длине
    cleaned_words = [''.join(filter(str.isalnum, word)) for word in words]
    return sorted(cleaned_words, key=len)

# Функция для вывода результата на экран
def display_result(sorted_words):
    print("Отсортированные слова по возрастанию длины:")
    for word in sorted_words:
        print(word)

# Главное меню программы
def main_menu():
    data = None  # Здесь будут храниться введенные данные
    sorted_words = None  # Здесь будут храниться отсортированные слова

    while True:
        print("\nМеню:")
        print("1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы программы")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            # Ввод данных пользователем
            user_input = get_input()
            if user_input.lower() == 'g':
                # Генерация случайного текста
                data = generate_random_text()
                print("Сгенерированный текст:", data)
            else:
                # Использование введенного текста
                data = user_input
            # Сбрасываем отсортированные слова, так как данные изменились
            sorted_words = None

        elif choice == '2':
            # Выполняем алгоритм по заданию, только если есть данные
            if data:
                sorted_words = process_text(data)
                print("Алгоритм выполнен.")
            else:
                print("Ошибка: сначала введите данные.")

        elif choice == '3':
            # Выводим результат, только если были выполнены обработка
            if sorted_words is not None:
                display_result(sorted_words)
            else:
                print("Ошибка: необходимо сначала выполнить алгоритм.")

        elif choice == '4':
            # Завершение работы программы
            print("Завершение работы программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите пункт меню от 1 до 4.")

# Запуск программы
if __name__ == "__main__":
    main_menu()
