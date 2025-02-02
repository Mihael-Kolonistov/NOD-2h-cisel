from tkinter import *
from logic import formul1, formul2 
root = Tk()
root.title('Расчет НОД 2-х чисел')
root.resizable(0,0)

var = StringVar(root)
var.set("Евклид")


otv, sch=0.0, 0.0

def mode_choice():
    global otv, sch, l, var
    print(var.get())
    if var.get() == 'Евклид':
        ans_cort=formul1(int(t1.get()), int(t2.get()))
    elif var.get() == 'Евклид улучшенная':
        ans_cort=formul2(int(t1.get()),int(t2.get()))
    else:
        ans_cort=('Ошибка!','Ошибка!')
    otv, sch =  ans_cort
    l['text']=f'НОД из {str(t1.get())} и {str(t2.get())} = {otv} | Циклов выполнено: {sch}'


tf=LabelFrame(root)

t1=Entry(tf, width=30, font=('Comic Sans', 20))
t2=Entry(tf, width=30, font=('Comic Sans', 20))

bf=LabelFrame(root)
b=Button(bf, text='Считать',  font=('Comic Sans', 20), width=50, command=mode_choice)

mode=OptionMenu(bf, var, "Евклид", "Евклид улучшенная")

l=Label(root, text=f'НОД из {t1.get()} и {t2.get()} = {otv} | Циклов выполнено: {sch}' )

tf.grid(column=0, row=0, padx=5, pady=5)

t1.grid(column=0, row=0, padx=5, pady=5)
t2.grid(column=1, row=0, padx=5, pady=5)

bf.grid(column=0, row=1, padx=5, pady=5)
b.grid(column=0, row=0, padx=5, pady=5)
mode.grid(column=1, row=0, padx=5, pady=5)

l.grid(column=0, row=2, padx=5, pady=5)

root.mainloop()