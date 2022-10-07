from tkinter import *
from playsound import playsound
import random
from tkinter import messagebox, Label
from tkinter.ttk import *



def Slide():
    import time
    Progress_Bar['value']=20
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=50
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=80
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value']=100

def play():
    playsound("1.mp3")

def clicked():

    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u',
               'i', 'o', 'p', 'a', 's', 'd', 'f',
               'g', 'h', 'j', 'k', 'l', 'z', 'x',
               'c', 'v', 'b', 'n', 'm']
    res = txt.get()
    if (len(res)!=6):
        messagebox.showinfo(title='Ошибка', message='Введите 6-ти символьное слово')
    elif(not(str(res).isalpha())):
        messagebox.showinfo(title='Ошибка', message='Введите только буквы')
    else:
        code=''
        numbers = ''
        code += ''.join((random.choice(res)) for x in range(3)).upper()
        code += '-'
        for i in range(len(res)):
            if(ord(str(res[i]).upper())-64 >= 20):
                numbers += str(ord(str(res[i]).upper())-84)
            elif(ord(str(res[i]).upper())-64 >= 10):
                numbers += str(ord(str(res[i]).upper())-74)
            else:
                numbers += str(ord(str(res[i]).upper()) - 64)
        code += ''.join((random.choice(numbers)) for x in range(6))
        code += '-'
        code += ''.join((random.choice(res)) for x in range(3)).upper()
        Slide()

        play()
        messagebox.showinfo(title='Ваш ключ', message=code)




window = Tk()
window.title("Wellcom")
window.geometry('500x500')
window.image=PhotoImage(file='fz1.png')
bg_logo: Label=Label(window,image=window.image)
bg_logo.grid(row=0,column=0)

lbl = Label(window, text="Введите 6-ти символьное слово")
lbl.place(relx=.5, rely=.1, anchor="c")

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.place(relx=.5, rely=.2, anchor="c")
Progress_Bar=Progressbar(window,orient=HORIZONTAL,length=250,mode='determinate')
Progress_Bar.place(relx=.5, rely=.2, anchor="c")
Progress_Bar.grid(row=0,column=0)

btn = Button(window, text="Сгенерировать ключ", command=clicked)
btn.place(relx=.5, rely=.7, anchor="c")



# Button(window,text='Run',command=Slide).pack(pady=10)


window.mainloop()
