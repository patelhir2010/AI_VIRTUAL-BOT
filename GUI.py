from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("AI ASSISTANT")
root.geometry("600x700")
root.resizable(False, False)
root.config(bg="#aab3bf")  # Soft light blue-gray for the background

# ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->' + user_val + "\n")
    if bot_val != None:
        text.insert(END, "BOT <---" + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->' + send + "\n")
    if bot != None:
        text.insert(END, "BOT <---" + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def del_text():
    text.delete('1.0', "end")

# Frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#FFFFFF")  # Balanced contrast with the background
frame.grid(row=0, column=1, padx=55, pady=10)

# Text label
text_label = Label(frame, text="AI ASSISTANT", font=("Arial", 14, "bold"), bg="#FFFFFF", fg="#2D2D2D")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label = Label(frame, image=image, bg="#FFFFFF")  # Matches the frame
image_label.grid(row=1, column=0, pady=20)

# Adding a text widget
text = Text(root, font=('Arial', 10, 'bold'), bg="#EFEFEF", fg="#2D2D2D", insertbackground="#2D2D2D", highlightthickness=0)
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100)

# Entry widget
entry = Entry(root, justify=CENTER, bg="#EFEFEF", fg="#2D2D2D", insertbackground="#2D2D2D")
entry.place(x=100, y=500, width=375, height=30)

# Button1 - ASK
Button1 = Button(root, text='ASK', bg="#818891", fg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

# Button2 - Send
Button2 = Button(root, text='Send', bg="#818891", fg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

# Button3 - Delete
Button3 = Button(root, text='Delete', bg="#818891", fg="#FFFFFF", pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575)

root.mainloop()
