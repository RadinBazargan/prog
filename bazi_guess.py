import tkinter as tk
import random as ran
color =["red","yellow","blue","pink","white","black","orange","green","gray"]
fruit =["banana","apple","pineapple","apricot","cherry","grape","orange","pomegranate"]
word = ""
mistakes = 0
namayesh =[]
def update_namayesh():
    lable.config(text=" ".join(namayesh))  
def color_word():
    global mistakes,namayesh,word
    word = ran.choice(color)
    namayesh =["_"] * len(word)
    mistakes = 0
    update_namayesh()
    lable2.config(text=f"mistakes : {mistakes}") 
def fruit_word():
    global mistakes,namayesh,word
    word = ran.choice(fruit)
    namayesh =["_"] * len(word)
    mistakes = 0
    update_namayesh()
    lable2.config(text=f"mistakes : {mistakes}")         
def tryy():
    global mistakes
    char = textt.get().strip().lower()
    textt.delete(0, tk.END)
    if char and len(char) == 1:         
        if char in word:                
            for i, ch in enumerate(word):
                if ch == char:
                    namayesh[i] = char   
            update_namayesh()
        else:                            
            mistakes += 1
            lable2.config(text=f"mistakes: {mistakes}")    
    if  "_" not in namayesh:
        lable.config(text=" ".join(namayesh) + "   You Win!")

win = tk.Tk()
win.geometry('400x400')
but = tk.Button(win,text="try",command=tryy)
but.place(x=200,y=200)
menu1 = tk.Button(win,text='color',fg='blue',command=color_word)
menu1.place(x=100,y=300)
menu2 = tk.Button(win,text='fruit',fg='orange',command=fruit_word)
menu2.place(x=150,y=300)
lable = tk.Label(win,text="word",font='bold')
lable.place(x =150,y=100)
lable2 = tk.Label(win,text="mistakes: 0")
lable2.place(x =300,y=70)
textt = tk.Entry(win,)
textt.place(x =150,y=30)

tk.mainloop()
