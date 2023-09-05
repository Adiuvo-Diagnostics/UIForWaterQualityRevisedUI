import tkinter as tk
from .base_screen import BaseScreen
import os
from .config_handler import ConfigHandler
from tkinter import messagebox


class ConfigPage(BaseScreen):

    def __init__(self, master, app_instance):
        super().__init__(master, "", app_instance, background="../images/config.png")
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config_handler = ConfigHandler()


        # Parent frame to hold the grid
        parent_frame = tk.Frame(self)
        parent_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        low_level_frame = tk.Frame(parent_frame)
        low_level_frame.grid(row=0, column=0, padx=10, pady=10)

        low_level_label = tk.Label(low_level_frame, text="Threshold Delta Peak Counts")
        low_level_label.grid(row=0, column=0, padx=10, pady=10)
        low_level_label.bind("<Button-1>", lambda event: self.show_entry_widgets(self.threshold_delta_peak_edittext))

        self.threshold_delta_peak_edittext = tk.Entry(low_level_frame, name="threshold_delta_peak")
        self.threshold_delta_peak_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.threshold_delta_peak_edittext.insert(0, self.config_handler.get_threshold_delta_peak_counts())  # Set default value

        high_level_frame = tk.Frame(parent_frame)
        high_level_frame.grid(row=1, column=0, padx=10, pady=10)

        high_level_label = tk.Label(high_level_frame, text="Threshold Delta Total Counts")
        high_level_label.grid(row=0, column=0, padx=10, pady=10)
        high_level_label.bind("<Button-1>", lambda event: self.show_entry_widgets(self.threshold_delta_total_edittext))

        self.threshold_delta_total_edittext = tk.Entry(high_level_frame, name="threshold_delta_total")
        self.threshold_delta_total_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.threshold_delta_total_edittext.insert(0, self.config_handler.get_threshold_delta_total_counts())  # Set default value

        # Acquisition Duration Frame
        acquisition_duration_frame = tk.Frame(parent_frame)
        acquisition_duration_frame.grid(row=2, column=0, padx=10, pady=10)

        acquisition_duration_label = tk.Label(acquisition_duration_frame, text="Acquisition Duration (Seconds)")
        acquisition_duration_label.grid(row=0, column=0, padx=10, pady=10)
        acquisition_duration_label.bind("<Button-1>",
                                        lambda event: self.show_entry_widgets(self.acquisition_duration_edittext))

        self.acquisition_duration_edittext = tk.Entry(acquisition_duration_frame, name="acquisition_duration")
        self.acquisition_duration_edittext.grid(row=0, column=1, padx=10, pady=10)
        self.acquisition_duration_edittext.insert(0,self.config_handler.get_acquisition_duration_in_secs())  # Set default value


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

        # Update the JSON object
        self.config_handler.set_threshold_delta_peak_counts(threshold_delta_peak_value)
        self.config_handler.set_threshold_delta_total_counts(threshold_delta_total_value)
        self.config_handler.set_acquisition_duration_in_secs(acquisition_duration_value)

        # Show a messagebox to inform the user
        messagebox.showinfo("Info", "Configuration saved successfully!")

    def back_to_home(self):
        from .home_screen import HomeScreen  # Import inside the function
        self.app_instance.switch_screen(HomeScreen)
