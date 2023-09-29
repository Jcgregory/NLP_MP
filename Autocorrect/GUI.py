import tkinter as tk
from tkinter import messagebox

def run_main_code():
    language = language_input.get().lower()
    user_input_text = user_input.get()
    
    # Replace these lines with your actual code
    result = f"Language: {language}\nUser Input: {user_input_text}"
    
    # Display the result in a message box
    messagebox.showinfo("Output", result)

# Create the main window
root = tk.Tk()
root.title("Simple Autocorrect GUI")

# Language input
language_label = tk.Label(root, text="Language (en/fa):")
language_label.pack()
language_input = tk.Entry(root)
language_input.pack()

# User input
user_input_label = tk.Label(root, text="Enter words:")
user_input_label.pack()
user_input = tk.Entry(root)
user_input.pack()

# Run button
run_button = tk.Button(root, text="Run Autocorrect", command=run_main_code)
run_button.pack()

# Start the GUI event loop
root.mainloop()
