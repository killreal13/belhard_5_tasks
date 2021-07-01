"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая получает список с числами и возвращает список с
элементами, которые не кратны 3
"""


def not_3(array: list) -> list:
    result_array = []
    for i in range(len(array)):
        if not array[i] % 3 == 0:
            result_array.append(array[i])
    return result_array


if __name__ == '__main__':
    assert not_3([2, 1, 3, 5, 6, 4, 7]) == [2, 1, 5, 4, 7]
    print('Решено!')
