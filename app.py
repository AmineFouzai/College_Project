import sys
from tkinter import *
import tkinter.ttk as TTK
import tkinter.messagebox as Alert
import sqlite3
import ctypes

#INIT PROGRAM
user32=ctypes.windll.user32
user32.SetProcessDPIAware()
Root= Tk()
Root.title("Tournoi App")
Root.iconbitmap('static/ball.ico')
Width = user32.GetSystemMetrics(0)
Height = user32.GetSystemMetrics(1)
Ratio=200
Root.minsize(width=Width-Ratio,height=Height-Ratio)
Root.maxsize(width=Width,height=Height)
Root.geometry(f"{int(Width-Ratio)}x{int(Height-Ratio)}")
Poules=[chr(_).capitalize() for _ in range(97,105)]

#Globale DataBase Connection
def Connect():
    global Conn,Cursor
    with sqlite3.connect('Poules.db') as Conn:
        Conn=Conn
        Cursor=Conn.cursor()

#Sort Poules With TotalPoint Entry 
def Sort_poules():
    Connect()
    with open('SQL/sort.sql','r') as SQL:
        [Conn.execute(str(SQL.read()).format(Poul,Poul)) for Poul in Poules]
        Conn.commit()  

#Create New Poule   
def Create():
   if not Poul_Name.get() or not  Nom.get()  or not NB_Match.get()  or not Total_Point.get() or not NB_Victoir.get() or not NB_Defait.get() or not NB_Match_Null.get() or not But_Marque.get() or not But_Concede.get():
       Alert.showinfo(title="info",message="All Fields Are Required")
   else :
        Connect()
        for Poul in Poules:
            try:
                with open('SQL/create.sql','r') as SQL:
                    Cursor.execute(str(SQL.read()).format(Poul))
            except Exception as e:
                #No Exception NeedS To Be Handled If Table Exist Pass
                pass
        try:
            with open('SQL/insert.sql','r') as SQL:
                Cursor.execute(str(SQL.read()).format(
                    Poul_Name.get() ,
                    Nom.get() ,
                    NB_Match.get(),
                    Total_Point.get(),
                    NB_Victoir.get(),
                    NB_Defait.get(),
                    NB_Match_Null.get(),
                    But_Marque.get(),
                    But_Concede.get()   ))
                Conn.commit()
                Tree.delete(*Tree.get_children()) 
                Read()
        except  sqlite3.IntegrityError:
            Alert.showinfo('info',f'Poul All Ready Existe With Name: {Nom.get()}')
        except Exception as e:   
            Alert.showinfo(title='info',message=f'NO Such Pouls Called {Poul_Name.get()} Only Accept [A-H]')
            
#Update A Selected Team
def Update():
    if not Tree.selection() and not Poul_Name.get() or not  Nom.get()  or not NB_Match.get()  or not Total_Point.get() or not NB_Victoir.get() or not NB_Defait.get() or not NB_Match_Null.get() or not But_Marque.get() or not But_Concede.get():
        Alert.showinfo(title="info",message="Please Select An Item First")
    else:
        Connect()
        try:
            with open('SQL/update.sql','r') as SQL:
                Cursor.execute(str(SQL.read()).format(
                    Poul_Name.get(),
                    NB_Match.get() ,
                    Total_Point.get(),
                    NB_Victoir.get() ,
                    NB_Defait.get() ,
                    NB_Match_Null.get(),
                    But_Marque.get(),
                    But_Concede.get(),
                    Nom.get() ))
                Conn.commit()
                Tree.delete(*Tree.get_children()) 
                Read()
        except sqlite3.DatabaseError :
            Alert.showinfo(title='info',message=f'NO Such Pouls Called {Poul_Name.get()} Only Accept [A-H]')

#Event Handler For Selecting A Team 
def OnSelected(event):
        Row=Tree.focus()
        Items=Tree.item(Row)
        Values=Items['values']
        Poul_Name.insert(0,Values[0])
        Nom.insert(0,Values[1])     
        NB_Match.insert(0,Values[2]),
        Total_Point.insert(0,Values[3])
        NB_Victoir.insert(0,Values[4])
        NB_Defait.insert(0,Values[5])
        NB_Match_Null.insert(0,Values[6])
        But_Marque.insert(0,Values[7])
        But_Concede.insert(0,Values[8])

#Clear All Entry Widgets From A Selected Team 
def Clear():
        Poul_Name.delete(0,len(Poul_Name.get()))
        Nom.delete(0,len(Nom.get()))     
        NB_Match.delete(0,len(NB_Match.get())),
        Total_Point.delete(0,len(Total_Point.get()))
        NB_Victoir.delete(0,len(NB_Victoir.get()))
        NB_Defait.delete(0,len(NB_Defait.get()))
        NB_Match_Null.delete(0,len(NB_Match_Null.get()))
        But_Marque.delete(0,len(But_Marque.get()))
        But_Concede.delete(0,len(But_Concede.get()))

#Read All Teams From  A DataBase
def Read():
    Connect()
    for Poul in Poules :
        try: 
            with open('SQL/select.sql','r') as SQL:
                for Row in Cursor.execute(str(SQL.read()).format(Poul)):
                    Tree.insert('', 'end', values=(Poul,Row[0], Row[1], Row[2], Row[3],Row[4], Row[5],Row[6],Row[7]))            
        except Exception as e:
            print(e)
    
#Delete a selected Team
def Delete():
    if not Tree.selection():
           Alert.showinfo(title="info",message="Please Select An Item First")
    else:
        Result = Alert.askquestion('Delete', 'Confirm Delete ?', icon="warning")
        if Result == Alert.YES:
            Row = Tree.focus()
            Items =(Tree.item(Row))
            Values= Items['values']
            Tree.delete(Row)
            Connect()
            with open('SQL/delete.sql','r') as SQL:
                Cursor.execute(str(SQL.read()).format(Values[0],Values[1]))
            Conn.commit()
            Alert.showinfo(title="info",message="Deleted Successfully")

#A Callback for Sorting all Teams  
def TreeSort():
    Connect()
    Sort_poules()
    Tree.delete(*Tree.get_children()) 
    Read()

#FRAME WIDGETS
Top = Frame(Root,height=10)
Top.pack(side=TOP)

Left = Frame(Root, width=300, height=500)
Left.pack(side=LEFT)

Right = Frame(Root, width=600, height=500)
Right.pack(side=RIGHT)

Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)

Buttons = Frame(Left, width=300, height=100)
Buttons.pack(side=BOTTOM)


#LABEL WIDGETS
Poul_label = Label(Forms, text="Poul [ A - H ]:", font=('arial', 16), bd=15)
Poul_label.grid(row=0)

Nom_label = Label(Forms, text="Nom de l'Equipe :", font=('arial', 16), bd=15)
Nom_label.grid(row=1)

NB_Match_label = Label(Forms, text="Nombre des Match :", font=('arial', 16), bd=15)
NB_Match_label.grid(row=2)

Total_Point_label = Label(Forms, text="Total Point :", font=('arial', 16), bd=15)
Total_Point_label.grid(row=3)

NB_Victoir_label= Label(Forms, text="Nombre des Victoire :", font=('arial', 16), bd=15)
NB_Victoir_label.grid(row=4)

NB_Defait_label = Label(Forms, text="Nombre des Defait :", font=('arial', 16), bd=15)
NB_Defait_label.grid(row=5)

NB_Match_Null_label= Label(Forms, text="Nombre des Match Null :", font=('arial', 16), bd=15)
NB_Match_Null_label.grid(row=6)

But_Marque_label= Label(Forms, text="But Marque :", font=('arial', 16), bd=15)
But_Marque_label.grid(row=7)

But_Concede_label= Label(Forms, text="But Concede :", font=('arial', 16), bd=15)
But_Concede_label.grid(row=8)

# Txt_result = Label(Buttons)
# Txt_result.pack(side=TOP)

#ENTRY WIDGETS
Poul_Name= Entry(Forms, textvariable="Poul", width=30)
Poul_Name.grid(row=0, column=1,padx="0px 50px")

Nom= Entry(Forms, textvariable="Nom", width=30)
Nom.grid(row=1, column=1,padx="0px 50px")

NB_Match = Entry(Forms, textvariable="NB_Match", width=30)
NB_Match.grid(row=2, column=1,padx="0px 50px")

Total_Point = Entry(Forms, textvariable="Total_Point", width=30)
Total_Point.grid(row=3, column=1,padx="0px 50px")

NB_Victoir= Entry(Forms, textvariable="NB_Victoir", width=30)
NB_Victoir.grid(row=4, column=1,padx="0px 50px")


NB_Defait = Entry(Forms, textvariable="NB_Defait", width=30)
NB_Defait.grid(row=5, column=1,padx="0px 50px")

NB_Match_Null= Entry(Forms, textvariable="NB_Match_Null", width=30)
NB_Match_Null.grid(row=6, column=1,padx="0px 50px")

But_Marque= Entry(Forms, textvariable="But_Marque",  width=30)
But_Marque.grid(row=7, column=1,padx="0px 50px")


But_Concede= Entry(Forms, textvariable="But_Concede",  width=30)
But_Concede.grid(row=8, column=1,padx="0px 50px")


#BUTTONS WIDGET
Btn_create = Button(Buttons, width=10, text="Create", command=Create)
Btn_create.pack(side=LEFT)


Btn_update = Button(Buttons, width=10, text="Update", command=Update)
Btn_update.pack(side=LEFT)

Btn_sort = Button(Buttons, width=10, text="Sort", command=TreeSort)
Btn_sort.pack(side=LEFT)

Btn_delete = Button(Buttons, width=10, text="Delete", command=Delete)
Btn_delete.pack(side=LEFT)


Btn_clear = Button(Buttons, width=10, text="Clear", command=Clear)
Btn_clear.pack(side=LEFT)


#LIST WIDGET
Scrollbary = Scrollbar(Right, orient=VERTICAL)
Scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
Tree = TTK.Treeview(Right, columns=(
    "Poul", 
    "Nom", 
    "NB_Match", 
    "Total_Point",
    "NB_Victoir",
    "NB_Defait", 
    "NB_Match_Null",
    "But_Marque",
    "But_Concede"), 
    selectmode="extended", 
    height=500,
    yscrollcommand=Scrollbary.set,
    xscrollcommand=Scrollbarx.set)

Scrollbary.config(command=Tree.yview)
Scrollbary.pack(side=RIGHT, fill=Y)
Scrollbarx.config(command=Tree.xview)
Scrollbarx.pack(side=BOTTOM, fill=X)



Tree.heading('Poul', text="Poul", anchor=W)
Tree.heading('Nom', text="Nom", anchor=W)
Tree.heading('NB_Match', text="NB_Match", anchor=W)
Tree.heading('Total_Point', text="Total_Point", anchor=W)
Tree.heading('NB_Victoir', text="NB_Victoir", anchor=W)
Tree.heading('NB_Defait', text="NB_Defait", anchor=W)
Tree.heading('NB_Match_Null', text="NB_Match_Null", anchor=W)
Tree.heading('But_Marque', text="But_Marque", anchor=W)
Tree.heading('But_Concede', text="But_Concede", anchor=W)

Tree.column('#0', stretch=NO, minwidth=0, width=0)
Tree.column('#1', stretch=NO, minwidth=0, width=100)
Tree.column('#2', stretch=NO, minwidth=0, width=100)
Tree.column('#3', stretch=NO, minwidth=0, width=100)
Tree.column('#4', stretch=NO, minwidth=0, width=100)
Tree.column('#5', stretch=NO, minwidth=0, width=100)
Tree.column('#6', stretch=NO, minwidth=0, width=100)
Tree.column('#7', stretch=NO, minwidth=0, width=100)
Tree.column('#8', stretch=NO, minwidth=0, width=100)
Tree.column('#9', stretch=NO, minwidth=0, width=100)

Tree.pack()
Tree.bind('<Double-Button-1>',OnSelected)

#Main Program
if __name__ == '__main__':
    Read()
    Root.mainloop()
