import tkinter as tk 
import random
from tkinter import messagebox
import string

def generate_password():
    sLow = string.ascii_lowercase
    sUpp = string.ascii_uppercase
    sDigi = string.digits
    sPunct = string.punctuation
    
    all_chars = sLow + sUpp + sDigi + sPunct
    password = random.choice(sLow) + random.choice(sUpp) + \
        random.choice(sDigi) + random.choice(sPunct)
    lenght = 12 
    remaining_chars = random.sample(all_chars, lenght - 4)
    password += "" .join(remaining_chars)
    
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)
    

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Password Copied",
                            "Password has been copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "No Password Generated.")
        

root = tk.Tk()
root.title("password Generated")


password_label = tk.Label(root, text="Generated Password:")
password_label.pack()


password_entry = tk.Entry(root, width=30)
password_entry.pack()


generate_button = tk.Button(
    root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

root.mainloop()

