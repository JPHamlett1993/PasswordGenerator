from tkinter import *
import passwordModule

"""
Clear a text field
"""
def clear_password_text(password_text_field):
    password_text_field.delete(1.0, END)

"""
Sets the text field to the provided string.
"""
def set_password_text(password_text_field, password):
    clear_password_text(password_text_field)
    password_text_field.insert(END, password)

"""
Run the program.
"""
def create_gui():
    root = Tk()

    # Create the window.
    root.title("Password Generator")
    root.geometry("400x200")

    # Create the labels.
    length_label = Label(root, text="Length:")
    length_label.grid(row=0, column=0)
    chars_label = Label(root, text="Characters:")
    chars_label.grid(row=1, column=0)
    ints_label = Label(root, text="Numbers:")
    ints_label.grid(row=2, column=0)
    specials_label = Label(root, text="Special Characters:")
    specials_label.grid(row=3, column=0)
    password_label = Label(root, text="Password:")
    password_label.grid(row=4, column=0)


    # Create the length slider
    length_slider = Scale(root, from_=8, to=25, orient=HORIZONTAL)
    length_slider.grid(row=0, column=1)
    # Create the checkboxes.
    chars_checked_var = IntVar(value=1)
    chars_checkbox = Checkbutton(root, text="Characters", variable=chars_checked_var)
    chars_checkbox.grid(row=1, column=1)
    ints_checked_var = IntVar()
    ints_checkbox = Checkbutton(root, text="Numbers", variable=ints_checked_var)
    ints_checkbox.grid(row=2, column=1)
    specials_checked_var = IntVar()
    specials_checkbox = Checkbutton(root, text="Special Characters", variable=specials_checked_var)
    specials_checkbox.grid(row=3, column=1)
    
    # Create the password label.
    password_text = Text(root, width=30, height=1)
    password_text.grid(row=4, column=1)

    # Create the buttons.
    generate_button = Button(
        root, 
        text="Generate", 
        command=lambda: set_password_text(password_text, passwordModule.generate_password(length_slider.get(), chars_checked_var.get(), ints_checked_var.get(), specials_checked_var.get()))
    )
    generate_button.grid(row=5, column=0)
    clear_button = Button(root, text="Clear", command=lambda: clear_password_text(password_text))
    clear_button.grid(row=5, column=1)

    root.mainloop()

if __name__ == "__main__":
    create_gui()