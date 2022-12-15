from tkinter import *

master = Tk()
master.resizable(width=FALSE, height=FALSE)
canvas = Canvas(master,bg= 'indianred', height =650, width=850)
canvas.pack()   # pack-place-grid

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


cekme_butonu = Button(frame_ust_sol, text="Para Çekme", font='Arial 15 bold', bg='#add8e6', width=50, height=8)
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