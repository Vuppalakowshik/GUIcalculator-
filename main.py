import customtkinter

root=customtkinter.CTk()
root.title('Modern Calculator')
root.geometry('300x300')
root.config(bg='black')

entryFeild=customtkinter.CTkEntry(root,font=('arial',20,'bold'),text_color='white',fg_color='black'
                                  ,border_color='white',width=288,height=50,bg_color='black')
entryFeild.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
b7=customtkinter.CTkButton(root,text='7',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b7.grid(row=1,column=0)
b8=customtkinter.CTkButton(root,text='8',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b8.grid(row=1,column=1)
b9=customtkinter.CTkButton(root,text='9',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b9.grid(row=1,column=2)
bplus=customtkinter.CTkButton(root,text='+',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3')
bplus.grid(row=1,column=3)


b4=customtkinter.CTkButton(root,text='4',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b4.grid(row=2,column=0,pady=10)
b5=customtkinter.CTkButton(root,text='5',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b5.grid(row=2,column=1)
b6=customtkinter.CTkButton(root,text='6',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b6.grid(row=2,column=2)
bminus=customtkinter.CTkButton(root,text='-',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3')
bminus.grid(row=2,column=3)


b1=customtkinter.CTkButton(root,text='4',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b1.grid(row=3,column=0,pady=10)
b2=customtkinter.CTkButton(root,text='5',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b2.grid(row=3,column=1)
b3=customtkinter.CTkButton(root,text='6',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b3.grid(row=3,column=2)
bmultiply=customtkinter.CTkButton(root,text='*',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3')
bmultiply.grid(row=3,column=3)


b0=customtkinter.CTkButton(root,text='0',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
b0.grid(row=4,column=0,pady=10)
bdot=customtkinter.CTkButton(root,text='.',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2')
bdot.grid(row=4,column=1)
bclear=customtkinter.CTkButton(root,text='C',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='red',hover_color='red4')
bclear.grid(row=4,column=2)
bdivision=customtkinter.CTkButton(root,text='/',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3')
bdivision.grid(row=4,column=3)

bequal=customtkinter.CTkButton(root,text='=',font=('arial',20,'bold'),width=280,bg_color='black',cursor='hand2',fg_color='green',hover_color='dark green')
bequal.grid(row=5,column=0,columnspan=4)
root.mainloop()