import tkinter,tkinter.ttk as ttk
import random



class BaseWindow(tkinter.Tk):
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

        canvas = tkinter.Canvas(self,bg= '#add8e6', height =1024, width=1800)
        canvas.pack()
        bakiye_area=tkinter.Frame(self,bg='#D6E4E5')
        bakiye_area.place(relx=0.37,rely=0.07,relwidth=0.17,relheight=0.05)

        bakiye_text=tkinter.Label(bakiye_area,text="Bakiyeniz:",font="Verdana 12 bold",bg="#D6E4E5")
        bakiye_text.pack(padx=30,pady=10,side="left")

        bakiye_miktar=tkinter.Label(bakiye_area,text="1000 TL",font="Verdana 12 bold",bg="#D6E4E5")
        bakiye_miktar.pack(padx=30,pady=10)

        pin_area=tkinter.Frame(self,bg='#D6E4E5')
        pin_area.place(relx=0.1,rely=0.14,relwidth=0.75,relheight=0.1)

        pin_text=tkinter.Label(pin_area,text="Lütfen Çekmek İstediğiniz Miktarı giriniz.",)
        pin_text.pack(padx=10,pady=10)

        text_area=tkinter.Text(pin_area,height=1,width=30)
        text_area.tag_configure("style",foreground="white")
        text_area.pack()

        number_area=tkinter.Frame(self,bg='#D6E4E5')
        number_area.place(relx=0.1,rely=0.3,relwidth=0.55,relheight=0.5)

        button_area=tkinter.Frame(self,bg='#D6E4E5')
        button_area.place(relx=0.67,rely=0.3,relwidth=0.175,relheight=0.5)
        
        self.EntryFrame=tkinter.Frame(number_area)
        self.PadFrame=tkinter.Frame(number_area)

        self.EntryFrame.pack(padx=15,pady=15)
        self.PadFrame.pack(padx=15,pady=15)

        self.AllButtons=[]
        self.CanWrite=True

        self.Code=args.get("code") or random.randrange(9999)
        self.Timer=args.get("timer") or 2000

        for x in range(1,10):
            
            self.AllButtons.append(ttk.Button(self.PadFrame,width=40,text=x,command=lambda y=x:self.Update(y)))
            self.bind(str(x),lambda CatchEvent,y=x:self.Update(y))

        self.FGridFormatButtons(self.AllButtons)

        self.ZeroButton=ttk.Button(self.PadFrame,width=40,text=0,command=lambda:self.Update(0))
        self.yildizButton=ttk.Button(self.PadFrame,width=40,text="*")
        self.kareButton=ttk.Button(self.PadFrame,width=40,text="#")

        self.SubmitButton=ttk.Button(button_area,width=40,text="enter",command=self.CheckCode)
        self.ClearButton=ttk.Button(button_area,width=40,text="Clear",command=lambda:self.Update(-1))
        self.ExitButton=ttk.Button(button_area,width=40,text="exit")

        self.ZeroButton.grid(row=self.Row,column=1)
        self.yildizButton.grid(row=self.Row,column=0)
        self.kareButton.grid(row=self.Row,column=2)

        self.SubmitButton.grid(padx=10,pady=10)
        self.ClearButton.grid(padx=10,pady=10)
        self.ExitButton.grid(padx=10,pady=10)

        self.bind("0",lambda CatchEvent:self.Update(0))
        self.bind("<Return>",lambda CatchEvent:self.CheckCode())

        self.KeyEnter=ttk.Entry(text_area,state="disabled")
        self.KeyEnter.pack()

        self.after(5,self.Change)

    def Update(self,x):
    
        if self.CanWrite:
            self.KeyEnter["state"]="normal"

            if x==-1:
                self.KeyEnter.delete(0,tkinter.END)
            else:
                self.KeyEnter.insert(tkinter.END,x)

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