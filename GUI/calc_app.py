from tkinter import *

window = Tk()
window.geometry('300x300')
window.title('Basic Calc')

text_Box = Entry(window, width=25, justify='right', font=(14))
text_Box.grid(row=0, columnspan=4, padx=10, pady=10)

buttons = [
    ['c', 'del', '%', '='],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '/'],
    ['1', '2', '3', '-'],
    ['.', '0', 'e', '+']
]

def calculate(event):
    # print(event.widget.cget('text'))
    value = event.widget.cget('text')

    if value == '=':
        expression = text_Box.get()
        result = eval(expression)
        text_Box.delete(0, END)
        text_Box.insert(0, result)
        # print(result)
    else:
        length = len(text_Box.get())
        text_Box.insert(length,value)

buttons_dict = {}
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        current_btn = 'btn_{}'.format(buttons[i][j])
        btn = Button(window, text=buttons[i][j], font=(14),
                     width=5, bg='red', fg='white')
        buttons_dict[current_btn] = btn
        buttons_dict[current_btn].grid(row=i + 1, column=j,
                                       padx=5, pady=5)

        buttons_dict[current_btn].bind('<Button-1>', calculate)

window.mainloop()
