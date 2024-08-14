import tkinter as tk
from tkinter import ttk

class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login Form")

        # Username label and entry
        username_label = ttk.Label(master, text="Username:")
        username_label.pack(pady=10)

        self.username_entry = ttk.Entry(master)
        self.username_entry.pack()

        # Password label and entry
        password_label = ttk.Label(master, text="Password:")
        password_label.pack(pady=10)

        self.password_entry = ttk.Entry(master, show="*")
        self.password_entry.pack()

        # Login button
        login_button = ttk.Button(master, text="Login", command=self.login)
        login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace this with your actual authentication logic
        if username == "user" and password == "password":
            # Successful login
            tk.messagebox.showinfo("Login Successful", "Welcome!")
            self.master.destroy()  # Close the login window
        else:
            # Invalid credentials
            tk.messagebox.showerror("Login Error", "Invalid username or password.")

# Create the main window and run the app
root = tk.Tk()
app = LoginApp(root)
root.mainloop()
