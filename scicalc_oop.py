import tkinter as tk
import math

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry('330x620')
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()


class SciCalc():
    def __init__(self):
        self.operation=''   # επιλογή για βασικές πράξεις
        self.total=0
        self.result=False   # έλεγχος αν αυτό που εμφανίζεται στην οθόνη είναι αποτέλεσμα ή εισαγωγή απο το πληκτρολόγιο

    def opSelect(self):     # για τις βασικές πράξεις και το '='
        if self.operation=='addition':
            self.total += float(display.get())
        elif self.operation=='':
            self.total=float(display.get())    

    def equal(self):
        self.opSelect()
        display.delete(0, 'end')
        display.insert(0,self.total)
        self.result=True
        self.operation=''
        self.total=0  

    def addition(self):
        self.operation='addition'
        self.opSelect()
        display.delete(0, 'end')
        display.insert(0,self.total)
        self.result=True        

    def all_clear(self):
        display.delete(0, 'end')
        display.insert(0, '0')
        self.result==False
        self.total=0

    def square_root(self):
        result = math.sqrt(float(display.get()))
        display.delete(0, 'end')
        display.insert(0,result)


    def num_1(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','1')
        else:
            display.insert('end','1')
        self.result=False        

    def num_2(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','2')
        else:
            display.insert('end','2')
        self.result=False    

    def num_3(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','3')
        else:
            display.insert('end','3')
        self.result=False    

    def num_4(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','4')
        else:
            display.insert('end','4')
        self.result=False    

    def num_5(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','5')
        else:
            display.insert('end','5')
        self.result=False    

    def num_6(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','6')
        else:
            display.insert('end','6')
        self.result=False    

    def num_7(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','7')
        else:
            display.insert('end','7')
        self.result=False    

    def num_8(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','8')
        else:
            display.insert('end','8')
        self.result=False    

    def num_9(self,*args):
        if display.get()=='0' or self.result==True:
            display.delete(0, 'end')
            display.insert('end','9')
        else:
            display.insert('end','9')
        self.result=False    

    def num_0(self,*args):
        if self.result==True:
            display.delete(0, 'end')
            display.insert('end', '0')
        else:
            display.insert('end','0')
        self.result=False    

    def comma(self,*args):
        txt=display.get()
        if self.result==True:
            display.delete(0, 'end')
            display.insert('end','0.')
        elif '.' in txt:
            pass    
        else:
            display.insert('end', '.')
        self.result=False    
calc=SciCalc()


display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
display.grid(padx=5, pady=5, sticky="NEW")
display.grid_configure(columnspan=5)
display.insert(0, "0")



tags_func=[ 'rad','deg','M+'       ,'MR'       ,'MC' ,
            'x^y', 'e' ,'sin'      ,'cos'      ,'tan',
            'log','ln' ,'arc\nsin' ,'arc\ncos' ,'arc\ntan',
            '1/x','n!' ,'sinh'     ,'cosh'     ,'tanh',    
            'n√x','2√x','arc\nsinh','arc\ncosh','arc\ntanh'
               ]

functions_1=['', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', calc.square_root, '', '', ''
]

tags_simple=['7', '8', '9', 'C', 'AC',
             '4', '5', '6', 'x', '÷',
             '1', '2', '3', '+', '-',
             '0', ',', chr(177), '='
]

functions_2=[   calc.num_7, calc.num_8, calc.num_9, '', calc.all_clear,
                calc.num_4, calc.num_5, calc.num_6, '', '',
                calc.num_1, calc.num_2, calc.num_3, calc.addition, '',
                calc.num_0, calc.comma, '', calc.equal]

i=0
button_list=[]
for ro in range(1,6):
    for col in range(0,5):
        if tags_func[i]=='M+' or tags_func[i]=='MC' or tags_func[i]=='MR':
            button_list.append(tk.Button(frame, width=4, height=2, bg='grey', fg='red', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i]))
            button_list[i].grid(row=ro, column=col, pady=5)    
        else:
            button_list.append(tk.Button(frame, width=4, height=2, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i], command=functions_1[i]))
            button_list[i].grid(row=ro, column=col, pady=5)
        i+=1

i=0
for ro in range(6,10):
    for col in range(0,5):
        if tags_simple[i]=='C' or tags_simple[i]=='AC':
            button_list.append(tk.Button(frame, width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+25].grid(row=ro, column=col, pady=5)
        elif tags_simple[i]=='=':
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightblue', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+25].grid(row=ro, column=col, columnspan=2, pady=5, sticky="EW")
            break
        else:
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightgrey', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+25].grid(row=ro, column=col, pady=5)
        i+=1

for child in frame.winfo_children():
    child.grid_configure(sticky='NSEW')

root.bind('0', calc.num_0)
root.bind('1', calc.num_1)
root.bind('2', calc.num_2)
root.bind('3', calc.num_3)
root.bind('4', calc.num_4)
root.bind('5', calc.num_5)
root.bind('6', calc.num_6)
root.bind('7', calc.num_7)
root.bind('8', calc.num_8)
root.bind('9', calc.num_9)
root.bind('.', calc.comma)


root.mainloop()