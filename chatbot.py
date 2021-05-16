from tkinter import *
root = Tk()

def send() :
    send = "you =>" +e.get()
    txt.insert(END, "\n".format(send))
    if (e.get() == 'hello') :
        txt.insert(END, "\n" + "Bot => Hi sir")
    elif(e.get() == 'hi') :
        txt.insert(END, "\n" + "Bot => Hello sir")
    elif(e.get() == 'how are you?') :
        txt.insert(END, "\n" + "Bot => fine and you sir ?")
    elif(e.get() == 'fine') :
        txt.insert(END, "\n" + "Bot => nice to hear sir")
    else :
        txt.insert(END, "\n" + "Bot => Sorry I did not get sir!!!")
    e.delete(0, END)

var1 ="chat bot"
txt=Text(root)
txt.grid(row=0, column=0)
e = Entry(root, width=100)
send = Button(root, text="send", bg='black', fg='yellow', command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title(var1)
root.mainloop()
