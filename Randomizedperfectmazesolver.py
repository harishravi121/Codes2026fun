 #write a python gui to display a random no on button click and show 3 more dummy buttons how to embed flood fill by asking gemini or seeing git hub codes made for robotic maze solver for floodfill humanization

import tkinter as tk
import random
#IF you want to use a heavy laptop or embed the code in a car or microcontroller with LCD Display
def show_random_number():
    # Generate a random integer between 1 and 100
    num = random.choice(['left','right','straight','back'])
    # Update the label text
    result_label.config(text=f"Result: {num}")

# Initialize the main window
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("300x250")

# The functional button
btn_main = tk.Button(root, text="Click for Random Number", command=show_random_number, bg="#4CAF50", fg="white")
btn_main.pack(pady=10)

# The display label
result_label = tk.Label(root, text="Result: --", font=("Arial", 14))
result_label.pack(pady=10)

# The 3 Dummy Buttons
for i in range(1, 4):
    dummy_btn = tk.Button(root, text=f"Dummy Button {i}", state="disabled")
    dummy_btn.pack(pady=5)

# Start the application
root.mainloop()
