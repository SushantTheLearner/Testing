import tkinter as tk
import webbrowser
import pyautogui
import time
import random


name = ""
question_index = 0
questions = [
    "chappan chale street food khane??",
    "mausam kitna accha hai na Long drive pe chale",
    "Shopping karne chale??",
    "Movie chaloge??",
]


def submit_name():
    global name
    name = name_entry.get()
    greeting_label.config(text=f"Hello, {name}, Ji")
    name_entry.delete(0, tk.END)
    

    instruction_label.config(text="Please install library pyautogui by 'pip install pyautogui' ")
    instruction_label.pack(pady=10)
    
    
    next_button.config(state=tk.NORMAL)


def rotate_questions():
    global question_index
    question_label.config(text=f"{name}, {questions[question_index]}", fg="dodger blue") 
    question_index = (question_index + 1) % len(questions)
    root.after(3000, rotate_questions)  


def next_question():
    if name:
        greeting_label.pack_forget()
        name_entry.pack_forget()  
        instruction_label.pack_forget()
        submit_button.pack_forget()  
        next_button.pack_forget() 
        
        question_label.pack(pady=50)
        rotate_questions() 
        
        
        yes_button.place(relx=0.35, rely=0.7, anchor="center")  
        no_button.place(relx=0.65, rely=0.7, anchor="center")   


def move_no_button(event):
    no_button.place_forget()
    x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    y = random.randint(0, root.winfo_height() - no_button.winfo_height())
    no_button.place(x=x, y=y)


def yes_button_click():
    if name:
        
        webbrowser.open("https://wa.me/+919893549116") 
        time.sleep(10)
        
        
        message = "Yes, Sushant i want to come with you"
        pyautogui.typewrite(message)
        pyautogui.press('enter')


root = tk.Tk()
root.title("Simple Tkinter Window")


root.configure(bg='deep pink')
root.geometry("500x400")


name_entry = tk.Entry(root, font=("Helvetica", 14))
name_entry.insert(0, "Enter your name")
name_entry.bind("<FocusIn>", lambda args: name_entry.delete('0', 'end'))
name_entry.pack(pady=30)


submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=submit_name, bg="lightblue")
submit_button.pack(pady=10)


greeting_label = tk.Label(root, text="", font=("Helvetica", 16), fg="darkblue")  
greeting_label.pack(pady=20)


instruction_label = tk.Label(root, text="", font=("Helvetica", 12))


next_button = tk.Button(root, text="Next", font=("Helvetica", 14), command=next_question, bg="dodger blue", state=tk.DISABLED)
next_button.pack(pady=20)


question_label = tk.Label(root, text="", font=("Helvetica", 16), fg="dodger blue") 


yes_button = tk.Button(root, text="Yes", font=("Helvetica", 14), bg="blue", command=yes_button_click)
no_button = tk.Button(root, text="No", font=("Helvetica", 14), bg="yellow")
no_button.bind("<Enter>", move_no_button)


root.mainloop()
