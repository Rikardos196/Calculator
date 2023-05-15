from tkinter import *
from functools import partial

num = ''
num1 = ''
action = ''  # оператор
flag = True  # флаг проверяющий


def click_num(a):
    global num, flag
    if not flag:
        num = ''
        text1.configure(text=num)
    num += str(a)
    text1.configure(text=num)
    flag = True


def click_clear():
    global num
    num = ''
    text1.configure(text='')


def click_all_clear():
    global num, num1, action
    num, num1, action = '', '', ''
    text1.configure(text='')


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
        if action == '+':
            num1 = str(float(num1) + float(num))
        elif action == '-':
            num1 = str(float(num1) - float(num))
        elif action == '/':
            num1 = str(float(num1) / float(num))
        else:
            num1 = str(float(num1) * float(num))
        if int(num1[num1.find('.') + 1:]) == 0:
            num1 = num1[:num1.find('.')]
        num = ''
        action = a
    text1.configure(text=num1)


def click_equally():
    global num, num1, action, flag
    if num1 == '':
        return
    if action == '+':
        num1 = str(float(num1) + float(num))
    elif action == '-':
        num1 = str(float(num1) - float(num))
    elif action == '/':
        num1 = str(float(num1) / float(num))
    else:
        num1 = str(float(num1) * float(num))
    if int(num1[num1.find('.') + 1:]) == 0:
        num1 = num1[:num1.find('.')]
    text1.configure(text=num1)
    num = num1
    action = ''
    flag = False


window = Tk()
window.title("Калькулятор")
window.geometry('268x380')
window.resizable(False, False)
text1 = Label(window, text='0', width=13, height=1, font=("Arial Black", 20), bg="white", fg="brown",
              state="disabled")
# lbl = Label(window, text="", font=("Tahoma", 16))
text1.grid(columnspan=4, row=0)
button1 = Button(window, text="1", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_num, 1))
button1.grid(column=0, row=1)
button2 = Button(window, text="2", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_num, 2))
button2.grid(column=1, row=1)
button3 = Button(window, text="3", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_num, 3))
button3.grid(column=2, row=1)
button4 = Button(window, text="+", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_operation, '+'))
button4.grid(column=3, row=1)
button5 = Button(window, text="4", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_num, 4))
button5.grid(column=0, row=2)
button6 = Button(window, text="5", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_num, 5))
button6.grid(column=1, row=2)
button7 = Button(window, text="6", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_num, 6))
button7.grid(column=2, row=2)
button8 = Button(window, text="-", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_operation, '-'))
button8.grid(column=3, row=2)
button9 = Button(window, text="7", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                 command=partial(click_num, 7))
button9.grid(column=0, row=3)
button10 = Button(window, text="8", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=partial(click_num, 8))
button10.grid(column=1, row=3)
button11 = Button(window, text="9", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=partial(click_num, 9))
button11.grid(column=2, row=3)
button12 = Button(window, text="*", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=partial(click_operation, '*'))
button12.grid(column=3, row=3)
button13 = Button(window, text="C", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=click_all_clear)
button13.grid(column=0, row=4)
button14 = Button(window, text="0", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=partial(click_num, 0))
button14.grid(column=1, row=4)
button15 = Button(window, text=",", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=click_point)
button15.grid(column=2, row=4)
button16 = Button(window, text="/", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=partial(click_operation, '/'))
button16.grid(column=3, row=4)
button17 = Button(window, text="CE", width=3, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=click_clear)
button17.grid(column=0, row=5)
button18 = Button(window, text="=", width=10, height=1, font=("Arial Black", 20), bg="brown", fg="white",
                  command=click_equally)
button18.grid(column=1, columnspan=3, row=5)
window.mainloop()
