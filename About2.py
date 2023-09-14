from tkinter import *
Feild="درس منحصر به فرد این رشته زیست شناسی است که در هیچکدام از رشته های دیگر ارائه نمی شود"
Feild1=" زیست شناسی مهم ترین و سرنوشت سازترین درس رشته تجربی نیز می باشد و تاثیر بسیار زیادی در رتبه قبولی کنکور دارد"
Feild2="همچنین جالب است بدانید که بزرگ ترین جامعه آماری داوطلبان آزمون سراسری متعلق به رشته تجربی می باشد"
def Show():
    def Withdraw(e):
        Window.withdraw()

    #Win
    Window=Tk()
    Window.title("Experimental")
    Window.geometry("%dx%d+%d+%d"%(850,200,200,100))
    Window.configure(bg="#016A70")
    LaBeL_Lastname = Label(Window, text=Feild, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=70, y=10)
    LaBeL_Lastname = Label(Window, text=Feild1, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=-5, y=40)
    LaBeL_Lastname = Label(Window, text=Feild2, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=50, y=70)
    Button_Exit = Button(Window, text="Exit", bg="#FFFFDD", font=('arial', 15, 'bold'), width=20, height=2,bd=5)
    Button_Exit.place(x=300, y=110)
    Button_Exit.bind("<Button-1>",Withdraw)
    Window.mainloop()
