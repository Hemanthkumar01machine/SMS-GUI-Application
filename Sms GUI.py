import requests
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

class Sms:
    def __init__(self):
        pass
    def code(self):

        def sending(num,mess):
            url="https://www.fast2sms.com/dev/bulk"
            params={
                "authorization":"dkDyMgutmufPdeRGcy35hX9LDUfoBfD2YrGWsjcskrlPh1EIn9ltX1qKFglt",
                "sender_id":"FSTSMS",
                "message":mess,
                "language":"english",
                "route":"p",
                "numbers":num
            }

            response=requests.get(url,params=params)
            result=response.json()
            tk.Label(home_page,text="Last SMS Result :").grid(row=6,column=0,sticky="W")
            tk.Label(home_page,text=result).grid(row=7,column=0,columnspan=3)
            return result.get("return")


        def send_msg():
            mob_number=mobile_number.get()
            mes=message_entry.get("1.0","end")
            variable=sending(mob_number,mes)

            if variable:
                msg.showinfo("Sent","Message Sent Successfully")
            else:
                msg.showwarning("Warning","There Is An Error")
        def reset_message():
            message_entry.delete("1.0","end")

        def reset_number():
            mobile_number.set("")

        def reset_all():
            user_choice=msg.askyesno("Warning","Are You Sure You Want To Reset All?")
            if user_choice==True:
                reset_message()
                reset_number()
        
        home_page=tk.Tk()
        home_page.title("SMS GUI Application")
        home_page.config(background="orange")

        hed_lbl=tk.Label(home_page,text="SMS GUI Application",font=("giddyupstd",27,"bold"),background="orange").grid(row=0,column=0,columnspan=3)

        mobile_number=tk.StringVar()
        mobile_number_lbl=tk.Label(home_page,text="Mobile Number * :",foreground="white",background="orange",font=("jokerman",18)).grid(row=1,column=0,padx=8)
        mobile_number_entry=ttk.Entry(home_page,textvariable=mobile_number,font=("fixedsys",20),width=12)
        mobile_number_entry.grid(row=1,column=1,sticky="W")

        message=tk.StringVar()
        message_lbl=tk.Label(home_page,text="Message * :",foreground="white",background="orange",font=("jokerman",18)).grid(row=2,column=0,sticky="N"+"E",padx=8)
        message_entry=tk.Text(home_page,font=("arialblack",15),height=10,width=25)
        message_entry.grid(row=2,column=1,sticky="W"+"E"+"N"+"S",padx=5,pady=10,rowspan=3)

        send_btn=tk.Button(home_page,text="Send",background="blue",foreground="yellow",border=10,font=("arialblack",15,"bold"),command=send_msg).grid(row=1,column=2)

        reset_all_btn=tk.Button(home_page,text="Reset All",background="red",foreground="black",border=5,font=("arialblack",15,"bold"),command=reset_all).grid(row=2,column=2)

        reset_number_btn=tk.Button(home_page,text="Reset : Number",background="aqua",foreground="green",border=5,font=("arialblack",15,"bold"),command=reset_number).grid(row=3,column=2)

        reset_message_btn=tk.Button(home_page,text="Reset : Message",background="aqua",foreground="green",border=5,font=("arialblack",15,"bold"),command=reset_message).grid(row=4,column=2)


        home_page.mainloop()

if __name__=="__main__":
    obj=Sms
    obj.code("start")