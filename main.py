'LAB_6'
def p1():
    countries_dict = {'Австрия': 'Вена', 'Россия': 'Москва', 'Франция': 'Париж', 'Великобритания': 'Лондон',
                      'США': 'Вашингтон', 'Португалия': 'Лиссабон', 'Чехия': 'Прага', 'Германия': 'Берлин'}
    print(countries_dict, '\n')
    for key in sorted(countries_dict):
        print(key, " — ", countries_dict[key])

def p2():
    alphabet = {
        "а": 1,
        "б": 3,
        "в": 1,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3,
        " ": 0,
        "-": 1.5,
        "—": 1.5
    }
    x = input('Введите слово: ')
    x = x.lower()
    s = 0
    for i in x:
        s += alphabet[i]
    print('Ценность слова = ', s)

def p3():
    import random

    students = {"Иванова", "Козлов", "Щеглова", "Романов", "Петрова", "Кузнецов", "Киселёв", "Давыдова", "Лебедев",
                "Семенова"}
    languages = {"Русский", "Английский", "Французский", "Немецкий", "Китайский"}

    lang_stud = {}

    for st in students:
        kolvo = random.randint(1, 3)
        lang_stud[st] = random.sample(list(languages), kolvo)

    unique_lang = set()
    for i in lang_stud:
        unique_lang = unique_lang.union(set(lang_stud[i]))
    sorted(unique_lang)
    unique_lang_fix = ', '.join(unique_lang)
    # print(lang_stud)
    print("Множество различных языков, которые знают студенты: ", unique_lang_fix, f" ({len(unique_lang)})")

    china = [i for i in lang_stud if "Китайский" in lang_stud[i]]
    china_fix = ', '.join(china)
    print("Студенты, знающие китайский: ", china_fix)

p1(), p2(), p3()




