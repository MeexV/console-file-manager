import random


def game():
    person = {
        "А.С. Пушкин": "06.06.1799",
        "Джон фон Нейман": "28.12.1903",
        "А. Тьюринг": "23.06.1920",
        "А.П. Чехов": "29.01.1860",
        "Л.Н. Толстой": "09.09.1828",
        "Т. Эдисон": "11.02.1847",
        "Микеланджело": "06.03.1475",
        "В.М. Васницов": "15.05.1848",
        "Н.В.Гоголь": "01.04.1809",
        "М.Ю.Лермонтов": "15.10.1814"
    }

    data = {
        "06.06.1799": "шестое июня 1799 года",
        "28.12.1903": "двадцать восьмое декабря 1903 года",
        "23.06.1920": "двадцать третье июня 1920 года",
        "29.01.1860": "двадцать девятое января 1860 года",
        "09.09.1828": "девятое сентября 1828 года",
        "11.02.1847": "одинадцатое февраля 1847 года",
        "06.03.1475": "шестое марта 1475 года",
        "15.05.1848": "пятнадцатое мая 1848 года",
        "01.04.1809": "первое апреля 1809 года",
        "15.10.1814": "пятнадцатое октября 1814 года"
    }
    person_sample = random.sample(list(person.keys()), 5)
    k = 0
    ans = "да"

    while ans == "да":
        for i in person_sample:
            year_1_input = input(f"Введите год рождения {i}: ")

            if year_1_input == person[i]:
                k += 1
            else:
                print(data[person[i]])

        print(f"Количество правильный ответов: {k}")
        print(f"Количество ошибок: {5 - k}")

        k = 0
        ans = input("Хотите начать сначала (да/нет): ")
