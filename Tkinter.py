import tkinter as tk
from tkcalendar import DateEntry
from tkinter.ttk import Label


form=tk.Tk()
canvas=tk.Canvas(form,height=400,width=800)
canvas.pack()

frame_ust=tk.Frame(form,bg="#add8e6")
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)

frame_alt_sol=tk.Frame(form,bg="#add8e6")
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.23,relheight=0.5)

frame_alt_sag=tk.Frame(form,bg="#add8e6")
frame_alt_sag.place(relx=0.34,rely=0.21,relwidth=0.56,relheight=0.5)

hatirlatma_tipi_etiket=Label(frame_ust,background="#add8e6",text="Hatırlatma Tipi:",font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10,pady=10,side="left")

hatirlatma_opsion=tk.StringVar(frame_ust)
hatirlatma_opsion.set("\t")

hatirlatma_acilir=tk.OptionMenu(frame_ust,
hatirlatma_opsion,
"Doğum günü",
"Alışveris")

hatirlatma_acilir.pack(padx=10,pady=10,side="left")

hatirlatma_tarih_secici=DateEntry(frame_ust,width=12,background="orange",foreground="black",borderwidth=1,locale="de_De")
hatirlatma_tarih_secici.pack(padx=30,pady=10,side="right")

hatirlatma_tarihi_etiket=Label(frame_ust,background="#add8e6",text="Hatırlatma Tarihi:",font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=30,pady=10,side="right")

##doğru tanımlamalar

Label(frame_alt_sol,text="Hatırlatma yöntemi:",font="Verdana 10 bold",background="#add8e6").pack(padx=10,pady=10,anchor="nw")
var= tk.IntVar()

R1=tk.Radiobutton(frame_alt_sol,text="Sisteme kaydet",variable=var,value=1,bg="#add8e6",font="Verdana 12")
R1.pack(anchor="nw",pady=5,padx=5)

R2=tk.Radiobutton(frame_alt_sol,text="Eposta gönder",variable=var,value=2,bg="#add8e6",font="Verdana 12")
R2.pack(anchor="nw",pady=5,padx=5)


var1= tk.IntVar()
C1=tk.Checkbutton(frame_alt_sol,text="bir hafta önce",variable=var1,onvalue=1,offvalue=0,bg="#add8e6",font="Verdana 12")
C1.pack(anchor="nw",pady=5,padx=5)

var2= tk.IntVar()
C2=tk.Checkbutton(frame_alt_sol,text="bir gün önce",variable=var2,onvalue=1,offvalue=0,bg="#add8e6",font="Verdana 12")
C2.pack(anchor="nw",pady=5,padx=5)

Label(frame_alt_sag,text="Hatırlatma Mesajı:",font="Verdana 10 bold",background="#add8e6").pack(padx=10,pady=10,anchor="nw")
Text=tk.Text(frame_alt_sag,height=7,width=50,bg="blue")
Text.tag_configure("style",foreground="#bfbfbf",font=("verdana",7,"bold"))
Text.pack(padx=10,pady=10,anchor="nw")

placeholder="Mesajını buraya gir.."
Text.insert(tk.END,placeholder,"style")
from tkinter import messagebox

def gonder():
    last_message=""

    if var.get():
        if var.get()==1:
            last_message+="Veriniz başarıyla sisteme kaydedildi"
        elif var.get()==2:
            last_message+="eposta ile kaydedildi"
        messagebox.showinfo("Başarılı işlem",last_message)
    else:
        messagebox.showwarning("uyarı","işaretleyiniz")
    return
button=tk.Button(frame_alt_sag,text="gönder",command=gonder)
button.pack(anchor="s")

form.mainloop()