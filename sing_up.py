import os
from tkinter import *
from tkinter import ttk
import messagebox


Users=[]
def show_login():
    #def
    def sign_up():
        b = False
        for item in Users:
            if item["User"] == Text_UserName.get():
                messagebox.showinfo("Rep", "Change UserName")
                b = True
                break
        if b == False:
            if Text_Password.get() == Text_RePassword.get():
                dic = {"User": Text_UserName.get(), "Password": Text_Password.get()}
                Users.append(dic)
                print(Users)
            else:
                messagebox.showerror("Error", "Password Error")
    def in_login(e):
        Window.withdraw()
        os.system(f"log_in.py")
    def onclick_singup(e):
        sign_up()
        Window.withdraw()
    #Win
    Window=Tk()
    Window.title("Sing up")
    Window.geometry("%dx%d+%d+%d"%(400,400,550,200))
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
    #LBL_RePassword
    LaBeL_RePassword=Label(Window,text="Repassword",font=('arial', 11, 'bold'),bg="#FEFFAC")
    LaBeL_RePassword.place(x=50,y=140)
    #TXT_RePassword
    Text_RePassword=Entry(Window,bg="#D67BFF",bd=10,width=20,justify='center',textvariable=RePassword_variable)
    Text_RePassword.place(x=150,y=135)
    Text_RePassword.focus_set()

    #LBL_Log_in
    LaBeL_Log_in=Label(Window,text="Log In",font=('arial', 11, 'bold'),bg="#45FFCA")
    LaBeL_Log_in.place(x=175,y=280)
    LaBeL_Log_in.bind("<Button-1>",in_login)

    #Button
    #BTN_Singup
    Button_Singup=Button(Window,text="Sing Up",bg="#FFB6D9",font=('arial',15,'bold'),width=20,height=2,bd=5)
    Button_Singup.place(x=75,y=200)
    Button_Singup.bind("<Button-1>",onclick_singup)
    Window.mainloop()





