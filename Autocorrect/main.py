import tkinter as tk
from get_words import get_words
from model.pre_process import pre_process

def main():
    gw = get_words()
    pr = pre_process()
    
    
    user_input_text = user_input.get()

    language= "en"
    
    processed_text = pr.process(user_input_text, language)
    
    result = gw.get(processed_text, language)
    

    display_results(result)

def display_results(results):
    result_text.config(state=tk.NORMAL)  
    result_text.delete(1.0, tk.END)  
    
    result_text.insert(tk.END, "Autocorrection Results:\n")
    
    for model, words in results.items():
        result_text.insert(tk.END, f"{model}:\n")
        for index, word in enumerate(words, start=1):
            result_text.insert(tk.END, f"{index}. {word}\n")
    
    result_text.config(state=tk.DISABLED)  



root = tk.Tk()
root.title("Autocorrect GUI")

user_input_label = tk.Label(root, text="Enter words:")
user_input_label.pack()
user_input = tk.Entry(root)
user_input.pack()


run_button = tk.Button(root, text="Run Autocorrect", command=main)
run_button.pack()


result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
result_text.pack()

root.mainloop()
