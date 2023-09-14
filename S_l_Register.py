from tkinter import *
from tkinter import ttk
import messagebox
import About1
import About2
import About3
Feild=[]
Information=[]


#def
def Click(e):
    if Button_Register.cget("state")==NORMAL:
        Dictionary={"Name":Text_Name.get(),"Last Name":Text_Lastname.get(),"Age":int(Text_Age.get()),"Point":int(Text_Point.get()),"Feild":Feild[0]}
        if Exist(Dictionary)==False:
            Registering(Dictionary)
            insert(Dictionary)
            Clear_Text()
        else:
            messagebox.showerror("Rep","فرد مورد نظر تکراری میباشد")
            Clear_Text()
        Table_Search.place_forget()
        #Table.place(x=400, y=80)
        LaBeL_search.place_forget()
def Registering(Value) :
    Information.append(Value)
    print(Information)
    messagebox.showinfo("Registered", "اطلاعات شما با موفقیت ثبت شد")
def Clear_Text():
    # Variables
    Name_variable.set("")
    Lastname_variable.set("")
    Age_variable.set("")
    # focus
    Text_Name.focus_set()
def Delete(e):
    if Text_Delete.get()!=():
        Del=int(Text_Delete.get())
        Table.delete(f'I00{Del}')
        messagebox.showinfo("Delete", "اطلاعات فرد مورد نظر شما با موفقیت پاک شد")
        Delete_variable.set("")
def insert(value):
    Table.insert("","end",values=[value["Name"],value["Last Name"],str(value["Age"]),str(value["Point"]),value["Feild"]])
def insert_Search(value):
    Table_Search.insert("","end",values=[value["Name"],value["Last Name"],str(value["Age"]),str(value["Point"]),value["Feild"]])
def Active_Button(e):
    if Text_Name.get()=="":
        Button_Register.configure(state=DISABLED)
    else :
        Button_Register.configure(state=NORMAL)
def Clear_Text():
    Text_Name.focus_set()
    Name_variable.set("")
    Lastname_variable.set("")
    Age_variable.set("")
    Search_variable.set("")
    Delete_variable.set("")
    Point_variable.set("")
def search(value):
    resultlist = []
    for item in Information:
        if item["Name"] ==Text_Search.get() or item["Last Name"] ==Text_Search.get() or str(item["Age"])==Text_Search.get() or str(item["Point"]==Text_Search) or str(item["Feild"]==Text_Search.get()):
            resultlist.append(item)
    return resultlist

"""        if item["Name"] != Text_Search.get() and item["Last Name"] != Text_Search.get() and str(item["Age"]) != Text_Search.get():
            messagebox.showerror("Exist","فرد مورد نظر شما ثبت نشده است")"""


def getselection(e):
    selection=Table.selection()
    if selection!=():
        s=Table.item(selection)["values"]
        Name_variable.set(s[0])
        Lastname_variable.set(s[1])
        Age_variable.set(s[2])
        Point_variable.set(s[3])
def onclicksearch(e):
    Search=Text_Search.get()
    result=search(Search)
    for item in result:
        insert_Search(item)
    Clear_Text()
    Table_Search.place(x=900,y=90)
    #Table.place_forget()
    LaBeL_search.place(x=900,y=60)
def clear():
    for a in Table.get_children():
        Del_Table=str(a,)
        Table.delete(Del_Table)
    for b in Table_Search.get_children():
        Del_Search=str(b,)
        Table_Search.delete(Del_Search)
def Exist(value):
    for item in Information:
        if item["Name"]==value["Name"] and item["Last Name"]==value["Last Name"] and item["Age"]==value["Age"] and item["Point"]==value["Point"] and item["Feild"]==value["Feild"]:
            return True
    return False
def Onclickdelete(e):
    Ask=messagebox.askyesno("Delete Warning", "آیا اطلاعات فرد مورد نظر شما پاک شود؟")
    if Ask==True:
        Dictionary={"Name":Text_Name.get(),"Last Name":Text_Lastname.get(),"Age":int(Text_Age.get()),"Point":int(Text_Point.get()),"Feild":Feild[0]}
        Delete_Item(Dictionary)
        Remove_Item()
        Clear_Text()
def Delete_Item(value):
    for item in Information:
        if item["Name"]==value["Name"] and item["Last Name"]==value["Last Name"] and item["Age"]==value["Age"] and item["Point"]==value["Point"] and item["Feild"]==value["Feild"]:
            Information.remove(value)
def Remove_Item():
    selection=Table.selection()
    if selection!=():
        Table.delete(selection)
"""def Text_Eror_Reg(value):
    if Text_Name.get()=="":
        Text_Name.configure(bg="red")
        return False
    else:
        Text_Name.configure(bg="#C8FFE0")
        return True
    if Text_Lastname.get()=="":
        Text_Lastname.configure(bg="red")
        return False
    else:
        Text_Lastname.configure(bg="#C8FFE0")
        return True

    if Text_Age.get()=="":
        Text_Age.configure(bg="red")
        return False
    else:
        Text_Age.configure(bg="#C8FFE0")
        return True"""
def onclickclear(e):
    Ask=messagebox.askyesno("Clear Warning" , "آیا از پاک شدن تمام داده ها اطمینان دارید")
    if Ask==True:
        clear()
        Clear_Text()
def onclickupdate(e):
    selct=Table.selection()
    if selct!=():
        select_item=Table.item(selct)["values"]
        dic={"Name":select_item[0],"Last Name":select_item[1],"Age":int(select_item[2]),"Point":int(select_item[3]),"Feild":Feild[0]}
        index1=update(dic)
        p=Information[index1]
        Table.item(selct,values=[p["Name"],p["Last Name"],p["Age"],p["Point"]])



def update(value):
    index=Information.index(value)
    Information[index]={"Name":Text_Name.get(),"Last Name":Text_Lastname.get(),"Age":int(Text_Age.get()),"Point":int(Text_Point.get())}
    return index
def Math(e):
    Feild.clear()
    Feild.append("Mathematical Physics")
    print(Feild)
def Experimental(e):
    Feild.clear()
    Feild.append("Experimental")
    print(Feild)
def Humanities(e):
    Feild.clear()
    Feild.append("Humanities")
    print(Feild)
def about1(e):
    About1.Show()
def about2(e):
    About2.Show()
def about3(e):
    About3.Show()

#Win
Window=Tk()
Window.title("Rigistering")
Window.geometry("%dx%d+%d+%d"%(1300,530,200,100))
image = PhotoImage(file = "Photo2.png",width=1500)
Label(Window, image= image).place(x=-10,y=0)
"""image1 = PhotoImage(file = "Photo.png",width=900)
Label(Window, image= image1).place(x=735,y=0)"""
Window.resizable(False,False)

#Name
#Name_var
Name_variable=StringVar()
#LBL_Name
LaBeL_Name=Label(Window,text="Name",font=('arial', 11, 'bold'),bg="#016A70")
LaBeL_Name.place(x=20,y=20)
#TXT_Name
Text_Name=Entry(Window,bg="#EF9595",bd=8,width=20,justify='center',textvariable=Name_variable)
Text_Name.place(x=75,y=15)
Text_Name.bind("<KeyRelease>",Active_Button)
Text_Name.focus_set()

#Lastname
#Lastname_var
Lastname_variable=StringVar()
#LBL_Lastname
LaBeL_Lastname=Label(Window,text="Last Name",font=('arial', 11, 'bold'),bg="#016A70")
LaBeL_Lastname.place(x=20,y=65)
#TXT_Lastname
Text_Lastname=Entry(Window,bg="#EF9595",bd=8,width=20,justify='center',textvariable=Lastname_variable)
Text_Lastname.place(x=110,y=60)

#Age
#Age_var
Age_variable=StringVar()
#LBL_Age
LaBeL_Age=Label(Window,text="Age",font=('arial', 11, 'bold'),bg="#016A70")
LaBeL_Age.place(x=20,y=110)
#TXTAge
Text_Age=Entry(Window,bg="#EF9595",bd=8,width=20,justify='center',textvariable=Age_variable)
Text_Age.place(x=65,y=105)

#Point
#Point_var
Point_variable=StringVar()
#LBL_Point
LaBeL_Point=Label(Window,text="Point",font=('arial', 11, 'bold'),bg="#016A70")
LaBeL_Point.place(x=20,y=155)
#TXT_Point
Text_Point=Entry(Window,bg="#EF9595",bd=8,width=20,justify='center',textvariable=Point_variable)
Text_Point.place(x=75,y=150)

#Delete
#Delete_Var
Delete_variable=StringVar()
#LBL_Delete
LaBeL_Delete=Label(Window,text="Delete Box",font=('arial', 11, 'bold'),bg="#016A70")
LaBeL_Delete.place(x=20,y=295)
#TXT_Delete
Text_Delete=Entry(Window,bg="#EF9595",bd=8,width=20,justify='center',textvariable=Delete_variable)
Text_Delete.place(x=120,y=290)


#Search
#Search_Var
Search_variable=StringVar()
#TXT_Search
Text_Search=Entry(Window,bg="#EF9595",bd=8,width=40,justify="center",textvariable=Search_variable)
Text_Search.place(x=945,y=12)


#Button
#BTN_Register
Button_Register=Button(Window,text="Register",bg="#FFFFDD",font=('arial',15,'bold'),width=20,height=2,bd=5)
Button_Register.place(x=20,y=200)
Button_Register.configure(state=DISABLED)
#BTN_Delete
Button_Delete=Button(Window,text="Delete",bg="#FFFFDD",font=('arial',15,'bold'),width=30,height=2,bd=5)
Button_Delete.place(x=20,y=345)
#BTN_Search
Button_search=Button(Window,text="Search",bg="#FFFFDD",font=('arial',11,'bold'),width=7,height=1,bd=5)
Button_search.place(x=1210,y=10)
#BTN_ClearAll
Button_Clear=Button(Window,text="Clear All",bg="#FFFFDD",font=('arial',15,'bold'),width=14,height=2,bd=5)
Button_Clear.place(x=20,y=425)
#BTN_Update
Button_Update=Button(Window,text="Update",bg="#FFFFDD",font=('arial',15,'bold'),width=14,height=2,bd=5)
Button_Update.place(x=210,y=425)


#Radio_Button
#Var
Radio_Variable=IntVar()
#Math_Rdo
Math_Rdo=ttk.Radiobutton(Window,variable=Radio_Variable,value=1,text="Mathematical Physics")
Math_Rdo.place(x=260,y=50)
#Experimental_Rdo
Experimental_Rdo=ttk.Radiobutton(Window,variable=Radio_Variable,value=2,text="Experimental")
Experimental_Rdo.place(x=260,y=80)
#Humanities_Rdo
Humanities_Rdo=ttk.Radiobutton(Window,variable=Radio_Variable,value=3,text="Humanities")
Humanities_Rdo.place(x=260,y=110)
#Feild_LBL
Feild_LBL=Label(Window,text="Feilds",font=('arial', 11, 'bold'))
Feild_LBL.place(x=260,y=20)


#Checkbox
Check_variable=IntVar()
checkbox_Male=ttk.Checkbutton(Window,text="Male",variable=Check_variable,onvalue=1)
checkbox_Male.place(x=240,y=145)
checkbox_female=ttk.Checkbutton(Window,text="Female",variable=Check_variable,onvalue=2)
checkbox_female.place(x=310,y=145)
checkbox_nogender=ttk.Checkbutton(Window,text="No Gender",variable=Check_variable,onvalue=3)
checkbox_nogender.place(x=400,y=145)
#About
Check1_variable=IntVar()
checkbox_About1=ttk.Checkbutton(Window,text="About",variable=Check1_variable,onvalue=1)
checkbox_About1.place(x=404,y=50)
checkbox_About2=ttk.Checkbutton(Window,text="About",variable=Check1_variable,onvalue=2)
checkbox_About2.place(x=358,y=80)
checkbox_About3=ttk.Checkbutton(Window,text="About",variable=Check1_variable,onvalue=3)
checkbox_About3.place(x=350,y=110)

#Combo
a=[]
combo=ttk.Combobox(Window)
for i in range(1300,1400):
    a.append(i)
combo["values"]=a
combo.current(88)
combo.place(x=300,y=200)

#Table
Table=ttk.Treeview(Window,show="headings",columns=("Name_Column","Lastname_Column","Age_Column","Point_Column","Feild_Column"))
Table.place(x=500,y=90)
Table.configure(height=19)
Table.heading("Name_Column",text="Name")
Table.column("Name_Column",width=80)
Table.heading("Lastname_Column",text="Last Name")
Table.column("Lastname_Column",width=80)
Table.heading("Age_Column",text="Age")
Table.column("Age_Column",width=50)
Table.heading("Point_Column",text="Point")
Table.column("Point_Column",width=50)
Table.heading("Feild_Column",text="Feild")
Table.column("Feild_Column",width=130)


#Table_Search
Table_Search=ttk.Treeview(Window,show="headings",columns=("Name_Column","Lastname_Column","Age_Column","Point_Column","Feild_Column"))
Table_Search.configure(height=19)
Table_Search.heading("Name_Column",text="Name")
Table_Search.column("Name_Column",width=78)
Table_Search.heading("Lastname_Column",text="Last Name")
Table_Search.column("Lastname_Column",width=78)
Table_Search.heading("Age_Column",text="Age")
Table_Search.column("Age_Column",width=48)
Table_Search.heading("Point_Column",text="Point")
Table_Search.column("Point_Column",width=48)
Table_Search.heading("Feild_Column",text="Feild")
Table_Search.column("Feild_Column",width=130)
#LBL_Search
LaBeL_search=Label(Window,text="Search",font=('arial', 11, 'bold'),bg="#016A70")
LaBeL_search.place(x=880,y=17)
LaBeL_search=Label(Window,text="Search Table",font=('arial', 13, 'bold'),bg="#016A70",width=38)

#Binds
#Register
#if Text_Eror_Reg(1)==True:
#Button_Register.bind("<Button-1>",Text_Eror_Reg)
Button_Register.bind("<Button-1>",Click)
Window.bind("<Return>",Click)
#Claer
Button_Delete.bind("<Button-3>",onclickclear)
#Table
Table.bind("<Button-1>",getselection)
#Search
Button_search.bind("<Button-1>",onclicksearch)
#Clear
Button_Clear.bind("<Button-1>",onclickclear)
#Delete
if Text_Delete.get()=="":
    Button_Delete.bind("<Button-1>", Onclickdelete)
else:
    Button_Delete.bind("<Button-1>",Delete)
#Update
Button_Update.bind("<Button-1>",onclickupdate)
#Radiobutton
#Math
Math_Rdo.bind("<Button-1>",Math)
#Experimental
Experimental_Rdo.bind("<Button-1>",Experimental)
#Humanities
Humanities_Rdo.bind("<Button-1>",Humanities)
#About
checkbox_About1.bind("<Button-1>",about1)
checkbox_About2.bind("<Button-1>",about2)
checkbox_About3.bind("<Button-1>",about3)

Window.mainloop()
