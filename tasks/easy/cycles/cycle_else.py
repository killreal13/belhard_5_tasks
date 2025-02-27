"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая принимает значение для range и в которой работает
цикл, увеличивающий счетчик.

Если значение счетчика станет равно 7, то выполнить break.
Если цикл завершился без break, то вернуть -5

ПРИМЕРЫ
--------------------------------------------------------------------------------
lets_else(4) -> -5
lets_else(10) -> 7
"""


def lets_else(range_val: int) -> int:
    for counter in range(range_val):
        if counter == 7:
            break
    else:
        return -5
    return counter


if __name__ == '__main__':
    assert lets_else(5) == -5
    assert lets_else(8) == 7
    print('Решено!')
