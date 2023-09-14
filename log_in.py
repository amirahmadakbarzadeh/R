import os
from tkinter import *
from tkinter import ttk
import messagebox
import sing_up
def sign_up(e):
    sing_up.show_login()

def onclicklogin(e):
    result=login()
    if result:
        Window.withdraw()
        os.system(f"S_l_Register.py")
    else:
        messagebox.showinfo("Error Password or UserName")


def login():
    for item in sing_up.Users:
        if item["User"]==Text_UserName.get() and item["Password"]==Text_Password.get():
            return True
    return False


#Win
Window=Tk()
Window.title("Log in")
Window.geometry("%dx%d+%d+%d"%(400,300,550,200))
Window.configure(bg="#45FFCA")
Window.resizable(False,False)

#UserName
#UserName_var
UserName_variable=StringVar()
#LBL_UserName
LaBeL_UserName=Label(Window,text="User Name",font=('arial', 11, 'bold'),bg="#FEFFAC")
LaBeL_UserName.place(x=50,y=20)
#TXT_UserName
Text_UserName=Entry(Window,bg="#D67BFF",bd=10,width=20,justify='center',textvariable=UserName_variable)
Text_UserName.place(x=150,y=15)
Text_UserName.focus_set()

#Password
#Password_var
Password_variable=StringVar()
#LBL_Password
LaBeL_Password=Label(Window,text="Password",font=('arial', 11, 'bold'),bg="#FEFFAC")
LaBeL_Password.place(x=50,y=80)
#TXT_Password
Text_Password=Entry(Window,bg="#D67BFF",bd=10,width=20,justify='center',textvariable=Password_variable)
Text_Password.place(x=150,y=75)
Text_Password.focus_set()

#RePassword
#RePassword_var
RePassword_variable=StringVar()

#Button
#BTN_Singup
Button_Singup=Button(Window,text="Sing Up",bg="#FFB6D9",font=('arial',15,'bold'),width=20,height=2,bd=5)
Button_Singup.place(x=75,y=150)
Button_Singup.bind("<Button-1>",onclicklogin)

#LBL_Singup
LaBeL_Singup=Label(Window,text="Sing Up",font=('arial', 11, 'bold'),bg="#45FFCA")
LaBeL_Singup.place(x=175, y=230)
LaBeL_Singup.bind("<Button-1>",sign_up)


Window.mainloop(0)





