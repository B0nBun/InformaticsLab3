import re
from testing import run_tests


"""
Вариант 5
С помощью регулярного выражения найти в тексте все слова, в которых две гласные
стоят подряд, а после этого слова идёт слово, в котором не больше 3 согласных.
"""


cyrillic = "[ёЁа-яА-Я]"
vowels_lower = "ёуеыаоэяию"
consonants_lower = "йцкнгшщзхъфвпрлджчсмтьб"
vowels = vowels_lower + vowels_lower.upper()
consonants = consonants_lower + consonants_lower.upper()


def search(string: str) -> str:
    regex = rf"\b({cyrillic}*[{vowels}]{{2}}{cyrillic}*)\b([^{consonants}\b]*[{consonants}][^{consonants}\b]*){{1,3}}\b"
    return list(map(lambda tpl: tpl[0], re.findall(regex, string)))


def test():
    tests = [
        ("Кривошеее существо гуляет по парку", ["гуляет"]),
        (
            "Тогда Цинциннат брал себя в руки и, прижав к груди, относил в безопасное место.",
            ["безопасное"],
        ),
        (
            "Адвокат, сторонник классической декапитации, выиграл без труда против затейника прокурора, и судья синтезировал дело.",
            ["выиграл"],
        ),
        (
            "Супругу свою до того уважал и до того иногда боялся её, что даже любил",
            ["свою", "боялся"],
        ),
        ("В такую погоду хорошо повеситься…", ["такую"]),
        (
            "Вам дороги интересы народа и России, и потому вы ненавидите народ, так как в каждом подозреваете вора и грабителя",
            ["России", "подозреваете"],
        ),
    ]

    run_tests(tests, search)


def test_input():
    in_string = input("Input string: ")
    print()
    print("Found:", search(in_string))


if __name__ == "__main__":
    test()
    test_input()
