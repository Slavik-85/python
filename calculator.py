from tkinter import *

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equalpress():
    try:

        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:

        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="#282424")

    gui.title("Simple Calculator")

    gui.geometry("390x310")

    equation = StringVar()

    expression_field = Entry(gui, textvariable=equation, bg="#282424", fg="white")


    expression_field.grid(columnspan=100, ipadx=1000)

    button1 = Button(gui, text=' 1 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(1), height=3, width=10)
    button1.grid(row=5, column=0)

    button2 = Button(gui, text=' 2 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(2), height=3, width=10)
    button2.grid(row=5, column=1)

    button3 = Button(gui, text=' 3 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(3), height=3, width=10)
    button3.grid(row=5, column=2)

    button4 = Button(gui, text=' 4 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(4), height=3, width=10)
    button4.grid(row=6, column=0)

    button5 = Button(gui, text=' 5 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(5), height=3, width=10)
    button5.grid(row=6, column=1)

    button6 = Button(gui, text=' 6 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(6), height=3, width=10)
    button6.grid(row=6, column=2)

    button7 = Button(gui, text=' 7 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(7), height=3, width=10)
    button7.grid(row=7, column=0)

    button8 = Button(gui, text=' 8 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(8), height=3, width=10)
    button8.grid(row=7, column=1)

    button9 = Button(gui, text=' 9 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(9), height=3, width=10)
    button9.grid(row=7, column=2)

    button0 = Button(gui, text=' 0 ', fg='white', bg='#3b3b3b',
                     command=lambda: press(0), height=3, width=10)
    button0.grid(row=8, column=0)

    plus = Button(gui, text=' + ', fg='white', bg='#383434',
                  command=lambda: press("+"), height=3, width=10)
    plus.grid(row=5, column=3)

    minus = Button(gui, text=' - ', fg='white', bg='#383434',
                   command=lambda: press("-"), height=3, width=10)
    minus.grid(row=6, column=3)

    multiply = Button(gui, text=' * ', fg='white', bg='#383434',
                      command=lambda: press("*"), height=3, width=10)
    multiply.grid(row=7, column=3)

    divide = Button(gui, text=' / ', fg='white', bg='#383434',
                    command=lambda: press("/"), height=3, width=10)
    divide.grid(row=8, column=3)

    equal = Button(gui, text=' = ', fg='white', bg='#383434',
                   command=equalpress, height=3, width=10)
    equal.grid(row=8, column=2)

    clear = Button(gui, text='Clear', fg='white', bg='#383434',
                   command=clear, height=3, width=10)
    clear.grid(row=8, column=1)

    Decimal = Button(gui, text='.', fg='white', bg='#3b3b3b',
                     command=lambda: press('.'), height=3, width=10)
    Decimal.grid(row=9, column=0)
    gui.mainloop()