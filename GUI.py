from tkinter import*
from PIL import Image , ImageTk
import action
import speech_to_text

root = Tk()

root.title("AI ASSISTANT")
root.geometry("550x750")
root.resizable(False,False)




def ask():
    ask_val= speech_to_text.speech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val != None:
       text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()



def send():
   send = entry1.get() 
   bot = action.Action(send)
   text.insert(END, "Me --> "+send+"\n")
   if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
   if bot == "ok sir":
          root.destroy()  
   

def delete_text():
    text.delete("1.0", "end")
 


#frame

frame=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)

#textlabel
Text_lable = Label(frame, text = "AI ASSISTANT" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#356696")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)

#image
image = ImageTk.PhotoImage(Image.open("img/jk.jpg"))
image_lable = Label(frame, image= image)
image_lable.grid(row = 1 ,  column=0 , pady=20)

# Add a text widget
text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100)     

# Add a entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=100 , y = 500 , width= 350, height= 30)

# Add a text button1
button1 =  Button(root,  text="ASK" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 575)

# Add a text button2
button2 =  Button(root,  text="SEND" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=send)
button2.place(x= 400, y= 575)

# Add a text button3
button3 = Button(root, text="DELETE", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 225, y= 575)




root.mainloop()
