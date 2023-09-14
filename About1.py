from tkinter import *
Feild="ریاضی فیزیک یکی از رشته‌های نظری در متوسطه دوم است که دانش‌آموزان می‌توانند در سال نهم به دهم انتخاب کنند"
Feild1="                                     تمرکز این رشته برروی درس‌های محاسباتی، ریاضی و فیزیک است               "
Feild2="شرایط انتخاب رشته ریاضی فیزیک شامل کسب حد نصاب معدل سه سال متوسطه اول، نمره دروس ریاضی و فیزیک است   "
def Show():
    def Withdraw(e):
        Window.withdraw()

    #Win
    Window=Tk()
    Window.title("Mathematical Physics")
    Window.geometry("%dx%d+%d+%d"%(810,200,200,100))
    Window.configure(bg="#016A70")
    LaBeL_Lastname = Label(Window, text=Feild, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=5, y=10)
    LaBeL_Lastname = Label(Window, text=Feild1, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=-5, y=40)
    LaBeL_Lastname = Label(Window, text=Feild2, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=5, y=70)
    Button_Exit = Button(Window, text="Exit", bg="#FFFFDD", font=('arial', 15, 'bold'), width=20, height=2,bd=5)
    Button_Exit.place(x=300, y=110)
    Button_Exit.bind("<Button-1>",Withdraw)
    Window.mainloop()
