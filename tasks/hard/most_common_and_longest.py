"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""
import collections


def common_and_longest(text: str) -> tuple:
    common = collections.Counter(text.split(' ')).most_common(1)
    splited_text = text.split(' ')
    for i in range(len(text.split(' '))):
        if len(splited_text[0]) < len(splited_text[i]):
            splited_text[0], splited_text[i] = splited_text[i], splited_text[0]
            longest = splited_text[0]
    return common[0][0], longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
