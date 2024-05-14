import tkinter as tk
import math
from idlelib.tooltip import Hovertip


root=tk.Tk()
root.title('Scientific Calculator')
root.geometry('330x690-90+160')                                     # Διαστάσεις / θέση εμφάνισης
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()


# μεταβλητή για τον καθορισμό υπολογισμού μοιρών ή ακτινίων για τις τριγωνομετρικές συναρτήσεις
# απο default, ξεκινάει με μοίρες
is_deg=True                 

class SciCalc():
    def __init__(self):
        self.operation=None                                         # επιλογή για βασικές πράξεις
        self.total=0                                                # Βοηθητική μεταβλητή υπολογισμού
        self.result=False                                           # έλεγχος αν αυτό που εμφανίζεται στην οθόνη είναι αποτέλεσμα ή εισαγωγή απο το πληκτρολόγιο, ώστε να διαγραφεί κατά την επόμενη πληκτρολόγηση από την οθόνη
    
    
    def floatOrInt(self, *args):                                    # έλεγχος αν ο αριθμός που εμφανίζεται στην οθόνη είναι δεκαδικός ή ακέραιος
            if '.' in display.get():
                return float(display.get())
            else:
                return int(display.get())
        
    
    def opSelect(self):                                             # για τις βασικές πράξεις (+, -, *, /)  και το '='
        if self.operation=='addition':
            self.total += self.floatOrInt()
        elif self.operation=='subtraction':
            if total==0 and result==False:
                self.total = self.floatOrInt()
            else:
                self.total -= self.floatOrInt()    
            
        
        
        elif self.operation==None:
            self.total = self.floatOrInt()

    def equal(self,*args):                                          # Συνάρτηση που καλείται όταν πατηθεί το κουμπί '=' ή το πλήκτρο Enter
        self.opSelect()                                             # Κλήση της συνάρτησης υπολογισμού βασικών πράξεων
        display.delete(0, 'end')                                    # Διαγραφή οθόνης
        display.insert(0,self.total)                                # Εμφάνιση αποτελέσματος
        self.result=True                                            # Θέτουμε ότι αυτό που εμφανίζεται είναι αποτέλεσμα και όχι εισαγωγή απο το πληκτρολόγιο, ώστε κατά την επόμενη πληκτρολόγηση να διαγραφεί απο την οθόνη
        self.operation=None                                         # Θέτουμε τον επιλογέα τέλεσης βασικών πράξεων ως κενή μεταβλητή
        self.total=0                                                # Μηδενισμός βοηθητικής μεταβλητής

    def addition(self,*args):
        self.operation='addition'
        self.opSelect()
        display.delete(0, 'end')
        display.insert(0,self.total)
        self.result=True
    
    def subtraction(self, *args):
        self.operation='subtraction'
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
        answer = math.sqrt(float(display.get()))
        display.delete(0, 'end')
        display.insert(0,answer)

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
        elif display.get()=='0':
            pass
        else:
            display.insert('end','0')
        self.result=False

    def num_00(self,*args):
        if self.result==True:
            display.delete(0, 'end')
            display.insert('end', '00')
        elif display.get()=='0':
            pass
        else:
            display.insert('end','00')
        self.result=False

    def decimalPoint(self,*args):
        txt=display.get()
        if self.result==True:
            display.delete(0, 'end')
            display.insert('end','0.')
        elif '.' in txt:
            pass    
        else:
            display.insert('end', '.')
        self.result=False

    def sign(self, *args):
        if self.result==True:
            display.delete(0, 'end')
            display.insert('end','-')
        elif '-' in display.get():
            display.delete(0,1)
        else:
            display.insert(0, '-')
        self.result=False   



calc=SciCalc()


display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
display.grid(padx=5, pady=5, sticky="NSEW")
display.grid_configure(columnspan=5)
display.insert(0, "0")




tags_func=[ 'M-', 'MS', 'GT',
            'π','e','M+'       ,'MR'       ,'MC' ,
            'x^y', 'x^2' ,'sin'      ,'cos'      ,'tan',
            'log','ln' ,'arc\nsin' ,'arc\ncos' ,'arc\ntan',
            '1/x','n!' ,'sinh'     ,'cosh'     ,'tanh',    
            'n√x','2√x','arc\nsinh','arc\ncosh','arc\ntanh',
    
            ]

functions_1=['', '', '',
             '', '', '', '', '',
             '', '', '', '', '',
             '', '', '', '', '',
             '', '', '', '', '',
             '', calc.square_root, '', '', '',
                    
]

hover_message=['Αφαίρεση αριθμού από την μνήμη','Προσθήκη αριθμού στην μνήμη','Άθροισμα αποτελεσμάτων','Ο αριθμός π', 'Η σταθερά Όιλερ', 'Πρόσθεσε τον αριθμό στην μνήμη', 'Ανάκτηση αριθμού από την μνήμη', 'Καθαρισμός μνήμης',
               'Ύψωση σε δύναμη', 'Ύψωση στο τετράγωνο','Ημίτονο', 'Συνημίτονο', 'Εφαπτομένη',
               'Λογάριθμος', 'Φυσικός λογάριθμος', 'Αντίστροφο ημίτονο', 'Αντίστροφο συνημίτονο', 'Αντίστροφη εφαπτομένη',
               'Αντίστροφος', 'Παραγοντικό', 'Υπερβολικό ημίτονο', 'Υπερβολικό συνημίτονο', 'Υπερβολική εφαπτομένη',
               'n-οστή ρίζα του x', 'Τετραγωνική ρίζα του x', 'Αντίστροφο υπερβολικό\n              ημίτονο',
               'Αντίστροφο υπερβολικό\n          συνημίτονο', 'Αντίστροφη υπερβολική\n           εφαπτομένη']


tags_simple=['(', ')','C' , 'AC', chr(9003),
             '7', '8', '9', '%' , 'ROUND',
             '4', '5', '6', 'x', '÷',
             '1', '2', '3', '+', '-',
             '0', '.', '00', chr(177), '='
]

functions_2=[   '', '', '', calc.all_clear, '',
                calc.num_7, calc.num_8, calc.num_9, '', '',
                calc.num_4, calc.num_5, calc.num_6, '', '',
                calc.num_1, calc.num_2, calc.num_3, calc.addition, calc.subtraction,
                calc.num_0, calc.decimalPoint, calc.num_00, calc.sign, calc.equal]

def switch():
    global is_deg

    if is_deg:
        switch_button.config(image = rad)
        # TODO: add RAD calculation function
        is_deg = False
    else:
        switch_button.config(image = deg)
        # TODO: add DEG caclulation function
        is_deg = True 

rad = tk.PhotoImage(file = "Rad.png")
deg = tk.PhotoImage(file = "Deg.png")

switch_button=tk.Button(frame, width=2, height=40, image=deg, cursor="exchange", command=switch)
switch_button.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="NSEW")

i=0
button_list=[]
for col in range(2,5):
    if tags_func[i]=='M-' or tags_func[i]=='MS' or tags_func[i]=='GT':
        button_list.append(tk.Button(frame, width=4, height=2, bg='light sea green', fg='red', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i]))
        button_list[i].grid(row=1, column=col, pady=5, padx=2, sticky="NSEW")
    i+=1
for ro in range(2,7):
    for col in range(0,5):
        if tags_func[i]=='M+' or tags_func[i]=='MC' or tags_func[i]=='MR':
            button_list.append(tk.Button(frame, width=4, height=2, bg='light sea green', fg='red', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i]))
            button_list[i].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        else:
            button_list.append(tk.Button(frame, width=4, height=2, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i], command=functions_1[i]))
            button_list[i].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        i+=1

i=0
for ro in range(8,13):
    for col in range(0,5):
        if tags_simple[i]=='C' or tags_simple[i]=='AC' or tags_simple[i]==chr(9003):
            button_list.append(tk.Button(frame, width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        elif tags_simple[i]=='+' or tags_simple[i]=='-' or tags_simple[i]=='÷' or tags_simple[i]=='x' or tags_simple[i]== chr(177) or tags_simple[i]== '%':
            button_list.append(tk.Button(frame, width=5, height=2, bg='black', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        elif tags_simple[i]=='ROUND':
            button_list.append(tk.Button(frame, width=5, height=2, bg='black', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
            Hovertip(button_list[i+28], "Στρογγυλοποίηση", hover_delay=500)  
        elif tags_simple[i]=='=':
            button_list.append(tk.Button(frame, width=5, height=2, bg='indianred3', fg='black', activebackground='green', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, columnspan=1, pady=5, padx=2, sticky="NSEW")
            break
        else:
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightblue', activebackground='seagreen1', fg='black', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        i+=1

Hovertip(switch_button, "Κλίκ για εναλλαγή υπολογισμού\n            μοιρών/ ακτινίων", hover_delay=100)

for i in range(len(tags_func)):
    Hovertip(button_list[i], hover_message[i], hover_delay=500)

for child in frame.winfo_children():
    child.grid_configure(sticky='NSEW')

# Keybindings
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
root.bind('.', calc.decimalPoint)
root.bind('=', calc.equal)
root.bind('<Return>', calc.equal)
root.bind('+', calc.addition)
root.bind('-', calc.subtraction)


root.mainloop()