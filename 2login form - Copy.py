from tkinter import *
root = Tk()
root.title('LOGIN FORM')
root.config(bg='#0B5A81')

f = ('Times', 14)

left_frame = Frame(
    root, 
    bd=2, 
    bg='#CCCCCC',   
    relief=SOLID, 
    padx=10, 
    pady=10
    )

Label(
    left_frame, 
    text="Enter Email", 
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)



email_tf = Entry(
    left_frame, 
    font=f
    )


Label(
    left_frame, 
    text="UserName", 
    bg='#CCCCCC',
    font=f).grid(row=1, column=0, sticky=W, pady=10)

UserName_tf = Entry(
    left_frame, 
    font=f
    )

Label(
    left_frame, 
    text="Login_btn", 
    bg='#CCCCCC',
    font=f).grid(row=4, column=0, sticky=W, pady=10)

Login_btn= Button(
    left_frame, 
    width=15, 
    text='Login', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command = 'wrap'
    )

email_tf.grid(row=0, column=1, pady=10, padx=20)
UserName_tf.grid(row=1,column=1, pady=1, padx=20)

Login_btn.grid(row=4, column=1, pady=10, padx=20)
left_frame.pack()


root.mainloop()
