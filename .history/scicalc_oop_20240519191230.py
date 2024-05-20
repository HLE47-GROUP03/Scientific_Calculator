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
        self.haveOperant=False                                      # λογική μεταβλητή για τον έλεγχο ύπαρξης πρώτου τελεστέου για συναρτήσεις που απαιτούν δύο (πχ, ν-οστή ρίζα, ν-οστή δύναμη κτλ)
        self.secOperation=None                                      # επιλογή για δευτερεύουσες πράξεις
    
    
    def floatOrInt(self, *args):                                    # έλεγχος αν ο αριθμός που εμφανίζεται στην οθόνη είναι δεκαδικός ή ακέραιος
        if '.' in display.get():
            return float(display.get())
        else:
            return int(display.get())
        
    
    def opSelect(self):                                             # για τις ΄βασικές πράξεις ( '+' , '-' , '*' , '/' ) και το '='
        if self.operation=='addition':
            self.total += self.floatOrInt()

        elif self.operation=='subtraction':
            if self.result==True or (self.total==0 and self.result==False):                # έλεγχος αν υπάρχει ήδη ένας τελεστέος, ΄ώστε να μην αφαιρεθεί ο πρώτος τελεστέος από το '0' που είναι η αρχικοποιημένη τιμή της μεταβλητής self.total
                self.total = self.floatOrInt()
            else:
                self.total -= self.floatOrInt()

        elif self.operation=='multiplication':
            if self.result==True or (self.total==0 and self.result==False):
                self.total = self.floatOrInt()
            else:
                self.total *= self.floatOrInt()

        elif self.operation=='division':
            if self.result==True or (self.total==0 and self.result==False):
                self.total = self.floatOrInt()
            else:
                if self.floatOrInt()!=0:                            # Έλεγχος αν ο διαιρέτης είναι διάφορος του '0' και εκτέλεση της διαίρεσης
                    self.total /= self.floatOrInt()
                else:                                               # Διαφορετικά εμφάνιση σφάλματος
                    self.total = 'Math ERROR'
        elif self.operation==None:
            self.total = self.floatOrInt()
        

    def secOpSelect(self):
        if self.secOperation=='nRoot':                              # # Υπολογισμός n-οστής ρίζας του Χ
            if self.haveOperant==False:                             # Αν δεν έχει αποθηκευτεί η μεταβλητή του βαθμού της ρίζας, χρήση του αριθμού που δόθηκε σαν βαθμός
                self.degree=self.floatOrInt()                       # Η τιμή της οθόνης αποθηκεύεται στη μεταβλητή βαθμού ρίζας
                self.haveOperant=True                               # Η μεταβλητή του πρώτης παραμέτρου γίνεται αληθής (πρώτη παράμετρος σε αυτή την περίπτωση είναι ο βαθμός-τάξη της ρίζας )
                self.result=True
            else:                                                   # Αν υπάρχει ήδη βαθμός, χρήση του αριθμού ως υπόρριζο
                self.radicand=self.floatOrInt()                     # Αποθήκευση της τιμής οθόνης ως υπόρριζο
                self.secTotal=self.radicand**(1/self.degree)        # Πράξη υπολογισμού της ρίζας
                display.delete(0, 'end')
                display.insert(0,self.secTotal)                     # Εμφάνιση στην οθόνη του αποτελέσματος
                self.haveOperant=False                              # Εφόσον έγινε η πράξη, η μεταβλητή ύπαρξης πρώτου τελεστέου γίνεται πάλι ψευδής
                self.result=False
                self.secOperation=None                              # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='nPower':                           # Υπολογισμός Χ στη δύναμη του Υ
            if self.haveOperant==False:                             # Αν δεν έχει αποθηκευτεί η μεταβλητή της βάσης, χρήση του αριθμού που δόθηκε σαν βάση
                self.base=self.floatOrInt()                         # Η τιμή της οθόνης αποθηκεύεται στη μεταβλητή βάσης
                self.haveOperant=True                               # Η μεταβλητή του πρώτης παραμέτρου γίνεται αληθής (πρώτη παράμετρος σε αυτή την περίπτωση είναι ο βάση )
                self.result=True
            else:                                                   # Αν υπάρχει ήδη βάση, χρήση του αριθμού ως εκθέτη
                self.exponent=self.floatOrInt()                     # Αποθήκευση της τιμής οθόνης ως εκθέτη
                self.secTotal=self.base**self.exponent              # Πράξη υπολογισμού της δύναμης
                display.delete(0, 'end')
                display.insert(0,self.secTotal)                     # Εμφάνιση στην οθόνη του αποτελέσματος
                self.haveOperant=False                              # Εφόσον έγινε η πράξη, η μεταβλητή ύπαρξης πρώτου τελεστέου γίνεται πάλι ψευδής
                self.result=False
                self.secOperation=None                              # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης
    
        elif self.secOperation=='squared':
            self.base=self.floatOrInt()                         # Αποθήκευση της τιμής οθόνης ως εκθέτη
            self.secTotal=self.base**2                              # Πράξη υπολογισμού της δύναμης
            display.delete(0, 'end')
            display.insert(0,self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.result=False
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης
        
        elif self.secOperation=='sin':
            self.angle=self.floatOrInt





    def equal(self,*args):                                          # Συνάρτηση που καλείται όταν πατηθεί το κουμπί '=' ή το πλήκτρο Enter
        if self.secOperation:                                       # Αν υπάρχει δευτερεύουσα πράξη σε εξέλιξη (πχ ν-οστή ρίζα) εκτέλεση αυτής
            self.secOpSelect()
        self.opSelect()                                             # Κλήση της συνάρτησης υπολογισμού βασικών πράξεων
        display.delete(0, 'end')                                    # Διαγραφή οθόνης
        try:
            if (self.total%1)==0:                                   # Έλεγχος αν το αποτέλεσμα είναι ακέραιος ή δεκαδικός, για τη σωστή εμφάνιση του αριθμού
                display.insert(0,int(self.total))                   
            else:
                display.insert(0,self.total)
        except:                                                     # Εξαίρεση σφάλματος για την περίπτωση που η μεταβλητή self.total περιέχει χαρακτήρες (πχ κατά τη διαίρεση με το 0)
            display.insert(0,self.total)                            # Εμφάνιση αποτελέσματος
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

    def multiplication(self, *args):
        self.operation='multiplication'
        self.opSelect()
        display.delete(0, 'end')
        display.insert(0,self.total)
        self.result=True

    def division(self, *args):
        self.operation='division'
        self.opSelect()
        display.delete(0, 'end')
        display.insert(0,self.total)
        self.result=True
    
    def percent(self, *args):
        if self.operation:
            self.equal()
            number=self.floatOrInt()
            display.delete(0, 'end')
            display.insert(0,number*100)     
        else:
            number=self.floatOrInt()
            display.delete(0, 'end')
            display.insert(0,number/100)
        self.result=True
    
    def roundFunc(self, *args):
        number=display.get()
        number=round(float(number))
        display.delete(0, 'end')
        display.insert(0, number)
        self.result=True

    def clear(self):
        display.delete(0, 'end')
        display.insert('end', self.total)
        self.result=True

    def backspace(self,*args):
        if display.get()=='0':
            self.result=True
        elif len(display.get())==1:
            display.delete(0, 'end')
            display.insert('end', '0')
            self.result=True
        else:
            display.delete(display.index("end") - 1)
            self.result=False

    def all_clear(self):
        display.delete(0, 'end')
        display.insert(0, '0')
        self.result=False
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
        if '-' in display.get():
            number=display.get()
            number=number[1:]
            display.delete(0, 'end')
            display.insert('end',number)
        else:
            display.insert(0, '-')
        self.result=False

    def piKey(self):
        display.delete(0, 'end')
        display.insert('end','3.14159265')
        self.result=False

    def napierConstant(self):
        display.delete(0, 'end')
        display.insert('end','2.71828182')
        self.result=False

    def nRoot(self, *args):
        self.secOperation='nRoot'
        self.secOpSelect()

    def nPower(self, *args):
        self.secOperation='nPower'
        self.secOpSelect()

    def squared(self, *args):
        self.secOperation='squared'
        self.secOpSelect()
    
    def sin(self, *args):
        self.secOperation='sin'
        self.secOpSelect()


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
             calc.piKey, calc.napierConstant, '', '', '',
             calc.nPower, calc.squared, '', '', '',
             '', '', '', '', '',
             '', '', '', '', '',
             calc.nRoot, calc.square_root, '', '', '',
                    
]

hover_message=['Αφαίρεση αριθμού από την μνήμη','Προσθήκη αριθμού στην μνήμη','Άθροισμα αποτελεσμάτων','Ο αριθμός π', 'Η σταθερά του Νέιπιερ\n(αριθμός Όιλερ)', 'Πρόσθεσε τον αριθμό στην μνήμη', 'Ανάκτηση αριθμού από την μνήμη', 'Καθαρισμός μνήμης',
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

functions_2=[   'left parenthesis', 'right parenthesis', calc.clear, calc.all_clear, calc.backspace,
                calc.num_7, calc.num_8, calc.num_9, calc.percent, calc.roundFunc,
                calc.num_4, calc.num_5, calc.num_6, calc.multiplication, calc.division,
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
            Hovertip(button_list[i+28], "Στρογγυλοποίηση στον\nκοντινότερο ακέραιο", hover_delay=500)  
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
root.bind('*', calc.multiplication)
root.bind('/', calc.division)
root.bind('<BackSpace>', calc.backspace)

root.mainloop()