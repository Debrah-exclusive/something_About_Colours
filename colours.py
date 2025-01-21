import tkinter as tk
import random

class ColourChanger:
    def __init__(self, root):
        self.root = root
        self.root.title("Colour Changer")
        self.root.geometry("500x500")
        self.label = tk.Label(root, text="Hello World", font=("Arial", 14))
        self.label.pack(pady=10)

        self.random_colour_button = tk.Button(root, text="Click for Random Colour", command=self.random_colour_change)
        self.random_colour_button.pack(pady=20)

        self.entry = tk.Entry(root, width=10)
        self.entry.pack(pady=50)

        self.colour_change_button = tk.Button(root, text="Change Colour", command=self.colour_change)
        self.colour_change_button.pack(pady=20)

    def random_colour_change(self):
        random_colour = self.generate_random_colour()
        self.root.config(bg=random_colour)
        self.label.config(text=f"You're automatically assigned the colour: {random_colour}")

    def colour_change(self):
        colour = self.entry.get()
        if self.is_valid_colour(colour):
            self.root.config(bg=colour)
            self.label.config(text=f"The colour you want is: {colour}")
        else:
            self.label.config(text="Invalid colour. Please enter a valid hex colour code.")

    def generate_random_colour(self):
        return f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"

    def is_valid_colour(self, colour):
        if len(colour) != 7 or colour[0] != '#':
            return False
        try:
            int(colour[1:], 16)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = ColourChanger(root)
    root.mainloop()