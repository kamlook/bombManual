# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:52:18 2019

@author: Kam Look
"""
import tkinter as tk

wirearray=[]
serialnumber=''
wireNumber=0 #want to use it for adding block to visualize wires
position=[1,2,3,4,5,6]
def wires():
    global wirearray
    global serialnumber
    if type(serialnumber) != int:
        return messageLbl.config(text='Serial number must be an interger')
    length=len(wirearray)
    valcheck=0
    valcheck2=0
    valcheck3=0
    #three wires
    if length == 3:
        for i in range(length):
            if wirearray[i] == 1:pass
            else:valcheck +=1
        if length <= valcheck:
            return messageLbl.config(text='Cut the second wire')
        else:
            valcheck = 0
        if wirearray[2] == 4:
            return messageLbl.config(text='Cut the last wire')
        #could refine and eliminate with valcheck2
        for i in range(length):
            if wirearray[i] ==5:valcheck +=1
            else:pass
        if valcheck >= 2:
            return messageLbl.config(text='Cut the last blue wire')
        else:
            return messageLbl.config(text='Cut the last wire')
    elif length == 4:
        for i in range(length):
            if wirearray[i]==1: valcheck += 1
            elif wirearray[i]==5: valcheck2 += 1
            else: pass
        if valcheck >= 2 and serialnumber%2==1:
            return messageLbl.config(text='Cut last red wire')
        elif wirearray[3]==2 and valcheck==0:
            return messageLbl.config(text='Cut the first wire')
        elif valcheck2==1:
            return messageLbl.config(text='Cut the first wire')
        else: 
            return messageLbl.config(text='Cut the second wire')
    elif length == 5:
        for i in range(length):
            if wirearray[i]==1: valcheck+=1
            elif wirearray[i] ==2: valcheck2 +=1
            elif wirearray[i]==3: valcheck3 += 1
            else:pass
        if wirearray[4]==5 and serialnumber%2==1:
            return messageLbl.config(text='Cut the fourth wire')
        elif valcheck == 1 and valcheck2 >= 2:
            return messageLbl.config(text='Cut the first wire')
        elif valcheck3==0:
            return messageLbl.config(text='Cut the second wire')
        else:
            return messageLbl.config(text='Cut the first wire')
    elif length == 6:
        for i in range(length):
            if wirearray[i]==2:valcheck +=1
            elif wirearray[i]==4: valcheck2 +=1
            elif wirearray[i]==1: valcheck3 +=1
            else:pass
        if valcheck==0 and serialnumber%2==1:
            return messageLbl.config(text='Cut the third wire')
        elif valcheck==1 and valcheck2 >1:
            return messageLbl.config(text='Cut the fourth wire')
        elif valcheck3==0:
            return messageLbl.config(text='Cut the last wire')
        else:
            return messageLbl.config(text='Cut the fourth wire')
    elif length < 3: return messageLbl.config(text='Not enough wires! Retry arrangement again')
    elif length > 6: return messageLbl.config(text='Too many wires! Retry enter arrangement again')

def createRed():
    wirearray.append(1)
    global wireNumber
    if wireNumber==0:wire1.config(bg='red')
    elif wireNumber==1:wire2.config(bg='red')
    elif wireNumber==2:wire3.config(bg='red')
    elif wireNumber==3:wire4.config(bg='red')
    elif wireNumber==4:wire5.config(bg='red')
    elif wireNumber==5:wire6.config(bg='red')
    elif wireNumber>5:pass
    wireNumber +=1
    return

def createYellow():
    wirearray.append(2)
    global wireNumber
    if wireNumber==0:wire1.config(bg='yellow')
    elif wireNumber==1:wire2.config(bg='yellow')
    elif wireNumber==2:wire3.config(bg='yellow')
    elif wireNumber==3:wire4.config(bg='yellow')
    elif wireNumber==4:wire5.config(bg='yellow')
    elif wireNumber==5:wire6.config(bg='yellow')
    elif wireNumber>5:pass
    wireNumber +=1
    return

def createBlack():
    wirearray.append(3)
    global wireNumber
    if wireNumber==0:wire1.config(bg='black')
    elif wireNumber==1:wire2.config(bg='black')
    elif wireNumber==2:wire3.config(bg='black')
    elif wireNumber==3:wire4.config(bg='black')
    elif wireNumber==4:wire5.config(bg='black')
    elif wireNumber==5:wire6.config(bg='black')
    elif wireNumber>5:pass
    wireNumber +=1
    return

def createWhite():
    wirearray.append(4)
    global wireNumber
    if wireNumber==0:wire1.config(bg='white')
    elif wireNumber==1:wire2.config(bg='white')
    elif wireNumber==2:wire3.config(bg='white')
    elif wireNumber==3:wire4.config(bg='white')
    elif wireNumber==4:wire5.config(bg='white')
    elif wireNumber==5:wire6.config(bg='white')
    elif wireNumber>5:pass
    wireNumber +=1
    return

def createBlue():
    wirearray.append(5)
    global wireNumber
    if wireNumber==0:wire1.config(bg='blue')
    elif wireNumber==1:wire2.config(bg='blue')
    elif wireNumber==2:wire3.config(bg='blue')
    elif wireNumber==3:wire4.config(bg='blue')
    elif wireNumber==4:wire5.config(bg='blue')
    elif wireNumber==5:wire6.config(bg='blue')
    elif wireNumber>5:pass
    wireNumber +=1
    return

def reset():
    #just using wirearray=[] doesn't work because variable is only defined with in the function. method calls wire area as a global function 
    wirearray.clear()
    wire1.config(bg='SystemButtonFace')
    wire2.config(bg='SystemButtonFace')
    wire3.config(bg='SystemButtonFace')
    wire4.config(bg='SystemButtonFace')
    wire5.config(bg='SystemButtonFace')
    wire6.config(bg='SystemButtonFace')
    return messageLbl.config(text='Wires have been reset')

def serialsubmit():
    global serialnumber
    serialnumber=serialenter.get()
    try:
        serialnumber=int(serialnumber)
    except:
        return messageLbl.config(text='Serial number must be an interger')
    else:messageLbl.config(text='')
    return print (serialnumber), serialnumber

def close():
    window.quit()
    window.destroy()
#now we are done defining the functions 

window = tk.Tk()
window.title('Automated Bomb Manual')
window.geometry('500x125')

# =============================================================================
# tab_control = tk.notebook(window)
# tab1 = tk.frame(tab_control)
# tab2 = tk.frame(tab_control)
# tab_control.add(tab1, text='Simple Wires')
# tab_control.add(tab2, text='Button')
# =============================================================================

#lbl=tk.Label(window, text='Select wire color:')
#lbl.grid()
#creating wire colors
btnred = tk.Button(window, text="Red", bg='red', fg='black', cursor='hand2', command=createRed)
btnred.grid(column=0, row=1, padx=10)

btny = tk.Button(window, text="Yellow", bg='yellow', fg='black', cursor='hand2',command=createYellow)
btny.grid(column=1, row=1, padx=10)

btnblk = tk.Button(window, text="Black", bg='black', fg='white', cursor='hand2', command=createBlack)
btnblk.grid(column=2, row=1,padx=10)

btnw = tk.Button(window, text="White", bg='white', fg='black', cursor='hand2', command=createWhite)
btnw.grid(column=3, row=1, padx=10)

btnblu = tk.Button(window, text="Blue", bg='blue', fg='white', cursor='hand2', command=createBlue)
btnblu.grid(column=4, row=1, padx=10)

serialLbl=tk.Label(window, text='Last digit of serial number', wraplength=100)
serialLbl.grid(column=0,row=2)

serialenter=tk.Entry(window, width=5)
serialenter.grid(column=3, row=2, pady=20)

btnserial = tk.Button(window, text="Submit Serial Number", bg='light grey', fg='black', cursor='hand2',command=serialsubmit)
btnserial.grid(column=5, row=2, padx=10)

btnreset = tk.Button(window, text="Reset Arrangement", bg='grey', fg='black', cursor='hand2',command=reset)
btnreset.grid(column=5, row=1, padx=10)

btnsolve = tk.Button(window, text="Solve!", bg='green', activebackground='light green', fg='black', cursor='hand2',command=wires)
btnsolve.grid(column=3, row=3, padx=10)

messageLbl=tk.Label(window, text='', wraplength=150)
messageLbl.place(x=350,y=83)

#btnclose = tk.Button(window,text="Close manual", bg='dark red', activebackground='pink', fg='white', cursor='hand2',command=close)
#btnclose.grid(column=5, row=3, padx=10)
#Setting up visual for entries 

shift=25
wire1= tk.Label(window,text=' ',relief='ridge')
wire1.place(x=25+shift, y=90, width=10, height=10)

wire2= tk.Label(window,text=' ',relief='ridge')
wire2.place(x=50+shift, y=90, width=10, height=10)

wire3= tk.Label(window,text=' ',relief='ridge')
wire3.place(x=75+shift, y=90, width=10, height=10)

wire4= tk.Label(window,text=' ',relief='ridge')
wire4.place(x=100+shift, y=90, width=10, height=10)

wire5= tk.Label(window,text=' ',relief='ridge')
wire5.place(x=125+shift, y=90, width=10, height=10)

wire6= tk.Label(window,text=' ',relief='ridge')
wire6.place(x=150+shift, y=90, width=10, height=10)

window.mainloop()

                
##        print(wirearray)
##        print(length)
#        use%for serial number
#            r=1
#            y=2
#            blk=3
#            wh=4
#            blu=5