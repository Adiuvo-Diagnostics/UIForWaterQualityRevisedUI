import tkinter as tk

class USKeyboard(tk.Frame):
    def __init__(self, master, active_text_widget=None):
        super().__init__(master)
        self.active_text_widget = active_text_widget
        self.shift_active = False  # State for the Shift key
        self.caps_lock_active = False  # State for the Caps Lock key

        # Define the keyboard layout
        keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['Caps Lock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'Enter','DONE'],
            ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift'],
            ['Space']
        ]

        for i, row in enumerate(keys):
            for j, key in enumerate(row):
                button = tk.Button(self, text=key, command=lambda k=key: self.press(k))
                button.grid(row=i, column=j, sticky='nsew', padx=1, pady=1)
                self.grid_columnconfigure(j, weight=1)
            self.grid_rowconfigure(i, weight=1)

    def hide_keyboard(self):
        self.destroy()  # This will "hide" the keyboard

    def press(self, key):
        if key == 'Backspace':
            # Delete the last character
            self.active_text_widget.delete(len(self.active_text_widget.get())-1)
        elif key == 'Shift':
            self.shift_active = not self.shift_active  # Toggle Shift state
        elif key == 'Caps Lock':
            self.caps_lock_active = not self.caps_lock_active  # Toggle Caps Lock state
        elif key == 'Enter':
            self.active_text_widget.insert(tk.END, '\n')  # Insert newline
        elif key == 'DONE':
            self.hide_keyboard()  # Hide the keyboard
        elif key == 'Tab':
            self.active_text_widget.insert(tk.END, '\t')  # Insert tab character
        elif key == 'Space':
            self.active_text_widget.insert(tk.END, ' ')  # Insert space
        else:
            # If Shift or Caps Lock is active, convert key to uppercase.
            # Otherwise, use its original case.
            if self.shift_active or self.caps_lock_active:
                self.active_text_widget.insert(tk.END, key.upper())
                # If just Shift was active (not Caps Lock), turn off Shift after one keypress
                if self.shift_active and not self.caps_lock_active:
                    self.shift_active = False
            else:
                self.active_text_widget.insert(tk.END, key.lower())

