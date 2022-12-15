

from tkinter import *

master = Tk()
canvas = Canvas(master,bg= 'indianred',height =1024, width=1895)
canvas.pack()   # pack-place-grid

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

bakiye_butonu = Button(frame_alt_sag, text="Miktar Giriniz", font='Arial 15 bold', bg='#add8e6', width=66, height=8)
bakiye_butonu.pack()

iptal_butonu = Button(frame_iptal, text="İptal", font='Arial 15 bold', bg='#add8e6', width=60, height=6)
iptal_butonu.pack()

master.mainloop()