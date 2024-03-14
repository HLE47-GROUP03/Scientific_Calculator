import tkinter as tk
from tkinter import ttk
from tkinter import *
from idlelib.tooltip import Hovertip


root=tk.Tk()
root.title('Scientific Calculator')
root.geometry("330x580-100+180")
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()

display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
display.grid(padx=5, pady=5, sticky="NEW")
display.grid_configure(columnspan=5)
display.insert(0, "0")

tags_func=[ 'rad','deg','M+'       ,'MR'       ,'MC' ,
            '^', 'e','sin'      ,'cos'      ,'tan',
            'log','ln' ,'arc\nsin' ,'arc\ncos' ,'arc\ntan',
            '1/x','n!' ,'sinh'     ,'cosh'     ,'tanh',    
            'n√x','√','arc\nsinh','arc\ncosh','arc\ntanh'
               ]

functions_1=['', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', ''
]
hover_message=['Ακτίνια', 'Μοίρες', 'Προσθήκη αριθμού στην μνήμη', 'Ανάκτηση αριθμού από την μνήμη', 'Καθαρισμός μνήμης',
               'Ύψωση σε δύναμη', 'Σταθερά e','Ημίτονο', 'Συνημίτονο', 'Εφαπτομένη', 'Λογάριθμος', 'Φυσικός λογάριθμος', 'Αντίστροφο ημίτονο',
               'Αντίστροφο συνημίτονο', 'Αντίστροφη εφαπτομένη', 'Αντίστροφο', 'Παραγοντικό', 'Υπερβολικό ημίτονο', 'Υπερβολικό συνημίτονο',
               'Υπερβολική εφαπτομένη','n-οστή ρίζα του x', 'Τετραγωνική ρίζα του x', 'Αντίστροφο υπερβολικό\n             ημίτονο',
               'Αντίστροφο υπερβολικό\n          συνημίτονο', 'Αντίστροφη υπερβολική\n          εφαπτομένη']

tags_simple=['7', '8', '9', 'C', 'AC',
             '4', '5', '6', 'x', '÷',
             '1', '2', '3', '+', '-',
             '0', ',', '+/-', '='
]

functions_2=['', '', '', '', 'all_clear',
            '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',]

i=0
button_list=[]
for ro in range(1,6):
    for col in range(0,5):
        if tags_func[i]=='M+' or tags_func[i]=='MC' or tags_func[i]=='MR':
            button_list.append(tk.Button(frame, width=4, height=2, bg='grey', fg='red', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i]))
            button_list[i].grid(row=ro, column=col, pady=5)    
        else:
            button_list.append(tk.Button(frame, width=4, height=2, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i]))
            button_list[i].grid(row=ro, column=col, pady=5)
        i+=1
   

i=0
for ro in range(6,10):
    for col in range(0,5):
        if tags_simple[i]=='C' or tags_simple[i]=='AC':
            button_list.append(tk.Button(frame, width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+25].grid(row=ro, column=col, pady=5)
        elif tags_simple[i]=='=':
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightblue', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i]))
            button_list[i+25].grid(row=ro, column=col, columnspan=2, pady=5, sticky="EW")
            break
        else:
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightgrey', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i]))
            button_list[i+25].grid(row=ro, column=col, pady=5)
        i+=1

for i in range(len(tags_func)):
    Hovertip(button_list[i], hover_message[i], hover_delay = 500 )
   
root.mainloop()
