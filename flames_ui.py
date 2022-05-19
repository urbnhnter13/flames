# -*- coding: utf-8 -*-

import fl_m_s as flm
import tkinter as tk
def creator():
    w=tk.Tk()
    
        
    
    yname=tk.StringVar()
    thname=tk.StringVar()
    def strtfn():
        nm1=yname.get()
        nm2=thname.get()
       # print(nm1,nm2)
        (xop,yop)=flm.printer(nm1,nm2)
        yop=str(yop)
       # print(xop,yop)
        displayer=tk.Text(w ,foreground="white",bg="crimson", font =(fontis, 13))
        displayer.grid(row=5,column=3,pady=5,padx=5)
        displayer.place(x=10,y=200,width=370, height=150)
        string01=( nm1+ " "+ nm2+"\n"+"Let's See what number  you get   "+ yop+ "\nNow Let's see What letter you get... \n"+ xop+"\n")
        displayer.insert(tk.END, string01)
        print("-----------------------------------------")
        
    def dest():
        name_2.delete(0,"end")
        name_1.delete(0,"end")
        displayer.delete("1.0","3.5")
        
      
    def valsender():
        return(yname,thname)  
   
        
    w.title("Art")
    w.geometry("400x450")
    w.configure(bg='crimson')
    fontis="Segoe Script"
    
    label1=tk.Label(w,text="Enter your name" ,foreground="white",bg="crimson" , font=(fontis,13,"bold"))
    label1.grid(row=1,column=1)
    
    label2=tk.Label(w,text="Enter  their name" ,foreground="white",bg="crimson" ,font=(fontis,13,"bold"))
    label2.grid(row=2,column=1)
    
    name_1=tk.Entry(textvariable=yname , font=(fontis,10),bd=5 ,insertwidth=4, bg="white")
    name_1.grid(row=1,column=3,pady=5,padx=5)
    name_2=tk.Entry(textvariable=thname, font=(fontis,10),bd=5 ,insertwidth=4, bg="white")
    name_2.grid(row=2,column=3,pady=5,padx=5)
    
    displayer=tk.Text(w , foreground="white",bg="crimson",font =(fontis, 13),bd=5 )
    displayer.grid(row=5,column=3,pady=5,padx=5)
    displayer.place(x=20,y=200,width=370, height=150)    
    
    sub_btn=tk.Button(text="Start",command=strtfn,width=20)
    sub_btn.grid(row=4,column=3,pady=15)
    sub_btn.config(bg="crimson")
    
    
    clrbtn=tk.Button(w,text="Clear", command=dest)
    clrbtn.grid(row=3,column=3)
    tk.mainloop()

def emp():
    creator()
    


