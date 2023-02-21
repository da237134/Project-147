
from tkinter import*


root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background='#beaff0')

enter_word= Entry(root)
enter_word.place(relx=0.5,rely=0.4, anchor=CENTER)

label = Label(root,text="Name in Ascii : ", bg="#dff0da" , fg ="black")
label2 = Label(root,text="Encrypted Name : ", bg="#dff0da" , fg ="black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + ","
        ascii1 = int(ord(letter))
        encrypted = ascii1 - 1
        label2["text"] += str(chr(encrypted))

btn=Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold', fg ='black')
btn.place(relx=0.5 , rely=0.5, anchor=CENTER) 

label.place(relx=0.5,rely=0.6, anchor=CENTER)  
label2.place(relx=0.5,rely=0.7, anchor=CENTER) 

root.mainloop()
