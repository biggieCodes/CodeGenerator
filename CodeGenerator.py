import tkinter as tk
import random
import string

# Create a function to generate a random string
def generate_code():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    code = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=code)

# Create the main application window
app = tk.Tk()
app.title("Code Generator")

# Create a label and entry for code length
length_label = tk.Label(app, text="Code Length:")
length_label.pack()

length_entry = tk.Entry(app)
length_entry.pack()

# Create a button to generate code
generate_button = tk.Button(app, text="Generate Code", command=generate_code)
generate_button.pack()

# Create a label to display the generated code
result_label = tk.Label(app, text="")
result_label.pack()

# Start the Tkinter main loop
app.mainloop()
