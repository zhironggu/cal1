from tkinter import *
import math

def click(button):
    str = entryField.get()
    answer=''
    try:
        if button=='C':
            str=str[0:len(str)-1]
            entryField.delete(0,END)
            entryField.insert(0,str)
            return

        elif button=='CE':
            entryField.delete(0,END)
            return

        elif button=='√':
            answer = math.sqrt(eval(str))

        elif button=='π':
            if str == "":
                answer = math.pi 
            else:
                entryField.insert(END,math.pi)
                return

        elif button=='sin':
            answer = math.sin(math.radians(eval(str)))

        elif button=='cos':
            answer = math.cos(math.radians(eval(str)))

        elif button=='tan':
            answer = math.tan(math.radians(eval(str)))

        elif button=='2π':
            if str == "":
                answer = math.pi * 2
            else:
                entryField.insert(END, math.pi * 2)
                return

        elif button=='asin':
            answer = math.asin(math.radians(eval(str)))

        elif button=='acos':
            answer = math.acos(math.radians(eval(str)))

        elif button=='atan':
            answer = math.atan(math.radians(eval(str)))

        elif button==chr(8731):
            answer = eval(str)**(1/3)

        elif button=='x\u02b8':
            entryField.insert(END,'**')
            return

        elif button=='x\u00B3':
            answer = eval(str)**3

        elif button=='x\u00B2':
            answer = eval(str)**2

        elif button=='log2':
            answer = math.log2(eval(str))

        elif button=='deg':
            answer = math.degrees(eval(str))

        elif button=='rad':
            answer = math.radians(eval(str))

        elif button=='e':
             if str=="":
              answer = math.e
             else:
                 entryField.insert(END,math.e)
                 return

        elif button=='lg':
            answer = math.log10(eval(str))

        elif button=='x!':
            answer = math.factorial(eval(str))

        elif button=='/':
            entryField.insert(END,"/")
            return

        elif button=='=':
            answer = eval(str)

        else:
            entryField.insert(END,button)
            return

        entryField.delete(0,END)
        entryField.insert(0,answer)

    except SyntaxError:
                pass


root = Tk()
root.title('Smart Calculator created by Guzhirong')
root.config(bg='dodgerblue2')
root.geometry('660x450')

entryField=Entry(root,font=('Arial',20,'bold'),bg='black',fg='white',bd=20,relief=SUNKEN,width=40)
entryField.grid(row=0,column=0,columnspan=8,pady=20)


button_list = ["C", "CE", "√", "+", "π", "sin",  "cos", "tan",
               "1", "2",  "3", "-", "2π", "asin",  "acos", "asin",
               "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
               "7", "8", "9", "/", "log2", "deg", "rad", "e",
               "-", "0", "%", "=", "lg", "(", ")", "x!"]
row_val=1
col_val=0

for i in button_list:
    button=Button(root,width=6,height=2,bd=2,relief=RAISED,text=i,bg='grey',fg='white',
                  font=('Arial',15,'bold'),command=lambda button=i: click(button))
    button.grid(row=row_val,column=col_val)
    col_val+=1
    if col_val==8:
        col_val=0
        row_val+=1
root.mainloop()