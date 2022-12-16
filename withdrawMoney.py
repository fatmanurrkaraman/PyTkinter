from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
master = Tk()
canvas = Canvas(master,bg= 'indianred',height =1024, width=1895)
canvas.pack()

frame_ust=Frame(master,bg="#add8e6")
frame_ust.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)


frame_alt=Frame(master,bg="#add8e6")
frame_alt.place(relx=0.3,rely=0.3,relwidth=0.4,relheight=0.1)

frame_alt_sol=Button(master,bg="#add8e6",text="YES",font="Verdana 12 bold",command=lambda: showinfo(
        title='İNFO',
        message='MAKBUZ İSTER MİSİNİZ?')
)

frame_alt_sol.place(relx=0.2,rely=0.46,relwidth=0.1,relheight=0.1)

frame_alt_sag=Button(master,bg="#add8e6",text="NO",font="Verdana 12 bold")
frame_alt_sag.place(relx=0.7,rely=0.46,relwidth=0.1,relheight=0.1)

hatirlatma_tipi_etiket=Label(frame_ust,background="#add8e6",text="ÇEKMEK İSTENEN TUTAR:",font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10,anchor=CENTER)


deposit_money=Label(frame_ust,background="#add8e6",text="1000TL",font="Verdana 12 bold")
deposit_money.pack(padx=10,pady=10,anchor=CENTER)


check_text=Label(frame_alt,background="#add8e6",text="ÇEKMEK İSTEDİĞİNİZ TUTAR DOĞRU MU?",font="Verdana 12 bold")
check_text.pack(anchor=CENTER,pady=40)



master.mainloop()