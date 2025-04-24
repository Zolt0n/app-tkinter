from tkinter import *
from tkinter import ttk
import re
from currency_converter import CurrencyConverter

c = CurrencyConverter()
sm = 0
label_sm = ''

'''Создание окна'''
window = Tk()
window.title('Конвертёр валюты')
window.geometry('700x500+400+200')

'''Обработка ввода'''


def entry_handler(new_val):
    return re.match("^\d{0,8}$", new_val) is not None


'''Удаление ошибки'''


def delete_label(event):
    entry.delete(0, END)
    label_error['text'] = ''


'''Обработка введения суммы'''


def enter():
    global sm, label_sm
    sm = entry.get().lstrip('0')
    if sm == '':
        label_error['text'] = 'Похоже, вы не ввели сумму\nПопробуйте снова'
        label_error.pack()
        entry.bind('<ButtonPress-1>', delete_label)
    else:
        entry.unbind('<ButtonPress-1>')
        entry['state'] = ['disabled']
        btn_enter['state'] = ['disabled']
        label_sm = ttk.Label()
        label_sm.place(x=285, y=300)


'''Cмена суммы'''


def change():
    global label_sm
    entry.delete(0, END)
    btn_enter['state'] = 'abled'
    entry['state'] = 'abled'
    entry.delete(0, END)
    label_sm['text'] = ''


'''Обработка самой суммы (кнопки валют)'''


def btn_convert_re():
    global sm
    total = c.convert(sm, 'RUB', 'EUR')
    label_sm['text'] = f'Ваша итоговая сумма: {round(total, 2)}'


def btn_convert_ru():
    global sm
    total = c.convert(sm, 'RUB', 'USD')
    label_sm['text'] = f'Ваша итоговая сумма: {round(total, 2)}'


def btn_convert_ue():
    global sm, label_sm
    total = c.convert(sm, 'USD', 'EUR')
    label_sm['text'] = f'Ваша итоговая сумма: {round(total, 2)}'


def btn_convert_eu():
    global sm, label_sm
    total = c.convert(sm, 'EUR', 'USD')
    label_sm['text'] = f'Ваша итоговая сумма: {round(total, 2)}'


'''Приветствие'''
label_greetings = ttk.Label(text='Привет! Это конвертёр валюты.'
                                 '\nВведи суммму, которую хочешь конвертировать,'
                                 '\nа также пару валют', font=('Arial', 18))
label_greetings.pack()

'''Создание строки ввода'''
check = (window.register(entry_handler), "%P")
entry = ttk.Entry(validate='key', validatecommand=check)
entry.pack(anchor='center', pady=30)

'''Создание кнопок'''
btn_enter = ttk.Button(text='Enter', command=enter)
btn_enter.pack()
btn_change = ttk.Button(text='Change amount', command=change)
btn_change.pack()
btn1 = ttk.Button(text='RUB/EUR', command=btn_convert_re)
btn2 = ttk.Button(text='RUB/USD', command=btn_convert_ru)
btn3 = ttk.Button(text='USD/EUR', command=btn_convert_ue)
btn4 = ttk.Button(text='EUR/USD', command=btn_convert_eu)
btn1.place(x=250, y=235)
btn2.place(x=250, y=270)
btn3.place(x=380, y=235)
btn4.place(x=380, y=270)
'''Вывод ошибки'''
label_error = ttk.Label()

window.mainloop()
