# -*- coding: utf-8 -*-

import flames_logic as flm
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def creator():
    w=tk.Tk()
    
        
    
    yname=tk.StringVar()
    thname=tk.StringVar()
    def strtfn():
        nm1=yname.get()
        nm2=thname.get()
       # print(nm1,nm2)
        (xop,yop)=flm.printer(nm1.lower(),nm2.lower())
        yop=str(yop)
       # print(xop,yop)
        
        displayer.delete("1.0","end")
        string01=( nm1.upper()+ " & "+ nm2.upper()+"\n"+"Let's See what number  you get   "+ yop+ "\nNow Let's see What letter you get... \n"+ xop+"\n")
        displayer.insert(tk.END, string01)
  #      print("-----------------------------------------")
        
    def dest():
        name_2.delete(0,"end")
        name_1.delete(0,"end")
        displayer.delete("1.0","end")
        
        
      
    def valsender():
        return(yname,thname)  
   
        
    w.title("FLAMES")
    w.geometry("420x450")
    w.configure(bg='crimson')
    w.iconbitmap(r"flames.ico")
    fontis="Segoe Script"
  
    label1=tk.Label(w,text="Enter your name" ,foreground="white",bg="crimson" , font=(fontis,13,"bold"))
    label1.grid(row=1,column=1)
    
    label2=tk.Label(w,text="Enter  their name" ,foreground="white",bg="crimson" ,font=(fontis,13,"bold"))
    label2.grid(row=2,column=1)
    
    name_1=tk.Entry(textvariable=yname , font=(fontis,11),bd=5 ,insertwidth=4, bg="white",relief="ridge")
    name_1.grid(row=1,column=2,pady=5,padx=5)
    name_2=tk.Entry(textvariable=thname, font=(fontis,11),bd=5 ,insertwidth=4, bg="white",relief="ridge")
    name_2.grid(row=2,column=2,pady=5,padx=5)
    
    displayer=ScrolledText(w , foreground="white",bg="crimson",font =(fontis, 13),bd=5 ,relief="ridge")
    displayer.grid(row=5,column=3,pady=5,padx=5)
    displayer.place(x=25,y=200,width=370, height=150)

    namelbl=tk.Label(w,text="\"FLAMES\"", foreground="white",bg="crimson" , font=(fontis,50,"bold"),relief="flat")
    namelbl.grid(row=6,column=2)
    namelbl.place(x=25,y=350)
    


    sub_btn=tk.Button(text="Start",command=strtfn,width=20)
    sub_btn.grid(row=4,column=2,pady=10)
    sub_btn.config(bg="crimson",foreground="white",font=(fontis,10,"bold"),relief=("ridge"),bd=5)
    
    
    clrbtn=tk.Button(w,text="Clear", command=dest,font=(fontis,10,"bold"),relief="sunken")
    clrbtn.grid(row=3,column=2)
    tk.mainloop()

def emp():
    creator()
    
