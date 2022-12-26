from tkinter import *
import random

master = Tk()
master.resizable(width=FALSE, height=FALSE)
canvas = Canvas(master,bg= 'indianred', height =650, width=850)
canvas.pack()   # pack-place-grid

def withdraw_page2():
 class BaseWindow(Tk):
    def Change(self):
        x,y=self.winfo_width(),self.winfo_height()

        self.minsize(x,y); self.maxsize(x,y)

    def FGridFormatButtons(self,ButtonList,NewLineAmount=3):
        self.Row=0
        self.Col=0

        for Button in ButtonList:
            Button.grid(row=self.Row,column=self.Col)

            self.Col+=1

            if self.Col==NewLineAmount:
                self.Row+=1
                self.Col=0
                continue

 class Window(BaseWindow):
    def __init__(self,**args):
        super(Window,self).__init__()

        canvas = Canvas(self,bg= '#add8e6', height =1024, width=1800)
        canvas.pack()
        bakiye_area=Frame(self,bg='#D6E4E5')
        bakiye_area.place(relx=0.37,rely=0.07,relwidth=0.17,relheight=0.05)

        bakiye_text=Label(bakiye_area,text="Bakiyeniz:",font="Verdana 12 bold",bg="#D6E4E5")
        bakiye_text.pack(padx=30,pady=10,side="left")

        bakiye_miktar=Label(bakiye_area,text="1000 TL",font="Verdana 12 bold",bg="#D6E4E5")
        bakiye_miktar.pack(padx=30,pady=10)

        pin_area=Frame(self,bg='#D6E4E5')
        pin_area.place(relx=0.1,rely=0.14,relwidth=0.75,relheight=0.1)

        pin_text=Label(pin_area,text="Lütfen Çekmek İstediğiniz Miktarı giriniz.",)
        pin_text.pack(padx=10,pady=10)

        text_area=Text(pin_area,height=1,width=30)
        text_area.tag_configure("style",foreground="white")
        text_area.pack()

        number_area=Frame(self,bg='#D6E4E5')
        number_area.place(relx=0.1,rely=0.3,relwidth=0.55,relheight=0.5)

        button_area=Frame(self,bg='#D6E4E5')
        button_area.place(relx=0.67,rely=0.3,relwidth=0.175,relheight=0.5)
        
        self.EntryFrame=Frame(number_area)
        self.PadFrame=Frame(number_area)

        self.EntryFrame.pack(padx=15,pady=15)
        self.PadFrame.pack(padx=15,pady=15)

        self.AllButtons=[]
        self.CanWrite=True

        self.Code=args.get("code") or random.randrange(9999)
        self.Timer=args.get("timer") or 2000

        for x in range(1,10):
            
            self.AllButtons.append(Button(self.PadFrame,width=40,text=x,command=lambda y=x:self.Update(y)))
            self.bind(str(x),lambda CatchEvent,y=x:self.Update(y))

        self.FGridFormatButtons(self.AllButtons)

        self.ZeroButton=Button(self.PadFrame,width=40,text=0,command=lambda:self.Update(0))
        self.yildizButton=Button(self.PadFrame,width=40,text="*")
        self.kareButton=Button(self.PadFrame,width=40,text="#")

        self.SubmitButton=Button(button_area,width=40,text="GİRİŞ",command=self.CheckCode)
        self.ClearButton=Button(button_area,width=40,text="TEMİZLE",command=lambda:self.Update(-1))
        self.ExitButton=Button(button_area,width=40,text="ÇIK")

        self.ZeroButton.grid(row=self.Row,column=1)
        self.yildizButton.grid(row=self.Row,column=0)
        self.kareButton.grid(row=self.Row,column=2)

        self.SubmitButton.grid(padx=10,pady=10)
        self.ClearButton.grid(padx=10,pady=10)
        self.ExitButton.grid(padx=10,pady=10)

        self.bind("0",lambda CatchEvent:self.Update(0))
        self.bind("<Return>",lambda CatchEvent:self.CheckCode())

        self.KeyEnter=Entry(text_area,state="disabled")
        self.KeyEnter.pack()

        self.after(5,self.Change)

    def Update(self,x):
    
        if self.CanWrite:
            self.KeyEnter["state"]="normal"

            if x==-1:
                self.KeyEnter.delete(0,END)
            else:
                self.KeyEnter.insert(END,x)

            self.KeyEnter["state"]="disabled"
    
    def CheckCode(self):
        Key=self.KeyEnter.get()

        self.Update(-1)

        if Key==str(self.Code):
            self.after(self.Timer,self.destroy)
        

        self.ChangeWritePerms()

        self.after(self.Timer,self.ChangeWritePerms)

    def ChangeWritePerms(self):
        if self.CanWrite:
            self.CanWrite=False
        else:
            self.CanWrite=True
            self.Update(-1)
 Window().mainloop()
    



def withdraw_page():
    frame_ust = Frame(master, bg= 'indianred',)
    frame_ust.place(relx=0.1, rely=0.01, relheight=0.1,relwidth=0.8)

    frame_ust_sol = Frame(master, bg='#add8e6')
    frame_ust_sol.place(relx=0.02, rely=0.15, relwidth=0.4, relheight=0.17)

    frame_alt_sol = Frame(master, bg='#add8e6')
    frame_alt_sol.place(relx=0.02, rely=0.4, relwidth=0.4, relheight=0.17)

    frame_ust_sag = Frame(master, bg='#add8e6')
    frame_ust_sag.place(relx=0.58, rely=0.15, relwidth=0.4, relheight=0.17)

    frame_alt_sag = Frame(master, bg='#add8e6')
    frame_alt_sag.place(relx=0.58, rely=0.4, relwidth=0.4, relheight=0.17)

    frame_iptal = Frame(master, bg='#add8e6')
    frame_iptal.place(relx=0.02, rely=0.75, relwidth=0.3, relheight=0.1)

    seciniz_etiketi = Label(frame_ust, bg='indianred', text= "Bakiyeniz:", font="Verdana 18 bold")
    seciniz_etiketi.pack(padx=10, pady=20, side=TOP)


    cekme_butonu = Button(frame_ust_sol, text="20 TL", font='Arial 15 bold', bg='#add8e6', width=66, height=8)
    cekme_butonu.pack()

    transfer_butonu = Button(frame_ust_sag, text="40 TL", font='Arial 15 bold', bg='#add8e6', width=66, height=8)
    transfer_butonu.pack()

    mevduat_butonu = Button(frame_alt_sol, text="100 TL", font='Arial 15 bold', bg='#add8e6', width=66, height=8)
    mevduat_butonu.pack()

    bakiye_butonu = Button(frame_alt_sag, text="Miktar Giriniz", font='Arial 15 bold', bg='#add8e6', width=66, height=8,command=lambda: withdraw_page2())
    bakiye_butonu.pack()

    iptal_butonu = Button(frame_iptal, text="İptal", font='Arial 15 bold', bg='#add8e6', width=60, height=6)
    iptal_butonu.pack()



frame_ust = Frame(master, bg='indianred')
frame_ust.place(relx=0.1, rely=0.01, relheight=0.1)

frame_ust_sol = Frame(master, bg='#add8e6')
frame_ust_sol.place(relx=0.02, rely=0.15, relwidth=0.4, relheight=0.17)

frame_alt_sol = Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.02, rely=0.4, relwidth=0.4, relheight=0.17)

frame_ust_sag = Frame(master, bg='#add8e6')
frame_ust_sag.place(relx=0.58, rely=0.15, relwidth=0.4, relheight=0.17)

frame_alt_sag = Frame(master, bg='#add8e6')
frame_alt_sag.place(relx=0.58, rely=0.4, relwidth=0.4, relheight=0.17)

frame_iptal = Frame(master, bg='#add8e6')
frame_iptal.place(relx=0.02, rely=0.75, relwidth=0.3, relheight=0.1)

seciniz_etiketi = Label(frame_ust, bg='indianred', text= "LÜTFEN İŞLEM SEÇİNİZ", font="Verdana 18 bold")
seciniz_etiketi.pack(padx=180, pady=20, side=TOP)


cekme_butonu = Button(frame_ust_sol, text="Para Çekme", font='Arial 15 bold', bg='#add8e6', width=50, height=8,command=lambda: withdraw_page())
cekme_butonu.pack()

transfer_butonu = Button(frame_ust_sag, text="Para Transfer", font='Arial 15 bold', bg='#add8e6', width=50, height=8)
transfer_butonu.pack()

mevduat_butonu = Button(frame_alt_sol, text="Mevduat Çeki", font='Arial 15 bold', bg='#add8e6', width=50, height=8)
mevduat_butonu.pack()

bakiye_butonu = Button(frame_alt_sag, text="Bakiye Sorgulama", font='Arial 15 bold', bg='#add8e6', width=50, height=8)
bakiye_butonu.pack()

iptal_butonu = Button(frame_iptal, text="İptal", font='Arial 15 bold', bg='#add8e6', width=30, height=6)
iptal_butonu.pack()

master.mainloop()