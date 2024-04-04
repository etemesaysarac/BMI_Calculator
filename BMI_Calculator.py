from tkinter import *
import math

window = Tk()
window.title('BMI_Calculator')
#window.iconbitmap('logo_1.ico')
window.minsize(600, 600)
window.config(padx=20, pady=20)

label = Label(window, text='Enter your Weight(kg)')
label.pack()
entry_weight = Entry()
entry_weight.focus()
entry_weight.pack()


label1 = Label(window, text='Enter your Height(cm)')
label1.pack()
entry_height = Entry()
entry_height.pack()

def button_clicked():
    print('Button Clicked...')

    try:
        b = int(entry_height.get())
        a = int(entry_weight.get())
    except:
        answer.config(text='Please write a number here!')

    BKI = (a/((b*b)*0.01**2))
    if BKI < 18.5:
        label3 = Label(window,text='According to Your Data: \nHeight = {}, Weight = {} ve BKI = {}'.format(b,a, BKI))
        answer.config(text='Thin')
        label3.pack()

    elif BKI > 18.5 and BKI < 25:
        label4 = Label(window,text='According to Your Data: \nHeight = {}, Weight = {} ve BKI = {}'.format(b,a, BKI))
        answer.config(text='Normal')
        label4.pack()
    elif BKI > 25 and BKI < 30:
        label5 = Label(window,text='According to Your Data: \nHeight = {}, Weight = {} ve BKI = {}'.format(b,a, BKI))
        answer.config(text='Over Weight!')
        label5.pack()
    elif BKI > 30:
        label6 = Label(window,text='According to Your Data: \nHeight = {}, Weight = {} ve BKI = {}'.format(b,a, BKI))
        answer.config(text='Go to Doctor!!!')
        label6.pack()
button1 = Button(text='Calculate', command=button_clicked)
button1.pack()

answer = Label(window, text='',font=('Arial',30,'bold'))
answer.pack()

window.mainloop()
