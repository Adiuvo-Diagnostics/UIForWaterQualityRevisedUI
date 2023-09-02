from tkinter import *  # import all module inside the tkinter
from datetime import *
import os
from tkinter import messagebox as msg
import tkinter as tk
from PIL import ImageTk, Image

exp = " "  # global variable
flag = 0


class my_key(tk.Frame):
    def __init__(self, master, active_text_widget=None):
        super().__init__(master)
        print("Keyboard initialized")
        self.active_text_widget = active_text_widget
        self.exp = ""  # Replacing the global variable with an instance variable
        test_button = tk.Button(self, text="Test", command=lambda: self.press("Test"))
        test_button.pack()
    def press(self, data):
        self.exp += str(data)

        if self.exp == ' ':
            print("Don't use space at the initial")
            self.exp = ''
        else:
            if self.active_text_widget:
                self.active_text_widget.delete(0, tk.END)  # Clear the current content
                self.active_text_widget.insert(tk.END, self.exp)  # Update with the new content

    # ... (rest of the methods and logic for the keyboard layout/buttons) ...

    def clear(self):
        global exp
        exp = exp[:-1]  ##remove the last character
        self.active_text_widget.set(exp)

    def submit(self, win, geo):
        global exp
        global flag
        Temp_window = Toplevel(win)
        Temp_window.geometry(geo)

        backgroundImage = Image.open("../images/AreYouOkayToCreateNewSample.png")
        resized_image = backgroundImage.resize((1030, 700), Image.ANTIALIAS)
        backgroundImageResized = ImageTk.PhotoImage(resized_image)
        backgroundImageLabel = Label(Temp_window, image=backgroundImageResized, bd=0, bg="#E6ECF0")
        backgroundImageLabel.place(x=0, y=0)

        # user_name = Label(Temp_window,text = "Are you okay to create new sample folder?",font=("Arial", 35)
        #     ,bg=0,fg=0,)
        # user_name.place(x = 60, y = 150)

        num = Button(Temp_window, text='No',
                     highlightthickness=0, bd=0,
                     bg="#004d6c", fg="white",
                     activeforeground="#ffffff", activebackground="#004d6c",
                     font=('Arial', 30, 'bold'),
                     width=10, height=4
                     , command=lambda: self.Value_return(Temp_window, 0))
        num.place(x=150, y=300)

        num = Button(Temp_window, text='Yes',
                     highlightthickness=0, bd=0,
                     bg="#004d6c", fg="white",
                     activeforeground="#ffffff", activebackground="#004d6c",
                     font=('Arial', 30, 'bold'),
                     width=10, height=4,
                     command=lambda: self.NextStep(win))
        num.place(x=600, y=300)

        Temp_window.config(background="#E6ECF0")
        Temp_window.mainloop()  # place window on computer screen, listen for events

    def Button_template(self, win, text, argument, X, Y):
        Button(win, text=text, highlightthickness=0, bd=0,
               bg="#004d6c", fg="white",
               activeforeground="#ffffff", activebackground="#004d6c",
               font=('Arial', 30, 'bold'),
               width=3, height=0
               , command=lambda: self.press(argument)).place(x=X, y=Y)

    def keyboard_button(self, win, geo):
        global exp
        exp = ''
        individual_button_width = 4
        individual_button_height = 3
        sampleIDWindow = Toplevel(win)
        sampleIDWindow.geometry(geo)

        backgroundImage = Image.open("../images/background image 2.png")
        resized_image = backgroundImage.resize((1030, 700), Image.ANTIALIAS)
        backgroundImageResized = ImageTk.PhotoImage(resized_image)
        backgroundImageLabel = Label(sampleIDWindow, image=backgroundImageResized, bd=0, bg="#E6ECF0")
        backgroundImageLabel.place(x=0, y=0)

        Dis_entry = Entry(sampleIDWindow, textvariable=self.active_text_widget, font=("Comic sans", 50))  ### entry Box
        Dis_entry.place(x=100, y=100)

        ##########NUMBER COLUMNM#######################

        Row = 260
        Button_Pos = 95
        position = 50
        letter = "1234567890"
        for i in range(len(letter)):
            self.Button_template(sampleIDWindow, letter[i], letter[i], position, Row)
            position = Button_Pos + position

        # ######################First Row for Letters##################
        Row = Row + 60
        Button_Pos = 95
        position = 50
        letter = "QWERTYUIOP"

        for i in range(len(letter)):
            self.Button_template(sampleIDWindow, letter[i], letter[i], position, Row)
            position = Button_Pos + position

        ### second row of letter##############
        Row = Row + 60
        Button_Pos = 95
        position = 80

        letter = "ASDFGHJKL"

        for i in range(len(letter)):
            self.Button_template(sampleIDWindow, letter[i], letter[i], position, Row)
            position = Button_Pos + position

        ### Third row of letter##############
        Row = Row + 60
        Button_Pos = 95
        position = 150

        letter = "ZXCVBNM"

        for i in range(len(letter)):
            self.Button_template(sampleIDWindow, letter[i], letter[i], position, Row)
            position = Button_Pos + position

        clear = Button(sampleIDWindow, text='Clear',
                       highlightthickness=0, bd=0,
                       bg="#004d6c", fg="white",
                       activeforeground="#ffffff", activebackground="#004d6c",
                       font=('Arial', 30, 'bold'),
                       width=6, height=0,
                       command=self.clear)
        clear.place(x=position, y=Row)

        ### Third row of letter##############
        Row = Row + 60
        Button_Pos = 95
        position = 100
        space_bar = Button(sampleIDWindow, text='SPACE',
                           highlightthickness=0, bd=0,
                           bg="#004d6c", fg="white",
                           activeforeground="#ffffff", activebackground="#004d6c",
                           font=('Arial', 30, 'bold'),
                           width=20, height=0, command=lambda: self.press('_'))
        space_bar.place(x=position, y=Row)

        position = 700
        destroy = Button(sampleIDWindow, text='Back to Menu',
                         highlightthickness=0, bd=0,
                         bg="#006A96", fg="white",
                         activeforeground="#ffffff", activebackground="#006A96",
                         font=('Arial', 30, 'bold'),
                         width=12, height=0,
                         # command=lambda:self.NextStep(sampleIDWindow,"BackToMenu"))
                         command=sampleIDWindow.destroy)
        destroy.place(x=position, y=0)

        position = 600
        enter = Button(sampleIDWindow, text='Submit',
                       highlightthickness=0, bd=0,
                       bg="#006A96", fg="white",
                       activeforeground="#ffffff", activebackground="#006A96",
                       font=('Arial', 30, 'bold'),
                       width=12, height=0,
                       command=lambda: self.submit(sampleIDWindow, geo))
        enter.place(x=position, y=Row)

        sampleIDWindow.config(background="#E6ECF0")
        sampleIDWindow.mainloop()  # place window on computer screen, listen for events
