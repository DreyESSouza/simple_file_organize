import customtkinter as ctk
import logic
from extensions import Extensions

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Organizer")
        self.geometry("270x130")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(self, text="Choose a folder to organize", font=("Arial", 15))
        self.label.grid(row=0, column=0, padx=23, pady=8)

        self.button = ctk.CTkButton(self, text="Click here", command=self.organize)
        self.button.grid(row=1, column=0, padx=23, pady=8)

        self.result = ctk.CTkLabel(self, text="")
        self.result.grid(row=2, column=0, pady=6)

    def show_result(self, selected_folder):
        if selected_folder:
            self.result.configure(text="Files organized successfully!")
        else:
            self.result.configure(text="")

    def organize(self):
        selected_folder = logic.choose_folder()
        logic.select_and_organize(selected_folder, Extensions)
        self.show_result(selected_folder)

if __name__ == "__main__":
    root = Window()
    root.mainloop()