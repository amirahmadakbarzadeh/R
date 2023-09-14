from tkinter import *
Feild="رشته انسانی در مورد تمدن انسان ها و ویژگی های آنها مطالعه می کند و آموزش می دهد؛"
Feild1="در مورد زبان های مختلف باستانی و مدرن، دین ها و مذهب های مختلف کشور ها،"
Feild2="باستان شناسی و تاریخ، اقتصاد، فلسفه و منطق و… را مورد بررسی قرار می دهد."
def Show():
    def Withdraw(e):
        Window.withdraw()

    #Win
    Window=Tk()
    Window.title("Mathematical Physics")
    Window.geometry("%dx%d+%d+%d"%(810,200,200,100))
    Window.configure(bg="#016A70")
    LaBeL_Lastname = Label(Window, text=Feild, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=100, y=10)
    LaBeL_Lastname = Label(Window, text=Feild1, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=130, y=40)
    LaBeL_Lastname = Label(Window, text=Feild2, font=('Bkoodak', 15, 'bold'), bg="#016A70")
    LaBeL_Lastname.place(x=130, y=70)
    Button_Exit = Button(Window, text="Exit", bg="#FFFFDD", font=('arial', 15, 'bold'), width=20, height=2,bd=5)
    Button_Exit.place(x=300, y=110)
    Button_Exit.bind("<Button-1>",Withdraw)
    Window.mainloop()
