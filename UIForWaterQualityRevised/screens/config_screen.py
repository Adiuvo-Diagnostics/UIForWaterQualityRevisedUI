import tkinter as tk
from .base_screen import BaseScreen
import os
from .config_handler import ConfigHandler
from .USKeyboard import USKeyboard
from tkinter import messagebox


def show_keyboard(self, event):
    self.keyboard.active_text_widget = event.widget
    self.keyboard.deiconify()


class ConfigPage(BaseScreen):
    def show_keyboard(self, event):
        if hasattr(self, "keyboard"):
            self.keyboard.destroy()
        self.keyboard = USKeyboard(self, active_text_widget=event.widget)
        self.keyboard.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def __init__(self, master, app_instance):
        super().__init__(master, "", app_instance, background="../images/config.png")
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config_handler = ConfigHandler()
        self.keyboard = USKeyboard(self)
        self.keyboard.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        self.keyboard.withdraw()



        # Parent frame to hold the grid
        parent_frame = tk.Frame(self)
        parent_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        low_level_frame = tk.Frame(parent_frame)
        low_level_frame.grid(row=0, column=0, padx=10, pady=10)

        low_level_label = tk.Label(low_level_frame, text="Threshold Delta Peak Counts")
        low_level_label.grid(row=0, column=0, padx=10, pady=10)
        low_level_label.bind("<Button-1>", lambda event: self.show_entry_widgets(self.threshold_delta_peak_edittext))

        self.threshold_delta_peak_edittext = tk.Entry(low_level_frame, name="threshold_delta_peak")
        self.threshold_delta_peak_edittext.bind('<FocusIn>', self.show_keyboard)
        self.threshold_delta_peak_edittext.bind('<Button-1>', self.show_keyboard)
        self.threshold_delta_peak_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.threshold_delta_peak_edittext.insert(0,
                                                  self.config_handler.get_threshold_delta_peak_counts())  # Set default value

        high_level_frame = tk.Frame(parent_frame)
        high_level_frame.grid(row=1, column=0, padx=10, pady=10)

        high_level_label = tk.Label(high_level_frame, text="Threshold Delta Total Counts")
        high_level_label.grid(row=0, column=0, padx=10, pady=10)
        high_level_label.bind("<Button-1>", lambda event: self.show_entry_widgets(self.threshold_delta_total_edittext))
        self.threshold_delta_total_edittext = tk.Entry(high_level_frame, name="threshold_delta_total")
        self.threshold_delta_total_edittext.bind('<FocusIn>', self.show_keyboard)
        self.threshold_delta_total_edittext.bind('<Button-1>', self.show_keyboard)
        self.threshold_delta_total_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.threshold_delta_total_edittext.insert(0,
                                                   self.config_handler.get_threshold_delta_total_counts())  # Set default value

        acquisition_duration_frame = tk.Frame(parent_frame)
        acquisition_duration_frame.grid(row=2, column=0, padx=10, pady=10)

        acquisition_duration_label = tk.Label(acquisition_duration_frame, text="Acquisition Duration (Seconds)")
        acquisition_duration_label.grid(row=0, column=0, padx=10, pady=10)
        acquisition_duration_label.bind("<Button-1>",
                                        lambda event: self.show_entry_widgets(self.acquisition_duration_edittext))

        self.acquisition_duration_edittext = tk.Entry(acquisition_duration_frame, name="acquisition_duration")
        self.acquisition_duration_edittext.bind('<FocusIn>', self.show_keyboard)
        self.acquisition_duration_edittext.bind('<Button-1>', self.show_keyboard)
        self.acquisition_duration_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.acquisition_duration_edittext.insert(0,
                                                  self.config_handler.get_acquisition_duration_in_secs())  # Set default value

        # mu1 Frame
        mu1_frame = tk.Frame(parent_frame)
        mu1_frame.grid(row=3, column=0, padx=10, pady=10)

        mu1_label = tk.Label(mu1_frame, text="mu1")
        mu1_label.grid(row=0, column=0, padx=10, pady=10)

        self.mu1_edittext = tk.Entry(mu1_frame, name="mu1")
        self.mu1_edittext.bind('<FocusIn>', self.show_keyboard)
        self.mu1_edittext.bind('<Button-1>', self.show_keyboard)
        self.mu1_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.mu1_edittext.insert(0, self.config_handler.get_mu1())  # Set default value

        # mu2 Frame
        mu2_frame = tk.Frame(parent_frame)
        mu2_frame.grid(row=3, column=1, padx=10, pady=10)

        mu2_label = tk.Label(mu2_frame, text="mu2")
        mu2_label.grid(row=0, column=0, padx=10, pady=10)

        self.mu2_edittext = tk.Entry(mu2_frame, name="mu2")
        self.mu2_edittext.bind('<FocusIn>', self.show_keyboard)
        self.mu2_edittext.bind('<Button-1>', self.show_keyboard)
        self.mu2_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.mu2_edittext.insert(0, self.config_handler.get_mu2())  # Set default value

        # std1 Frame
        std1_frame = tk.Frame(parent_frame)
        std1_frame.grid(row=4, column=0, padx=10, pady=10)

        std1_label = tk.Label(std1_frame, text="std1")
        std1_label.grid(row=0, column=0, padx=10, pady=10)

        self.std1_edittext = tk.Entry(std1_frame, name="std1")
        self.std1_edittext.bind('<FocusIn>', self.show_keyboard)
        self.std1_edittext.bind('<Button-1>', self.show_keyboard)
        self.std1_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.std1_edittext.insert(0, self.config_handler.get_std1())  # Set default value

        # std2 Frame
        std2_frame = tk.Frame(parent_frame)
        std2_frame.grid(row=4, column=1, padx=10, pady=10)

        std2_label = tk.Label(std2_frame, text="std2")
        std2_label.grid(row=0, column=0, padx=10, pady=10)

        self.std2_edittext = tk.Entry(std2_frame, name="std2")
        self.std2_edittext.bind('<FocusIn>', self.show_keyboard)
        self.std2_edittext.bind('<Button-1>', self.show_keyboard)
        self.std2_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.std2_edittext.insert(0, self.config_handler.get_std2())  # Set default value

        #Save
        current_directory = os.path.dirname(os.path.abspath(__file__))
        save_image_path = os.path.join(current_directory, "../buttons/save.png")
        self.save_image = tk.PhotoImage(file=save_image_path)
        save_button = tk.Button(self, image=self.save_image, command=self.save_config, borderwidth=0, highlightthickness=0)
        save_button.image = self.save_image  # Keep a reference to avoid garbage collection
        save_button.place(relx=0.30, rely=0.7)  # Center the button


        #HOME
        current_directory = os.path.dirname(os.path.abspath(__file__))
        home_image_path = os.path.join(current_directory, "../buttons/homeButton.png")
        self.home_image = tk.PhotoImage(file=home_image_path)
        home_button = tk.Button(self, image=self.home_image, command=self.back_to_home, borderwidth=0, highlightthickness=0)
        home_button.image = self.home_image  # Keep a reference to avoid garbage collection
        home_button.place(relx=0.55, rely=0.7)  # Center the button


    def show_entry_widgets(self, entry_widget):
        entry_widget.pack()  # Show the entry widget when the label is clicked

    def save_config(self):
        # Get the values from the Entry widgets
        threshold_delta_peak_value = self.threshold_delta_peak_edittext.get()
        threshold_delta_total_value = self.threshold_delta_total_edittext.get()
        acquisition_duration_value = self.acquisition_duration_edittext.get()
        mu1 = self.mu1_edittext.get()
        mu2 = self.mu1_edittext.get()
        std1 = self.std1_edittext.get()
        std2 = self.std2_edittext.get()

        # Update the JSON object
        self.config_handler.set_threshold_delta_peak_counts(threshold_delta_peak_value)
        self.config_handler.set_threshold_delta_total_counts(threshold_delta_total_value)
        self.config_handler.set_acquisition_duration_in_secs(acquisition_duration_value)
        self.config_handler.set_mu1(mu1)
        self.config_handler.set_mu2(mu2)
        self.config_handler.set_std1(std1)
        self.config_handler.set_std2(std2)

        # Show a messagebox to inform the user
        messagebox.showinfo("Info", "Configuration saved successfully!")

    def back_to_home(self):
        from .home_screen import HomeScreen  # Import inside the function
        self.app_instance.switch_screen(HomeScreen)
