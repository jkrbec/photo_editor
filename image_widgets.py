import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *

class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_function):
        super().__init__(master = parent)
        self.grid(column = 0, columnspan = 2, row = 0, sticky = "nsew")
        self.import_function = import_function

        ctk.CTkButton(master = self, text = "Open Image", command=self.open_dialog).pack(expand = True)

    def open_dialog(self):
        path = filedialog.askopenfilename()
        self.import_function(path)

class ImageOutput(Canvas):
    def __init__(self, parent, resize_image):
        super().__init__(master = parent, 
                         background = BACKGROUND_COLOR, highlightthickness = 0,
                         borderwidth = 0, relief = "ridge")
        self.grid(column = 1, row = 0, sticky = "nsew", padx = 10, pady = 10)
        self.bind("<Configure>", resize_image)

class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_function):
        super().__init__(master = parent, text = "x", text_color=WHITE,
                          fg_color = "transparent", width=40, height=40,
                          corner_radius=0, hover_color=CLOSE_RED, command = close_function)
        self.place(relx = 0.99, rely = 0.01, anchor = "ne")