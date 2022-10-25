import re
from typing import List
from testing import run_tests


"""
Вариант 1
С помощью регулярного выражения найти в тексте слова, в которых встречается
строго одна гласная буква (встречаться она может несколько раз). Пример таких
слов: окно, трава, молоко, etc.После чего данные слова требуется отсортировать по увеличению длины слова.
"""


cyrillic = "[ёЁа-яА-Я]"
vowels_lower = "ёуеыаоэяию"
consonants_lower = "йцкнгшщзхъфвпрлджчсмтьб"
vowels = vowels_lower + vowels_lower.upper()
consonants = consonants_lower + consonants_lower.upper()


def one_unique_vowel(string: str) -> List[str]:
    regex = rf"\b([{consonants}]*([{vowels}])(\2|[{consonants}])*|[{vowels}])\b"
    return sorted(
        list(map(lambda tpl: tpl[0], re.findall(regex, string, flags=re.IGNORECASE))),
        key=len,
    )


def test():
    tests = [
        (
            (
                "Классное слово – обороноспособность,\n"
                "которое должно идти после слов: трава\n"
                "и молоко."
            ),
            [
                "и",
                "идти",
                "слов",
                "слово",
                "трава",
                "должно",
                "молоко",
                "обороноспособность",
            ],
        ),
        (
            "Как я могу убедить дикого утенка, живущего в неволе и ненавидящего меня, что он мне симпатичен и что я сочувствую его страданию?",
            ["я", "и", "и", "я", "он", "Как", "что", "мне", "что"],
        ),
        ("Ии ббб test 123 зараза колкость", ["Ии", "зараза", "колкость"]),
        ("Завтра приезжает вся его юность, его Россия.", ["вся", "Завтра"]),
        (
            "Россию надо любить. Без нашей эмигрантской любви России – крышка. Там ее никто не любит.",
            ["ее", "не", "Без", "Там"],
        ),
        ("Коллекция дурацких физиономий и замученных вещей.", ["и", "вещей"]),
    ]

    run_tests(tests, one_unique_vowel)


def test_input():
    in_string = input("Input string: ")
    print()
    print("Found:", one_unique_vowel(in_string))


if __name__ == "__main__":
    test()
    test_input()
