# # import modul2 as m2
# # import ConcpectModul as m1
# # from modul2 import say_hi as s_h
# # import sys
# from dis import dis
# # import tkinter
#
#
# # если раскоментить вместо say_hi as s_h будет эта функция
# # def s_h():
# #     print('Я из модуля 1')
# def func():
#     print(f'привет! я из модуля 1')
#     # m2.say_hi()
#     # m1.func()
#     # m2.say_hi()
#     # m2.main()
#     print('Hi')
#     a = 'Hi'
#     return a
#     # print(m2.__name__)
#     # s_h()
#
# #
# # for path in sys.path:
# #     print(path)
#
# dis(func())
#

def hello(name):
    print(f'Hello {name}')