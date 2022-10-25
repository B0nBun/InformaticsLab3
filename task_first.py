import re
from testing import run_tests


"""
Вариант 513
Эмодзи: [<|
"""


def count_emojis(test_string: str):
    emoji_regex = r"\[\s*<\s*\|"
    return len(re.findall(emoji_regex, test_string))


def test():
    tests = [
        ("[<{|[<[<|", 1),
        ("][<||[<|[<||", 3),
        ("[<|:-([<|;<]<|[<|", 3),
        ("[  < |     <|   [< |    [<", 2),
        ("[<<| [<.| [*<|  [|   [|<", 0),
    ]

    run_tests(tests, count_emojis)


def test_input():
    in_string = input("Input string: ")
    print()
    print("Found", count_emojis(in_string), "entries in string")


if __name__ == "__main__":
    run_tests()
    test_input()
