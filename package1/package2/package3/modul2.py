# def say_hi():
#     print(f'ПРИВЕТ! Я ИЗ МОДУЛЯ 2')
#     from random import randint
#     print(randint(1,10))
#
# def main():
#     a = 5
#     b = 10
#     print(a, b)
#
#
# if __name__ == '__main__' :
#     main()
# . - тек. директория
from .modul1 import hello


def good_word(name):
    hello(name)
    print(f'IOU {name}')


if __name__ == '__main__':
    good_word('Urban')
