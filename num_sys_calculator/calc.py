from tkinter import *


def bol_to_mal(
    x,
):  # Функция по переводу большой цифры в маленькую - используется для красивого выведения степеней на экран
    if x == 0:
        return "⁰"
    a = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    s = ""
    while x > 0:
        d = x % 10
        x //= 10
        s += a[d]
    return s[::-1]


def dec_to_any(x, y):  # Функция по переводу из десятичной системы счисления в любую
    if x == 0:
        return "0"
    pvv4.insert(END, "\nПереводим из десятичной:")
    ost = 0
    a = []
    while x > 0:
        ost = x % y
        if ost > 9:
            a.append(chr(ord("A") + ost - 10))
            pvv4.insert(
                END,
                "\n"
                + str(x)
                + " % "
                + str(y)
                + " = "
                + str(ost)
                + "("
                + str(a[-1])
                + ")",
            )
            # print(x, ' % ', y, ' = ', ost, '(', a[-1], ')', sep='')
        else:
            a.append(str(ost))
            pvv4.insert(END, "\n" + str(x) + " % " + str(y) + " = " + str(ost))
            # print(x, '%', y, '=', ost)
        x //= y

    a.reverse()
    # print()
    return "".join(a)


def any_to_dec(x, y):  # Функция по переводу из любой системы счисления в десятичную
    a = 0
    pvv4.insert(END, "\nПереводим в десятичную:\n")
    for i in range(len(x)):
        if x[i].isnumeric():
            d = int(x[i])
        else:
            d = ord(x[i]) - ord("A") + 10
        pvv4.insert(END, str(d) + "·" + str(y) + str(bol_to_mal(len(x) - i - 1)))
        # print(pvv4.get(1.0, 1.5))
        # t1=(pvv4.get()).find('·')
        # pvv4.tag_add('title', '1.'+str(t1-1), '1.' + str(t1))
        # pvv4.tag_config('title', font=("Verdana", 24, 'bold'), justify=CENTER)
        # print(d,'·',y,bol_to_mal(len(x)-i-1), sep = '', end = '')
        if i == len(x) - 1:
            pvv4.insert(END, " = ")
            # print(' = ', end = '')
        else:
            pvv4.insert(END, " + ")
            # print(' + ', end = '')
        a += d * (y ** (len(x) - i - 1))
    pvv4.insert(END, str(a))
    # print(a)
    # print()
    return a


def result():
    pvv4["state"] = NORMAL
    pvv4.delete(1.0, END)
    f = (pvv1.get()).upper()
    ss_f = pvv2.get()
    a = [x for x in range(0, int(ss_f))]
    for i in range(len(a)):
        if a[i] > 9:
            a[i] = chr(ord("A") + i - 10)
        else:
            a[i] = str(a[i])
    error = False
    for dig in f:
        if dig not in a:
            pvv4.insert(1.0, "Ошибка ввода.")
            error = True
            break
    if error == False:
        ss_l = pvv3.get()
        if ss_l == ss_f:
            pvv4.insert(1.0, "Конечное число = " + f)
        elif ss_f == "10":
            pvv4.insert(1.0, "Конечное число = " + str(dec_to_any(int(f), int(ss_l))))
        elif ss_l == "10":
            pvv4.insert(1.0, "Конечное число = " + str(any_to_dec(str(f), int(ss_f))))
        else:
            pvv4.insert(
                1.0,
                "Конечное число = "
                + str(dec_to_any(any_to_dec(str(f), int(ss_f)), int(ss_l))),
            )
    pvv4["state"] = DISABLED


root = Tk()
root.title("Калькулятор систем счисления")
root.geometry("596x445")
root.resizable(False, False)


label1 = Label(text="Добро Пожаловать!", fg="#eee", bg="#333")
label2 = Label(bg="#D3D3D3")
text1 = Label(text="Начальное число:")
text2 = Label(text="Начальная система \nсчисления:")
text3 = Label(text="Конечная система \nсчисления:")
pvv1 = Entry(root, width=9)
pvv2 = Entry(root, width=9)
pvv3 = Entry(root, width=9)
pvv4 = Text(root, width=54, height=10, font="arial 14", wrap=WORD, state=DISABLED)
button1 = Button(text="Перевести!", fg="#eee", bg="#333", command=result)


label1.pack(fill=X)
label2.pack(expand=True, fill=BOTH)
text1.place(x=188, y=32, width=146)
text2.place(x=188, y=67, width=146)
text3.place(x=188, y=122, width=146)
pvv1.place(x=340, y=33)
pvv2.place(x=340, y=77)
pvv3.place(x=340, y=132)
pvv4.place(x=3, y=216)
button1.place(x=255, y=176)


root.mainloop()
