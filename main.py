import tkinter
from tkinter import *
from functools import partial
import math


num = ''
num1 = ''
action = ''  # оператор
flag = True  # флаг проверяющий
text1 = []

'''
num = 1906402368640
num1 = 0.00000000256000000000002
num2 = 999999.099999999999
num3 = 124567895151.03
num4 = 1.23456890598752352
num5 = 0.00025964123326541
num6 = 19439124912958158159519258.31234
num7 = 2469612491295815

num_array = [num, num1, num2, num3, num4, num5, num6, num7]
num_array_answer = [1906402368640, '2.5600000e-09', 999999.1, 124567895151, 1.23456890599,
                    '0.00025964123', '1.9439124e+25', '2.4696124e+15']
'''


def get_num(a):
    text_num = str(a)
    if 'e' in text_num:
        text_num = text_num[:9]+text_num[-4:]
        return text_num
    if len(text_num) <= 13:
        return text_num
    if len(text_num) > 13:
        if '.' in text_num:
            if '.' in text_num[:12]:
                text_num = text_num[0:11] + str(round(float(text_num[11:])/(10**(len(text_num[12:]))), 1)*10)[:-2]
                text_num = str(float(text_num))
                return text_num
            elif text_num.find('.') == 12:
                text_num = text_num[:12]
                return text_num
            else:
                point_index = text_num.find('.')
                text_num1 = text_num[0] + '.' + text_num[1:point_index] + text_num[point_index + 1:]
        else:
            text_num1 = text_num[0] + '.' + text_num[1:]
        power = math.log10(float(text_num)/(float(text_num1)))
        text_num = text_num1[0:9] + f'e+{power}'
        return text_num[:-2]


def get_test(a, b):
    for i in range(len(a)):
        if get_num(a[i]) == str(b[i]):
            print(f'Тест №{i+1} пройден успешно')
        else:
            print(f'Тест №{i + 1} не пройден')


def kill_null(a):
    count_null = 0
    flag_kill_null = True
    for i in range(1, len(a)):
        if a[-i] == '0' and flag_kill_null:
            count_null += 1
        else:
            flag_kill_null = False
    if count_null != 0:
        a = a[:-count_null]
    return a


def click_num(a):
    global num, flag
    if not flag:
        num = ''
        text1.configure(text=get_num(num))
    if num == '0':
        num = str(a)
    else:
        num += str(a)
    text1.configure(text=get_num(num))
    flag = True


def click_clear():
    global num
    num = ''
    text1.configure(text='0')


def click_all_clear():
    global num, num1, action
    num, num1, action = '', '', ''
    text1.configure(text='0')


def click_point():
    global num
    if len(num) == 0:
        num += '0'
    if num.count('.') == 0:
        num += '.'
        text1.configure(text=num)


def click_operation(a):
    global num, num1, action
    if action == '':
        action = a
        num1 = num
        num = ''
    else:
        if num == '':
            action = ''
        if action == '+':
            num1 = str(float(num1) + float(num))
        elif action == '-':
            num1 = str(float(num1) - float(num))
        elif action == '/':
            if float(num) == 0:
                num1 = '0'
            else:
                num1 = str(float(num1) / float(num))
        elif action == '*':
            num1 = str(float(num1) * float(num))
        if '.' in num1 and 'e' not in num1:
            num1 = kill_null(str(num1))
            if num1[-1] == '.':
                num1 = num1[:-1]
        num = ''
        action = a
    text1.configure(text=get_num(num1))


def click_equally():
    global num, num1, action, flag
    if num1 == '':
        return
    if num == '':
        num = '0'
    if action == '+':
        num1 = str(float(num1) + float(num))
    elif action == '-':
        num1 = str(float(num1) - float(num))
    elif action == '/':
        if float(num) == 0:
            num1 = '0.0'
        else:
            num1 = str(float(num1) / float(num))
    elif action == '*':
        num1 = str(float(num1) * float(num))
    if '.' in num1 and 'e' not in num1:
        num1 = kill_null(str(num1))
        if num1[-1] == '.':
            num1 = num1[:-1]
    text1.configure(text=get_num(num1))
    num = num1
    action = ''
    flag = False


def back_line():
    global num
    if len(num) > 1:
        num = num[:-1]
        text1.configure(text=get_num(num))
    elif len(num) == 1:
        num = '0'
        text1.configure(text=get_num(num))


def click_event_1(event):
    click_num(1)


def click_event_2(event):
    click_num(2)


def click_event_3(event):
    click_num(3)


def click_event_4(event):
    click_num(4)


def click_event_5(event):
    click_num(5)


def click_event_6(event):
    click_num(6)


def click_event_7(event):
    click_num(7)


def click_event_8(event):
    click_num(8)


def click_event_9(event):
    click_num(9)


def click_event_0(event):
    click_num(0)


def click_event_plus(event):
    click_operation('+')


def click_event_minus(event):
    click_operation('-')


def click_event_division(event):
    click_operation('/')


def click_event_multiplication(event):
    click_operation('*')


def click_event_point(event):
    click_point()


def click_event_back(event):
    back_line()


def click_event_equal(event):
    click_equally()

def main():
    global text1

    window = Tk()
    window.title("Calc")
    window.geometry('232x350')
    window.iconbitmap('favicon.ico')
    window.resizable(True, True)

    virtualPix = tkinter.PhotoImage(width=1, height=1)

    text1 = Label(window, text='0', image=virtualPix, width=222, height=53, compound="center",
                  font=('Arial', 20),
                  bg='brown', bd=4, foreground='white', relief=RIDGE)
    text1.grid(columnspan=4, row=0)

    button1 = Button(window, text="1", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_num, 1))
    button1.grid(column=0, row=1)

    button2 = Button(window, text="2", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_num, 2))
    button2.grid(column=1, row=1)

    button3 = Button(window, text="3", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_num, 3))
    button3.grid(column=2, row=1)

    button4 = Button(window, text="+", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_operation, '+'))
    button4.grid(column=3, row=1)

    button5 = Button(window, text="4", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_num, 4))
    button5.grid(column=0, row=2)

    button6 = Button(window, text="5", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_num, 5))
    button6.grid(column=1, row=2)

    button7 = Button(window, text="6", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_num, 6))
    button7.grid(column=2, row=2)

    button8 = Button(window, text="-", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                     bg="brown", fg="white", command=partial(click_operation, '-'))
    button8.grid(column=3, row=2)

    button9 = Button(window, text="7", image=virtualPix, width=50, height=50, compound="center",  font=("", 20),
                     bg="brown", fg="white", command=partial(click_num, 7))
    button9.grid(column=0, row=3)

    button10 = Button(window, text="8", image=virtualPix, width=50, height=50, compound="center",  font=("", 20),
                      bg="brown", fg="white", command=partial(click_num, 8))
    button10.grid(column=1, row=3)

    button11 = Button(window, text="9", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=partial(click_num, 9))
    button11.grid(column=2, row=3)

    button12 = Button(window, text="*", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=partial(click_operation, '*'))
    button12.grid(column=3, row=3)

    button13 = Button(window, text="C", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=click_all_clear)
    button13.grid(column=0, row=4)

    button14 = Button(window, text="0", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=partial(click_num, 0))
    button14.grid(column=1, row=4)

    button15 = Button(window, text=",", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=click_point)
    button15.grid(column=2, row=4)

    button16 = Button(window, text="/", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=partial(click_operation, '/'))
    button16.grid(column=3, row=4)

    button17 = Button(window, text="CE", image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=click_clear)
    button17.grid(column=0,  row=5)

    button18 = Button(window, text="=", image=virtualPix, width=108, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=click_equally)
    button18.grid(column=1, columnspan=2, row=5)

    button19 = Button(window, text=u'\u2190', image=virtualPix, width=50, height=50, compound="center", font=("", 20),
                      bg="brown", fg="white", command=back_line)
    button19.grid(column=3, row=5)


    window.bind('1', click_event_1)
    window.bind("2", click_event_2)
    window.bind('3', click_event_3)
    window.bind('4', click_event_4)
    window.bind("5", click_event_5)
    window.bind('6', click_event_6)
    window.bind("7", click_event_7)
    window.bind('8', click_event_8)
    window.bind("9", click_event_9)
    window.bind('0', click_event_0)
    window.bind("-", click_event_minus)
    window.bind('*', click_event_multiplication)
    window.bind("/", click_event_division)
    window.bind('+', click_event_plus)
    window.bind('.', click_event_point)
    window.bind("=", click_event_equal)
    window.bind("<Return>", click_event_equal)
    window.bind('<BackSpace>', click_event_back)
    window.mainloop()


if __name__ == '__main__':
    main()