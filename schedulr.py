import customtkinter
from typing import *

from user import User
from layout import MainFrame, UsersScrollableFrame, OptionsFrame, SolveButtonFrame, UserAddButtonFrame

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
menu_width = 0.25



class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    
    self.current_user: User = None
    
    self.geometry("1024x576")
    self.title("Schedulr")
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=10)
    self.grid_rowconfigure(0, weight=9)
    self.grid_rowconfigure(1, weight=1)
    self.grid_rowconfigure(2, weight=1)
    self.main_frame = MainFrame(master=self, corner_radius = 0)
    self.menu_frame = UsersScrollableFrame(master=self, corner_radius = 0)
    self.add_user_button_frame = UserAddButtonFrame(self, corner_radius = 0)
    self.solve_button_frame = SolveButtonFrame(self, corner_radius = 0)
    self.options_frame = OptionsFrame(self, corner_radius = 0)
    self.main_frame.grid(column = 1, row = 0, padx = 3, pady = 3, sticky="news", rowspan=2)
    self.menu_frame.grid(column = 0, row = 0, padx = 3, pady = 3, sticky="news")
    self.add_user_button_frame.grid(column = 0, row = 1, padx = 3, pady = 3, sticky="news")
    self.solve_button_frame.grid(column = 0, row = 2, padx = 3, pady = 3, sticky="news")
    self.options_frame.grid(column = 1, row = 2, padx = 3, pady = 3, sticky="news")

    
app = App()
app.mainloop()
