import tkinter as tk
from .base_screen import BaseScreen
from .USKeyboard import USKeyboard
import os
from datetime import datetime
from .config_handler import ConfigHandler

class NewExperiment(BaseScreen):
    def __init__(self, master, app_instance):
        super().__init__(master, "", app_instance, background="../images/new.png")
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config_handler=ConfigHandler()
        # Entry for experiment name with a custom keyboard binding
        self.experiment_name_entry = tk.Entry(self)
        self.experiment_name_entry.bind("<FocusIn>", self.show_keyboard)
        self.experiment_name_entry.place(relx=0.45, rely=0.215)

        #NEW EXPERIMENT
        start_image_path = os.path.join(current_directory, "../buttons/start.png")
        self.start_image = tk.PhotoImage(file=start_image_path)
        start_button = tk.Button(self, image=self.start_image, command=self.start_experiment, borderwidth=0, highlightthickness=0)
        start_button.image = self.start_image  # Keep a reference to avoid garbage collection
        start_button.place(relx=0.25, rely=0.3)  # Center the button


        # Back button
        back_image_path = os.path.join(current_directory, "../buttons/back.png")
        self.start_image = tk.PhotoImage(file=back_image_path)
        back_button = tk.Button(self, image=self.start_image, command=self.back_to_home, borderwidth=0, highlightthickness=0)
        back_button.image = self.start_image  # Keep a reference to avoid garbage collection
        back_button.place(relx=0.45, rely=0.3)  # Center the button


    def start_experiment(self):
        from .reference_sample_screen import ReferenceSample  # Import inside the function
        experiment_name = self.experiment_name_entry.get()
        # Get the current datetime
        now = datetime.now()
        # Format the datetime to "ddmmyyyyhhmmss"
        formatted_dateTime = now.strftime("%d%m%Y%H%M%S")
        formatted_date = now.strftime("%d%m%Y")
        print(formatted_date)
        if experiment_name:
            currentExperiment=experiment_name+"_"+formatted_dateTime
            self.config_handler.set_current_experiment(currentExperiment)
            self.config_handler.set_current_experiment_path(self.curr_dir+"/../RAW_DATA/"+formatted_date+"/"+currentExperiment)
            print(self.curr_dir+"/../RAW_DATA/"+formatted_date+"/"+currentExperiment)
            self.app_instance.switch_screen(ReferenceSample)

    def back_to_home(self):
        from .home_screen import HomeScreen  # Import inside the function
        self.app_instance.switch_screen(HomeScreen)

    def show_keyboard(self, event):
        # If keyboard already exists, bring it to the front
        if hasattr(self, 'keyboard'):
            self.keyboard.lift()
        else:
            # Create and display the custom USKeyboard
            self.keyboard = USKeyboard(self, active_text_widget=self.experiment_name_entry)
            self.keyboard.pack(side=tk.BOTTOM)  # Display the keyboard at the bottom
