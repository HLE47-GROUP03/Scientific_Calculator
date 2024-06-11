import os
import tkinter as tk
import math
from idlelib.tooltip import Hovertip
import decimal


root=tk.Tk()
root.title('Scientific Calculator')
root.geometry('322x690-250+90')                                     # Διαστάσεις / θέση εμφάνισης
root.resizable(False, False)

frame=tk.Frame(root)
frame.grid()

is_deg=True                                                         # επιλογή υπολογισμού σε μοίρες ή ακτίνια (default: μοίρες)

class SciCalc():
    def __init__(self):
        self.operation=None                                         # επιλογή για βασικές πράξεις
        self.total=0                                                # Βοηθητική μεταβλητή υπολογισμού
        self.result=False                                           # έλεγχος αν αυτό που εμφανίζεται στην οθόνη είναι αποτέλεσμα ή εισαγωγή απο το πληκτρολόγιο, ώστε να διαγραφεί κατά την επόμενη πληκτρολόγηση από την οθόνη
        self.haveOperant=False                                      # λογική μεταβλητή για τον έλεγχο ύπαρξης πρώτου τελεστέου για συναρτήσεις που απαιτούν δύο (πχ, ν-οστή ρίζα, ν-οστή δύναμη κτλ)
        self.secOperation=None                                      # επιλογή για δευτερεύουσες πράξεις
        self.memory=0                                               # για τους αριθμούς που αποθηκεύονται στη μνήμη
        self.grTotal=0                                              # για τη λειτουργία αποθήκευσης γενικού συνόλου

    def printNumber(self, number, *args):                           # Μέθοδος για την εμφάνιση των αποτελεσμάτων
        try:
            text=float(number)                                      # Μετατροπή σε δεκαδικό για την περίπτωση που είναι ΄ήδη σε επιστημονική μορφή
            try:
                significance = len(str(int(text)))                  # Η στρογγυλοποίηση θα γίνει βάσει του πλήθους ψηφίων του ακέραιου μέρους του αριθμού
                if significance>11:
                    significance=11
            except OverflowError:
                significance = 0                                    # Για την περίπτωση πολύ μεγάλων αριθμών
            if abs(round(text,4)==round(text,12-significance)) and round(text,4)!=0:    # Ελέγχουμε πόσο ακριβής είναι η στρογγυλοποίηση (πχ, ο αριθμός 5.0000000000001)
                try:
                    text=round(text,11-significance)                # Στην περίπτωση που ο δεκαδικός είναι πολύ κοντά στον ακέραιο (διαφέρουν μετά το 12ο δεκαδικό για μικρούς αριθμούς), στρογγυλοποιούμε στον κοντινότερο ακέραιο
                except OverflowError:                               # Για την περίπτωση πολύ μεγάλων αριθμών
                    text='Overflow ERROR'
            if '.' in str(text):                                    # Έλεγχος για την σωστή εμφάνιση δεκαδικών και ακεραίων
                if text%1==0:                                       # Αν υπάρχει δεκαδικό σημείο αλλά τα δεκαδικά ψηφία είναι '0'
                    text=int (text)                                 # Ο αριθμός θα εμφανιστεί σαν ακέραιος          
                else:
                    text=float (text)                               # Αλλιώς σαν δεκαδικός
            elif ('e' in str(text)):                                # Αν ο αριθμός είναι σε επιστημονική μορφή (π.χ. 4ε-06)
                exp_count = str(text)                               #
                while exp_count[0]!='e':                            #
                    exp_count=exp_count[1:]                         # Επανάληψη για να βρούμε πόσα δεκαδικά ψηφία έχει ο αριθμός (ο εκθέτης του 10 στην επιστημονική μορφή)
                exp_count=exp_count[1:]                             #
                exp_count=abs(int(exp_count))                       #
                if exp_count < 17:                                  # Αν ο εκθέτης είναι μικρότερος από το 17 (σε απόλυτη τιμή, άρα 18 δεκαδικά ψηφία) και επομένως μπορεί να εμφανιστεί στην οθόνη
                    text= "{:.17f}".format(text)                    # Μετατρέπεται σε δεκαδικό με 17 δεκαδικά
                    while text[-1]=='0':                            # Επανάληψη για να σβηστούν τα περιττά '0' στο τέλος
                        text=text[:-1]
            else:
                try:
                    text=int (text)                                 # Εφόσον δεν υπάρχει δεκαδικό σημείο, είναι ακέραιος
                except OverflowError:
                    text='Overflow ERROR'

            if len(str(text))>20:                                   # Αν το μήκος του αριθμού είναι μεγαλύτερο απο 20 ψηφία
                text=format(text, '.13e')                           # Μετατροπή σε επιστημονική μορφή (Συνολικού πλήθους 20 χαρακτήρων )
                if len(text) > 20:                                  # Αν η επιστημονική μορφή είναι μεγαλύτερη απο 20 χαρακτήρες
                    text='Display ERROR'                            # Εμφάνιση σφ΄΄αλματος

        except ValueError:
            if ('ERROR' not in str(number)) and ('-' not in str(number)):
                text='Display ERROR'
            else:
                text=str(number)    
        display.delete(0, 'end')                                    # Διαγραφή ΄΄ο,τι εμφανίζεται ήδη στην οθόνη
        display.insert(0,text)                                      # Εμφάνιση του αποτελέσματος
        self.result=True
        
    def inputHandler(self, *args):                                  # έλεγχος αν ο αριθμός που εμφανίζεται στην οθόνη είναι δεκαδικός ή ακέραιος
        if 'ERROR' in display.get() or display.get() == '-':
            return 0
        elif '.' or 'e' in display.get():                           # Αν υπάρχει η τελεία στον αριθμό
            return decimal.Decimal(display.get())                   # επιστρέφει float
        else:                                                       # αλλιώς
            return int(display.get())                               # επιστρέφει ακέραιο

    
    def opSelect(self):                                             # για τις ΄βασικές πράξεις ( '+' , '-' , '*' , '/' ) και το '='
        if self.secOperation:                                       # Αν υπάρχει δευτερεύουσα πράξη σε εξέλιξη (πχ ν-οστή ρίζα) εκτέλεση αυτής
            self.secOpSelect()

        if self.operation=='addition':                              # Πρόσθεση
            self.total += self.inputHandler()

        elif self.operation=='subtraction':                         # Αφαίρεση
            self.total -= self.inputHandler()

        elif self.operation=='multiplication':                      # Πολλαπλασιασμός
            self.total *= self.inputHandler()

        elif self.operation=='division':                            # Διαίρεση
            if self.inputHandler()!=0:                              # Έλεγχος αν ο διαιρέτης είναι διάφορος του '0' και εκτέλεση της διαίρεσης
                self.total /= self.inputHandler()
            else:                                                   # Διαφορετικά εμφάνιση σφάλματος
                self.total = 'Math ERROR'

        elif self.operation=='mod':                                 # Υπόλοιπο
            if self.inputHandler()!=0:                              # Έλεγχος αν ο διαιρέτης είναι διάφορος του '0' και εκτέλεση της διαίρεσης
                self.total %= self.inputHandler()
            else:                                                   # Διαφορετικά εμφάνιση σφάλματος
                self.total = 'Math ERROR'

        elif self.operation==None:
            self.total = self.inputHandler()
        

    def secOpSelect(self):
        if self.secOperation=='nRoot':                              # # Υπολογισμός n-οστής ρίζας του Χ
            if self.haveOperant==False:                             # Αν δεν έχει αποθηκευτεί η μεταβλητή του βαθμού της ρίζας, χρήση του αριθμού που δόθηκε σαν βαθμός
                self.degree=self.inputHandler()                     # Η τιμή της οθόνης αποθηκεύεται στη μεταβλητή βαθμού ρίζας
                if self.degree==0:
                    self.printNumber('Math ERROR')
                else:    
                    self.haveOperant=True                           # Η μεταβλητή του πρώτης παραμέτρου γίνεται αληθής (πρώτη παράμετρος σε αυτή την περίπτωση είναι ο βαθμός-τάξη της ρίζας )
            else:                                                   # Αν υπάρχει ήδη βαθμός, χρήση του αριθμού ως υπόρριζο
                self.radicand=self.inputHandler()                   # Αποθήκευση της τιμής οθόνης ως υπόρριζο
                self.secTotal=self.radicand**(1/self.degree)        # Πράξη υπολογισμού της ρίζας
                self.printNumber(self.secTotal)                     # Εμφάνιση στην οθόνη του αποτελέσματος
                self.haveOperant=False                              # Εφόσον έγινε η πράξη, η μεταβλητή ύπαρξης πρώτου τελεστέου γίνεται πάλι ψευδής
                self.secOperation=None                              # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='nPower':                           # Υπολογισμός Χ στη δύναμη του Υ
            if self.haveOperant==False:                             # Αν δεν έχει αποθηκευτεί η μεταβλητή της βάσης, χρήση του αριθμού που δόθηκε σαν βάση
                self.base=self.inputHandler()                       # Η τιμή της οθόνης αποθηκεύεται στη μεταβλητή βάσης
                self.haveOperant=True                               # Η μεταβλητή του πρώτης παραμέτρου γίνεται αληθής (πρώτη παράμετρος σε αυτή την περίπτωση είναι ο βάση )
            else:                                                   # Αν υπάρχει ήδη βάση, χρήση του αριθμού ως εκθέτη
                self.exponent=self.inputHandler()                   # Αποθήκευση της τιμής οθόνης ως εκθέτη
                self.secTotal=self.base**self.exponent              # Πράξη υπολογισμού της δύναμης
                self.printNumber(self.secTotal)                     # Εμφάνιση στην οθόνη του αποτελέσματος
                self.haveOperant=False                              # Εφόσον έγινε η πράξη, η μεταβλητή ύπαρξης πρώτου τελεστέου γίνεται πάλι ψευδής
                self.secOperation=None                              # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='squared':
            self.base=self.inputHandler()                           # Αποθήκευση της τιμής οθόνης ως εκθέτη
            self.secTotal=self.base**2                              # Πράξη υπολογισμού της δύναμης
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης
        
        elif self.secOperation=='sin':                              # Υπολογισμός ημίτονου
            self.angle=self.inputHandler()                          # Ανάγνωση οθόνης
            if is_deg:                                              # Αν ο επιλογέας είναι σε υπολογισμό σε μοίρες
                self.angle=math.radians(self.angle)                 # Μετατροπή της γωνίας σε ακτίνια (η math.sin() δέχεται παράμετρο σε ακτίνια)
            self.secTotal=round(math.sin(self.angle),15)            # Στρογγυλοποίηση στα 15 δεκαδικά
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='cos':                              # Υπολογισμός συνημίτονου
            self.angle=self.inputHandler()                            # Ανάγνωση οθόνης
            if is_deg:                                              # Αν ο επιλογέας είναι σε υπολογισμό σε μοίρες
                self.angle=math.radians(self.angle)                 # Μετατροπή της γωνίας σε ακτίνια (η math.cos() δέχεται παράμετρο σε ακτίνια)
            self.secTotal=round(math.cos(self.angle),15)            # Στρογγυλοποίηση στα 15 δεκαδικά
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης
        
        elif self.secOperation=='tan':                              # Υπολογισμός εφαπτομένης
            self.angle=self.inputHandler()                          # Ανάγνωση οθόνης
            right=False
            if is_deg:                                              # Αν ο επιλογέας είναι σε υπολογισμό σε μοίρες
                self.angle=math.radians(self.angle)                 # Μετατροπή της γωνίας σε ακτίνια (η math.tan() δέχεται παράμετρο σε ακτίνια)
            if float (self.angle)%math.pi==1.5707963267948966:
                right=True                                          # Έλεγχος αν η γωνία είναι 90 + (n * 180) μοίρες (δεν ορίζεται η εφαπτομένη 90 μοιρών)
            self.secTotal=math.tan(self.angle)
            if right:
                self.printNumber('Math ERROR')
            else:
                self.printNumber(round(self.secTotal,15))           # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='arcSin':                           # Υπολογισμός αντίστροφου ημίτονου
            try:
                self.secTotal=math.asin(self.inputHandler())
                if is_deg:                                          # Αν ο επιλογέας υπολογισμού γωνιών είναι σε μοίρες
                    self.secTotal=math.degrees(self.secTotal)       # Μετατροπή απο ακτίνια σε μοίρες (η math.asin() επιστρέφει αποτέλεσμα σε ακτίνια)
            except:
                self.secTotal='Math ERROR'                          # Εξαίρεση σφάλματος για την περίπτωση που η παράμετρος δεν είναι ανάμεσα στο -1 και το 1 (προϋπόθεση της math.asin())
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='arcCos':                           # Υπολογισμός αντίστροφου συνημίτονου
            try:
                self.secTotal=math.acos(self.inputHandler())
                if is_deg:                                          # Αν ο επιλογέας υπολογισμού γωνιών είναι σε μοίρες
                    self.secTotal=math.degrees(self.secTotal)       # Μετατροπή απο ακτίνια σε μοίρες (η math.acos() επιστρέφει αποτέλεσμα σε ακτίνια)
            except:
                self.secTotal='Math ERROR'                          # Εξαίρεση σφάλματος για την περίπτωση που η παράμετρος δεν είναι ανάμεσα στο -1 και το 1 (προϋπόθεση της math.acos())
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='arcTan':
            self.secTotal=math.atan(self.inputHandler())
            if is_deg:                                              # Αν ο επιλογέας υπολογισμού γωνιών είναι σε μοίρες
                self.secTotal=math.degrees(self.secTotal)           # Μετατροπή απο ακτίνια σε μοίρες (η math.atan() επιστρέφει αποτέλεσμα σε ακτίνια)
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='log':                              # Δεκαδικός Λογάριθμος
            try:
                self.secTotal=math.log10(self.inputHandler())
            except:
                self.secTotal='Math ERROR'                          # Εξαίρεση σφάλματος για την περίπτωση που η παράμετρος δεν είναι μεγαλύτερη του 0 (προϋπόθεση της math.log10())
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='ln':                               # Φυσικός Λογάριθμος
            try:
                self.secTotal=math.log(self.inputHandler())
            except:
                self.secTotal='Math ERROR'                          # Εξαίρεση σφάλματος για την περίπτωση που η παράμετρος δεν είναι μεγαλύτερη του 0 (προϋπόθεση της math.log())
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='inverse':                          # Αντίστροφος
            try:
                self.secTotal=1/self.inputHandler()
            except ZeroDivisionError:
                self.secTotal='Math ERROR'
            self.printNumber(self.secTotal)
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='factorial':                        # Παραγοντικό
            try:
                self.secTotal=math.factorial(self.inputHandler())
            except:                                                 # Για την περίπτωση που η παράμετρος είναι αρνητικός αριθμός
                self.secTotal='Math ERROR'
            self.printNumber(self.secTotal)
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='sinh':
            self.angle=self.inputHandler()
            if is_deg:                                              # Αν ο επιλογέας είναι σε μοίρες
                self.angle=math.radians(self.angle)                 # Μετατροπή σε ακτίνια για τον υπολογισμό της math.sinh()
            self.secTotal=math.sinh(self.angle)
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='cosh':
            self.angle=self.inputHandler()
            if is_deg:                                              # Αν ο επιλογέας υπολογισμού γωνιών είναι σε μοίρες
                self.angle=math.radians(self.angle)
            self.secTotal=math.cosh(self.angle)
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης
        
        elif self.secOperation=='tanh':
            self.angle=self.inputHandler()
            if is_deg:                                              # Αν ο επιλογέας είναι σε μοίρες
                self.angle=math.radians(self.angle)                 # Μετατροπή σε ακτίνια για τον υπολογισμό της math.tanh()
            self.secTotal=math.tanh(self.angle)
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='arcSinh':
            self.secTotal=math.asinh(self.inputHandler())
            if is_deg:                                              # Αν ο επιλογέας υπολογισμού γωνιών είναι σε μοίρες
                self.secTotal=math.degrees(self.secTotal)           # Μετατροπή απο ακτίνια σε μοίρες (η math.asinh επιστρέφει αποτέλεσμα σε ακτίνια)
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='arcCosh':
            try:
                self.secTotal=math.acosh(self.inputHandler())
                if is_deg:                                          # Αν ο επιλογέας υπολογισμού γωνιών είναι σε μοίρες
                    self.secTotal=math.degrees(self.secTotal)       # Μετατροπή απο ακτίνια σε μοίρες (η math.acosh επιστρέφει αποτέλεσμα σε ακτίνια)
            except:
                self.secTotal='Math ERROR'                          # Εξαίρεση σφάλματος για την περίπτωση που η παράμετρος δεν είναι θετικός (προϋπόθεση της math.acosh())
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        elif self.secOperation=='arcTanh':
            try:
                self.secTotal=math.atanh(self.inputHandler())
                if is_deg:                                          # Αν ο επιλογέας υπολογισμού γωνιών είναι σε μοίρες
                    self.secTotal=math.degrees(self.secTotal)       # Μετατροπή απο ακτίνια σε μοίρες (η math.atanh επιστρέφει αποτέλεσμα σε ακτίνια)
            except:
                self.secTotal='Math ERROR'                          # Εξαίρεση σφάλματος για την περίπτωση που η παράμετρος δεν είναι ανάμεσα στο 0,99 και το -0,99 (προϋπόθεση της math.atanh())
            self.printNumber(self.secTotal)                         # Εμφάνιση στην οθόνη του αποτελέσματος
            self.secOperation=None                                  # Μηδενισμός της μεταβλητής επιλογής δευτερεύουσας πράξης

        self.result=True


    def equal(self,*args):                                          # Μέθοδος που καλείται όταν πατηθεί το κουμπί '=' ή το πλήκτρο Enter
        self.opSelect()                                             # Κλήση της μεθόδου υπολογισμού βασικών πράξεων
        display.delete(0, 'end')                                    # Διαγραφή οθόνης
        try:
            if (self.total%1)==0:                                   # Έλεγχος αν το αποτέλεσμα είναι ακέραιος ή δεκαδικός, για τη σωστή εμφάνιση του αριθμού
                self.printNumber(int(self.total))                   
            else:
                self.printNumber(self.total)
        except:                                                     # Εξαίρεση σφάλματος για την περίπτωση που η μεταβλητή self.total περιέχει χαρακτήρες (πχ κατά τη διαίρεση με το 0)
            self.printNumber(self.total)                            # Εμφάνιση αποτελέσματος
        self.grTotal+=self.inputHandler()
        self.result=True                                            # Θέτουμε ότι αυτό που εμφανίζεται είναι αποτέλεσμα και όχι εισαγωγή απο το πληκτρολόγιο, ώστε κατά την επόμενη πληκτρολόγηση να διαγραφεί απο την οθόνη
        self.operation=None                                         # Θέτουμε τον επιλογέα τέλεσης βασικών πράξεων ως κενή μεταβλητή
        self.total=0                                                # Μηδενισμός βοηθητικής μεταβλητής

    def addition(self,*args):                                       # Πρόσθεση
        self.opSelect()                                             # Κλήση της μεθόδου opSelect() ώστε να εκτελεστεί η προηγούμενη πράξη (αν υπάρχει)
        self.operation='addition'                                   # Θέτουμε τον επιλογέα κύριας πράξης ως πρόσθεση
        self.printNumber(self.total)                                # Εμφάνιση μερικού συνόλου
        self.result=True
    
    def subtraction(self, *args):                                   # Αφαίρεση
        self.opSelect()                                             # Κλήση της μεθόδου opSelect() ώστε να εκτελεστεί η προηγούμενη πράξη (αν υπάρχει)
        self.operation='subtraction'                                # Θέτουμε τον επιλογέα κύριας πράξης ως αφαίρεση
        self.printNumber(self.total)                                # Εμφάνιση μερικού συνόλου
        self.result=True

    def multiplication(self, *args):                                # Πολλαπλασιασμός
        self.opSelect()                                             # Κλήση της μεθόδου opSelect() ώστε να εκτελεστεί η προηγούμενη πράξη (αν υπάρχει)
        self.operation='multiplication'                             # Θέτουμε τον επιλογέα κύριας πράξης ως πολλαπλασιασμό
        self.printNumber(self.total)                                # Εμφάνιση μερικού συνόλου
        self.result=True

    def division(self, *args):                                      # Διαίρεση
        self.opSelect()                                             # Κλήση της μεθόδου opSelect() ώστε να εκτελεστεί η προηγούμενη πράξη (αν υπάρχει)
        self.operation='division'                                   # Θέτουμε τον επιλογέα κύριας πράξης ως διαίρεση
        self.printNumber(self.total)                                # Εμφάνιση μερικού συνόλου
        self.result=True

    def percent(self, *args):                                                   # Ποσοστό
        if self.operation=='addition' or self.operation=='subtraction':         # Αν υπάρχει πρόσθεση ή αφαίρεση σε εκκρεμότητα
            number=(self.inputHandler()/100)*self.total                         # Βρίσκω το ποσοστό % του προηγούμενου αριθμού
            self.printNumber(number)
            self.equal()                                                        # Το προσθέτω/αφαιρώ από τον προηγούμενο αριθμό 
            
        elif self.operation=='multiplication' or self.operation=='division':    # Αν υπάρχει πολλαπλασιασμός ή διαίρεση
            number=(self.inputHandler()/100)                                    # Μετατροπή του αριθμού στην οθόνη σε %
            self.printNumber(number)
            self.equal()                                                        # Πολλαπλασιασμός/Διαίρεση του δεκαδικού πλέον αριθμού με τον προηγούμενο
        else:
            self.printNumber(self.inputHandler()/100)                           # Μετατροπή του αριθμού απο ποσοστό επί τοις 100 σε δεκαδικό
        self.result=True                 

    def clear(self,*args):                                          # Καθαρισμός
        self.printNumber(self.total)                                # Εμφάνιση αποθηκευμένου μερικού συνόλου
        self.operation=None                                         # Καθαρισμός της τελευταίας πράξης
        self.result=True

    def backspace(self,*args):                                      # Διαγραφή τελευταίου χαρακτήρα
        if self.inputHandler()=='0':
            self.result=True
        elif len(str(self.inputHandler()))==1:                      # Αν το μήκος του αριθμού που εμφανίζεται είναι ένα ψηφίο
            self.printNumber('0')                                   # Διαγραφή του αριθμού και εμφάνιση του '0'
            self.result=True
        else:
            display.delete(display.index("end") - 1)                # Αλλιώς διαγραφή του τελευταίου ψηφίου του αριθμού
            self.result=False

    def allClear(self):                                             # Καθαρισμός όλων
        self.printNumber('0')                                       # Εμφάνιση του '0' στην οθόνη
        self.operation=None                                         #
        self.total=0                                                #
        self.result=False                                           #
        self.haveOperant=False                                      #
        self.secOperation=None                                      # Επαναφορά όλων τον βοηθητικών μεταβλητών
        self.memory=0                                               #
        self.grTotal=0                                              #

    def squareRoot(self):                                           # Τετραγωνική ρίζα
        self.printNumber(math.sqrt(self.inputHandler()))            # Εμφάνιση του αποτελέσματος της math.sqrt()

    def num_1(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('1')                                   # Εμφανίζω το 1 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','1')                               # Αλλιώς προσθέτω το 1 από δεξιά
        self.result=False        

    def num_2(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('2')                                   # Εμφανίζω το 2 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','2')                               # Αλλιώς προσθέτω το 2 από δεξιά
        self.result=False    

    def num_3(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('3')                                   # Εμφανίζω το 3 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','3')                               # Αλλιώς προσθέτω το 3 από δεξιά
        self.result=False    

    def num_4(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('4')                                   # Εμφανίζω το 4 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','4')                               # Αλλιώς προσθέτω το 4 από δεξιά
        self.result=False    

    def num_5(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('5')                                   # Εμφανίζω το 5 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','5')                               # Αλλιώς προσθέτω το 5 από δεξιά
        self.result=False    

    def num_6(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('6')                                   # Εμφανίζω το 6 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','6')                               # Αλλιώς προσθέτω το 6 από δεξιά
        self.result=False    

    def num_7(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('7')                                   # Εμφανίζω το 7 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','7')                               # Αλλιώς προσθέτω το 7 από δεξιά
        self.result=False    

    def num_8(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('8')                                   # Εμφανίζω το 8 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','8')                               # Αλλιώς προσθέτω το 8 από δεξιά
        self.result=False    

    def num_9(self,*args):
        if display.get()=='0' or self.result==True:
            self.printNumber('9')                                   # Εμφανίζω το 9 στην οθόνη αν πριν υπήρχε αποτέλεσμα ή '0'
        else:
            display.insert('end','9')                               # Αλλιώς προσθέτω το 9 από δεξιά
        self.result=False    

    def num_0(self,*args):
        if self.result==True:
            self.printNumber('0')
        elif display.get()=='0' or display.get()=='-0':             # Δεν προσθέτουμε άλλα μηδενικά χωρίς νόημα, περιμένουμε '.' ή καινούργιο αριθμό
            pass
        else:
            display.insert('end','0')                               # Προσθέτω το '0' στην οθόνη από δεξιά
        self.result=False

    def num_00(self,*args):
        if self.result==True:
            self.printNumber('0')                                   # Προσθέτω μόνο 1 μηδενικό, αν είναι αποτέλεσμα
        elif display.get()=='0' or display.get()=='-0':
            pass
        elif display.get()=='-':
            self.printNumber('-0')                                  # Προσθέτω μόνο 1 μηδενικό, αν υπάρχει '-'
        else:
            display.insert('end','00')                              # Προσθέτω το '00' στην οθόνη από δεξιά
        self.result=False

    def decimalPoint(self,*args):
        txt=display.get()
        if self.result==True:
            display.delete(0, 'end')                                # Διαγραφή ΄΄ο,τι εμφανίζεται ήδη στην οθόνη
            display.insert(0,'0.')                                  # Εκτυπώνω '0.'
        elif '.' in txt:
            pass                                                    # Αν η οθόνη έχει ήδη '.', δεν κάνω τίποτα
        elif txt=='-':
            self.printNumber('-0.')                                 # Αν η οθόνη έχει '-', εκτυπώνω '-0.'
        else:
            display.insert('end', '.')                              # Αλλιώς προσθέτω ένα '-' απο δεξιά
        self.result=False

    def sign(self, *args):
        number=display.get()
        if self.result==True or number=='0':                        # Αν στην οθόνη έχουμε αποτέλεσμα ή το 0
            self.printNumber('-')                                   # Καθαρίζουμε την οθόνη και ξεκινάμε με -
        elif '-' in display.get():                                  # Αν στην οθόνη έχουμε αρνητικό αριθμό ή το -
            if number=='-':                                         # Αν στην οθόνη είναι το -
                number='0'                                          # Θέλουμε να εμφανιστεί το 0
            else:
                number=number[1:]                                   # Αν είναι αρνητικός, διαχωρίζουμε τον αριθμό από το πρόσημο
            self.printNumber(number)                                # Διαγράφουμε οθόνη και γράφουμε 0 ή τον διαχωρισμένο αριθμό
        else:
            display.insert(0, '-')                                  # Αν είναι θετικός και όχι αποτέλεσμα ή 0, βάζουμε ένα - μπροστά
        self.result=False

    def piKey(self):
        self.printNumber(math.pi)
        self.result=False

    def napierConstant(self):
        self.printNumber(math.e)
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

    def cos(self, *args):
        self.secOperation='cos'
        self.secOpSelect()
    
    def tan(self, *args):
        self.secOperation='tan'
        self.secOpSelect()

    def arcSin(self,*args):
        self.secOperation='arcSin'
        self.secOpSelect()

    def arcCos(self,*args):
        self.secOperation='arcCos'
        self.secOpSelect()

    def arcTan(self,*args):
        self.secOperation='arcTan'
        self.secOpSelect()

    def log(self, *args):
        self.secOperation='log'
        self.secOpSelect()

    def ln(self, *args):
        self.secOperation='ln'
        self.secOpSelect()

    def inverse(self,*args):
        self.secOperation='inverse'
        self.secOpSelect()

    def factorial(self,*args):
        self.secOperation='factorial'
        self.secOpSelect()

    def sinh(self, *args):
        self.secOperation='sinh'
        self.secOpSelect()

    def cosh(self, *args):
        self.secOperation='cosh'
        self.secOpSelect()
    
    def tanh(self, *args):
        self.secOperation='tanh'
        self.secOpSelect()

    def arcSinh(self,*args):
        self.secOperation='arcSinh'
        self.secOpSelect()

    def arcCosh(self,*args):
        self.secOperation='arcCosh'
        self.secOpSelect()

    def arcTanh(self,*args):
        self.secOperation='arcTanh'
        self.secOpSelect()

    def memPlus(self,*args):                                        # Πρόσθεση του αριθμού της οθόνης στον αποθηκευμένο στη μν΄΄ήμη αριθμό
        self.memory+=self.inputHandler()
        self.result=True

    def memMinus(self, *args):                                      # Αφαίρεση του αριθμού της οθόνης απο τον αποθηκευμένο αριθμό
        self.memory-=self.inputHandler()
        self.result=True

    def memRecall(self, *args):                                     # Ο αριθμός που είναι αποθηκευμένος στη μνήμη εμφανίζεται στην οθόνη
        self.printNumber(self.memory)
        self.result=False

    def memClear(self, *args):                                      # Εκκαθάριση μνήμης
        self.memory=0

    def memSet(self, *args):                                        # Αποθήκευση του αριθμού που εμφανίζεται στην οθόνη στη μνήμη
        self.memory=self.inputHandler()

    def grandTotal(self, *args):                                    # Λειτουργία γενικού συνόλου (άθροισμα όλων των αποτελεσμάτων)
        self.printNumber(self.grTotal)
        self.result=True

    def mod(self, *args):
        self.opSelect()
        self.operation='mod'
        self.printNumber(self.total)
        self.result=True


    def ceil(self, *args):
        try:
            self.printNumber(math.ceil(self.inputHandler()))
        except:
            self.printNumber('ERROR')
        self.result=True

    def floor(self, *args):
        try:
            self.printNumber(math.floor(self.inputHandler()))
        except:
            self.printNumber('ERROR')
        self.result=True
    
    

calc=SciCalc()

# Δημιουργία όθονης(display) της εφαρμογής.
display=tk.Entry(frame,font=('Helvetica',19,'bold'), bg='lightgreen', fg='black', width=21, justify='right', bd=4, cursor='arrow')
display.grid(padx=5, pady=5, sticky="NSEW")
display.grid_configure(columnspan=5)
display.insert(0, "0")



# Λίστα με τα σύμβολα/ ονόματα για τα πλήκτρα σύνθετων πράξεων.
tags_func=[ 'M-', 'MS', 'GT',
            'π','e','M+'       ,'MR'       ,'MC' ,
            'x^y', 'x^2' ,'sin'      ,'cos'      ,'tan',
            'log','ln' ,'arc\nsin' ,'arc\ncos' ,'arc\ntan',
            '1/x','n!' ,'sinh'     ,'cosh'     ,'tanh',    
            'n√x','2√x','arc\nsinh','arc\ncosh','arc\ntanh']

# Λίστα αντιστοίχισης συναρτήσεων για σύνθετες πράξεις.
functions_1=[calc.memMinus, calc.memSet, calc.grandTotal,
             calc.piKey, calc.napierConstant, calc.memPlus, calc.memRecall, calc.memClear,
             calc.nPower, calc.squared, calc.sin, calc.cos, calc.tan,
             calc.log, calc.ln, calc.arcSin, calc.arcCos, calc.arcTan,
             calc.inverse, calc.factorial, calc.sinh, calc.cosh, calc.tanh,
             calc.nRoot, calc.squareRoot, calc.arcSinh, calc.arcCosh, calc.arcTanh]

# Λίστα με τα μην΄υματα πληροφοριών για κάθε πλήκτρο κατά το mouse-over.
hover_message=['Αφαίρεση αριθμού από την μνήμη','Προσθήκη αριθμού στην μνήμη','Άθροισμα αποτελεσμάτων','Ο αριθμός π', 'Η σταθερά του Νέιπιερ\n(αριθμός Όιλερ)', 'Πρόσθεσε τον αριθμό στην μνήμη', 'Ανάκτηση αριθμού από την μνήμη', 'Καθαρισμός μνήμης',
               'Ύψωση σε δύναμη', 'Ύψωση στο τετράγωνο','Ημίτονο', 'Συνημίτονο', 'Εφαπτομένη',
               'Δεκαδικός Λογάριθμος', 'Φυσικός λογάριθμος', 'Αντίστροφο ημίτονο', 'Αντίστροφο συνημίτονο', 'Αντίστροφη εφαπτομένη',
               'Αντίστροφος', 'Παραγοντικό', 'Υπερβολικό ημίτονο', 'Υπερβολικό συνημίτονο', 'Υπερβολική εφαπτομένη',
               'n-οστή ρίζα του x', 'Τετραγωνική ρίζα του x', 'Αντίστροφο υπερβολικό\n              ημίτονο',
               'Αντίστροφο υπερβολικό\n          συνημίτονο', 'Αντίστροφη υπερβολική\n           εφαπτομένη']

# Λίστα με τα σύμβολα/ ονόματα για τα πλήκτρα απλών πράξεων και λειτουργίες καθαρισμο΄υ οθόνης.
tags_simple=['ceil', 'floor','C' , 'AC', chr(9003),
             '7', '8', '9', '%' , 'mod',
             '4', '5', '6', 'x', '÷',
             '1', '2', '3', '+', '-',
             '0', '.', '00', chr(177), '=']

# Λίστα αντιστοίχισης συναρτήσεων για απλές πράξεις.
functions_2=[   calc.ceil, calc.floor, calc.clear, calc.allClear, calc.backspace,
                calc.num_7, calc.num_8, calc.num_9, calc.percent, calc.mod,
                calc.num_4, calc.num_5, calc.num_6, calc.multiplication, calc.division,
                calc.num_1, calc.num_2, calc.num_3, calc.addition, calc.subtraction,
                calc.num_0, calc.decimalPoint, calc.num_00, calc.sign, calc.equal]

# Μέθοδος για τον επιλογέα εναλλαγής υπολογισμού μοιρών/ακτινίων.
def switch():
    global is_deg

    if is_deg:
        switch_button.config(image = rad)
        is_deg = False
    else:
        switch_button.config(image = deg)
        is_deg = True

def ClickedEntry(*args):                                  # Όταν γίνεται αριστερό κλικ στην οθόνη, επιστρέφει break για να μην εκτελεστεί
    return 'break'

# rad = tk.PhotoImage(file = "./images/Rad.png")
# deg = tk.PhotoImage(file = "./images/Deg.png")


# Path για τα αρχεία εικόνας του επιλογέα μοιρών/ακτινίων.
script_dir = os.path.dirname(os.path.realpath(__file__))
rad = tk.PhotoImage(file=os.path.join(script_dir, "images", "Rad.png"))
deg = tk.PhotoImage(file=os.path.join(script_dir, "images", "Deg.png"))

# Δημιουργία πλήκτρου- επιλογέα εναλλαγής μοιρών ακτινίων.
switch_button=tk.Button(frame, width=2, height=40, image=deg, cursor="exchange", command=switch)
switch_button.grid(row=1, column=0, columnspan=2, pady=5, padx=2, sticky="NSEW")

# Δομές επανάληψης για την δημιουργία πλήκτρων σύνθετων πράξεων.
i=0
button_list=[]
for col in range(2,5):
    if tags_func[i]=='M-' or tags_func[i]=='MS' or tags_func[i]=='GT':
        button_list.append(tk.Button(frame, width=4, height=2, bg='light sea green', fg='red', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i], command=functions_1[i]))
        button_list[i].grid(row=1, column=col, pady=5, padx=2, sticky="NSEW")
    i+=1
for ro in range(2,7):
    for col in range(0,5):
        if tags_func[i]=='M+' or tags_func[i]=='MC' or tags_func[i]=='MR':
            button_list.append(tk.Button(frame, width=4, height=2, bg='light sea green', fg='red', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i],command=functions_1[i]))
            button_list[i].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        else:
            button_list.append(tk.Button(frame, width=4, height=2, bg='black', fg='white', font=('Helvetica', 10, 'bold'), bd=2, text=tags_func[i], command=functions_1[i]))
            button_list[i].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        i+=1

# Δομή επανάληψης για την δημιουργία πλήκτρων απλών πράξεων και αριθμών, όπου κάθε συνθήκη δίνει διαφορετικά χαρακτηριστικά σε κάθε κουμπί.
i=0
for ro in range(8,13):
    for col in range(0,5):
        if tags_simple[i]=='ceil':
            button_list.append(tk.Button(frame, width=5, height=2, bg='darkslategray', fg='lightgoldenrod3',cursor='top_side', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
            Hovertip(button_list[i+28], "Στρογγυλοποίηση προς\nτον μεγαλύτερο ακέραιο", hover_delay=500)
        elif tags_simple[i]=='floor':
            button_list.append(tk.Button(frame, width=5, height=2, bg='darkslategray', fg='lightgoldenrod3',cursor='bottom_side', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
            Hovertip(button_list[i+28], "Στρογγυλοποίηση προς\n τον μικρότερο ακέραιο", hover_delay=500)           
        elif tags_simple[i]=='C' or tags_simple[i]=='AC' or tags_simple[i]==chr(9003):
            button_list.append(tk.Button(frame, width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        elif tags_simple[i]=='+' or tags_simple[i]=='-' or tags_simple[i]=='÷' or tags_simple[i]=='x' or tags_simple[i]== chr(177) or tags_simple[i]== '%':
            button_list.append(tk.Button(frame, width=5, height=2, bg='darkslategray', fg='lightgoldenrod3', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        elif tags_simple[i]=='mod':
            button_list.append(tk.Button(frame, width=5, height=2, bg='darkslategray', fg='lightgoldenrod3', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
            Hovertip(button_list[i+28], "Υπόλοιπο ακέραιας\n         διαίρεσης", hover_delay=500)  
        elif tags_simple[i]=='=':
            button_list.append(tk.Button(frame, width=5, height=2, bg='indianred3', fg='black', activebackground='green', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, columnspan=1, pady=5, padx=2, sticky="NSEW")
        else:
            button_list.append(tk.Button(frame, width=5, height=2, bg='lightblue', activebackground='seagreen1', fg='black', font=('Helvetica', 12, 'bold'), bd=2, text=tags_simple[i],command=functions_2[i]))
            button_list[i+28].grid(row=ro, column=col, pady=5, padx=2, sticky="NSEW")
        i+=1

# Μήνυμα πληροφορίας για το πλήκτρο εναλλαγής μοιρών/ακτινίων.
Hovertip(switch_button, "Κλίκ για εναλλαγή υπολογισμού\n            μοιρών/ ακτινίων", hover_delay=100)

# Δομή επανάληψης για αντιστοίχιση πλήκτρων και μηνυμάτων πληροφορίας.
for i in range(len(tags_func)):
    Hovertip(button_list[i], hover_message[i], hover_delay=500)

# for child in frame.winfo_children():
#    child.grid_configure(sticky='NSEW')


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
root.bind('<KP_Decimal>', calc.decimalPoint)
root.bind('=', calc.equal)
root.bind('<Return>', calc.equal)
root.bind('+', calc.addition)
root.bind('-', calc.subtraction)
root.bind('*', calc.multiplication)
root.bind('/', calc.division)
root.bind('<BackSpace>', calc.backspace)
root.bind('<Escape>', calc.clear)
display.bind('<1>',ClickedEntry)                   # Κάνω την οθόνη να μην δέχεται αριστερό κλικ

root.mainloop()