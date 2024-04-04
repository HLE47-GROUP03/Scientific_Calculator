import tkinter as tk
import math

root=tk.Tk()
root.title('Scientific Calculator')
root.geometry('600x900')
# root.resizable(False, False)
root.resizable(True, True) ## Made it resizable wont deal with frontend right now.

frame=tk.Frame(root)
frame.grid()

class DYNAMIC_CANVAS(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        ## Add text to the canvas
        # self.text_item = self.create_text(580, 150, text="0", font=("Arial", 20), anchor='e')
        self.text_item_0 = self.create_text(580, 50, text="0", font=("Arial", 20), anchor='e')
        self.text_item_1 = self.create_text(580, 100, text="", font=("Arial", 20), anchor='e')
        self.text_item_2 = self.create_text(580, 150, text="", font=("Arial", 20), anchor='e')


        self.update_periodically()
    
    def update_text(self):
        if RAM:  # Check if RAM is not empty
            if len(RAM) >= 3:
                self.itemconfigure(self.text_item_0, text=str(RAM[-3]))
                self.itemconfigure(self.text_item_1, text=str(RAM[-2]))
                if RAM[-1] != None:
                    self.itemconfigure(self.text_item_2, text=str(RAM[-1]))
                else:
                    self.itemconfigure(self.text_item_2, text=0)
            elif len(RAM) == 2 and RAM[-2] != None:
                self.itemconfigure(self.text_item_0, text=str(RAM[-2]))
                self.itemconfigure(self.text_item_1, text=str(RAM[-1]))
                self.itemconfigure(self.text_item_2, text="")
            elif len(RAM) == 1 and RAM[0] != None:
                self.itemconfigure(self.text_item_0, text=str(RAM[-1]))
                self.itemconfigure(self.text_item_1, text="")
                self.itemconfigure(self.text_item_2, text="")
            else:
                self.itemconfigure(self.text_item_0, text="")
                self.itemconfigure(self.text_item_1, text="")
                self.itemconfigure(self.text_item_2, text="")
    
    def update_periodically(self):
        self.update_text()
        self.after(25, self.update_periodically)


class RAM_HANDLER(list):
    ## RAM HANDLER METHODS. 
    ## Validation method on append.
    def __setitem__(self, index, value):
        if isinstance(value, str):
            if '.' in value:
                float_value = float(value)
                super().__setitem__(index, float_value)
            elif value == "":
                super().__setitem__(index, 0)
            else:
                try:
                    int_value = int(value)
                    super().__setitem__(index, int_value)
                except:
                    super().__setitem__(index, value)
        else:
            super().__setitem__(index, value)

    def new_ram_slot(self):
        super().append(None)
    
    def modify_ram_value(self, value):
        ## If the list is empty
        if not self:
            self.append(value)
        elif self[-1] == None:
            self[-1] = value
        else:
            print(self[-1])
            print(value)
            self[-1] = str(self[-1]) + str(value)

class Number_button(tk.Button):
    def __init__(self, master=None, col=None, ro=None, **kw): ## Using **kw to give text to button when creating it
        self.col = col
        self.ro = ro
        self.button_value = kw['text'] if 'text' in kw else ''

        tk.Button.__init__(self, frame, **kw)
        # self.write_number = write_number()

        self.config(width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, command=self.write_number)
        
        self.grid(row=self.ro, column=self.col, pady=5) ## hard coded pady No need to change it on frequently

    ## Custom methods here
    
    def write_number(self):
        RAM.modify_ram_value(self.button_value)
        print(RAM)


## To add one more class for single number operation
        
class Operation_button(tk.Button):
    def __init__(self, master=None, col=None, ro=None, **kw):
        self.col = col
        self.ro = ro
        self.button_value = kw['text'] if 'text' in kw else ''
        tk.Button.__init__(self, master, **kw)

        if self['text'] == '+':
            self.config(width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, command=self.oper_addition)
        elif self['text'] == "sqroot":
            self.config(width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2, command=self.oper_sq_root)
        else:    
            self.config(width=5, height=2, bg='red', fg='white', font=('Helvetica', 12, 'bold'), bd=2)

        self.grid(row=self.ro, column=self.col, pady=5)

        ## Custom methods here

    def oper_addition(self): ## TWO MEMBERS OPERATION EXAMPLE
        ## We check if there is RAM
        RAM.new_ram_slot()
        RAM.modify_ram_value(self.button_value)
        RAM.new_ram_slot()

        print(RAM)

    def oper_sq_root(self): ###### NEA KLASH ME ENA TELESTH DIAFORETIKH ######
    #     ## We check if there is RAM   ###### SHOULD MAKE IT GIVE THE RESULT WHEN OPERATION BUTTON IS PRESSED. HAVE TO THINK BOUT IT
        if RAM:
            ## Caclulating
            result = math.sqrt(RAM[0])
            ## Clearing RAM
            RAM.clear()
            ## Storing result in the first RAM index KEEPING RAM CLEAR ALL THE TIME
            RAM.custom_append(result)
            ## We are deleting the display in order to show result
            display.delete(0, 'end')
            display.insert(0, RAM[0])
        else:
            RAM.custom_append(display.get())
            ## Caclulating
            result = math.sqrt(RAM[0])
            ## Clearing RAM
            RAM.clear()
            ## Storing result in the first RAM index KEEPING RAM CLEAR ALL THE TIME
            RAM.custom_append(result)
            ## We are deleting the display in order to show result
            display.delete(0, 'end')
            display.insert(0, RAM[0])
        

RAM     = RAM_HANDLER() ## There will be added when another function is done a seperator between indexes to know where each element ends We are gonna approach it like this. We are gonna use RAM[0], RAM[1] for storing the operation numbers and RAM[2] to store the result.
MEMORY  = []






i=0
button_list=[]

# display=tk.Entry(frame,font=('Helvetica',20,'bold'), bg='lightgreen', fg='black', width=20, justify='right', bd=5)
# display.grid(padx=5, pady=5, sticky="NEW")
# display.grid_configure(columnspan=5)
# display.insert(0, "0")

display = DYNAMIC_CANVAS(root, width=580, height=200, bg='lightgreen')
display.grid(padx=5, pady=5, sticky="NEW")
display.grid_configure(columnspan=5)            ## There will be stored the memory buttons numbers more like its like STATIC_MEMORY

for ro in range(1, 6):
    for col in range(0, 5):
        # Number_button(root, text=str(i), column=col, row=ro, pady=5)
        Number_button(root, col, ro, text=str(i))
        # Number_button.grid(row=ro, column=col, pady=5)
        print(i)
        i+=1

Operation_button(root, 0, 6, text='+')
Operation_button(root, 1, 6, text='sqroot')


root.mainloop()

