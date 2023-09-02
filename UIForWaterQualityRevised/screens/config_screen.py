import tkinter as tk
from .base_screen import BaseScreen

class ConfigPage(BaseScreen):
    def __init__(self, master, app_instance):
        super().__init__(master, "", app_instance, background="../images/config.png")

        low_level_frame = tk.Frame(self)
        low_level_frame.pack(padx=10, pady=10)

        low_level_label = tk.Label(low_level_frame, text="Low Level Threshold")
        low_level_label.pack(side="left", padx=10, pady=10)
        low_level_label.bind("<Button-1>", lambda event: self.show_entry_widgets(low_level_edittext))

        low_level_edittext = tk.Entry(low_level_frame)
        low_level_edittext.pack(side="left", padx=10, pady=10)
        low_level_edittext.insert(0, "100")  # Set default value
        low_level_edittext.pack_forget()  # Hide the entry widget initially

        high_level_frame = tk.Frame(self)
        high_level_frame.pack(padx=10, pady=10)

        high_level_label = tk.Label(high_level_frame, text="High Level Threshold")
        high_level_label.pack(side="left", padx=10, pady=10)
        high_level_label.bind("<Button-1>", lambda event: self.show_entry_widgets(high_level_edittext))

        high_level_edittext = tk.Entry(high_level_frame)
        high_level_edittext.pack(side="left", padx=10, pady=10)
        high_level_edittext.insert(0, "1000")  # Set default value
        high_level_edittext.pack_forget()  # Hide the entry widget initially

        save_button = tk.Button(self, text="Save", command=self.save_config)
        save_button.pack(pady=20)

        home_button = tk.Button(self, text="Back to Home", command=self.back_to_home)
        home_button.pack(pady=10)

    def show_entry_widgets(self, entry_widget):
        entry_widget.pack()  # Show the entry widget when the label is clicked

    def save_config(self):
        # Implement save config logic
        pass

    def back_to_home(self):
        from .home_screen import HomeScreen  # Import inside the function
        self.app_instance.switch_screen(HomeScreen)
