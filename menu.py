import customtkinter as ctk
from panels import *
class Menu(ctk.CTkTabview):
    def __init__(self, parent, pos_vars, color_vars, effect_vars):
        super().__init__(master = parent)
        self.grid(column = 0, row = 0, sticky = "nsew", pady = 10, padx = 10)

        # tabs
        self.add("Position")
        self.add("Color")
        self.add("Effects")
        self.add("Export")

        # widgets
        PositionFrame(self.tab("Position"), pos_vars)
        ColorFrame(self.tab("Color"), color_vars)
        EffectFrame(self.tab("Effects"), effect_vars)
class PositionFrame(ctk.CTkFrame):
    def __init__(self, parent, pos_vars):
        super().__init__(master = parent,
                       fg_color="transparent",)
        self.pack(expand = True, fill = "both")

        SliderPanel(self, "Rotation", pos_vars['rotate'], 0, 360)
        SliderPanel(self, "Zoom", pos_vars['zoom'], 0, 200)
class ColorFrame(ctk.CTkFrame):
    def __init__(self, parent, color_vars):
        super().__init__(master = parent,
                         fg_color="transparent",)
        self.pack(expand = True, fill = "both")

        SliderPanel(self, "Brightness", color_vars['brightness'], 0, 5)
        SliderPanel(self, "Vibrance", color_vars['vibrance'], 0, 5)



class EffectFrame(ctk.CTkFrame):
    def __init__(self, parent, effect_vars):
        super().__init__(master = parent,
                         fg_color="transparent",)
        self.pack(expand = True, fill = "both")