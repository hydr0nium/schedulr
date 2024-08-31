import customtkinter
import months
from typing import *


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

    
    
class OptionsFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.app: App = master
    self.grid_columnconfigure(0, weight=3)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure(2, weight=2)
    self.grid_columnconfigure(3, weight=1)
    self.grid_columnconfigure(4, weight=3)
    self.left = customtkinter.CTkButton(self, text="⮘",command=self.last_month(self.app))
    self.right = customtkinter.CTkButton(self, text="⮚",command=self.next_month(self.app))
    self.label = customtkinter.CTkLabel(self, text="")
    self.label.grid(row = 0, column = 2, sticky= "news", padx = 2, pady=2)
    self.label.grid_propagate(0)
  
  def init_option_buttons(self):
    self.left.grid(row = 1, column = 1, sticky="ew", padx = 2, pady=2)
    self.left.grid_propagate(0)
    self.right.grid(row = 1, column = 3, sticky="ew", padx = 2, pady=2)
    self.right.grid_propagate(0)

  def next_month(self, app: App):
    def inner():
      if app.current_user == None:
        return
      app.current_user.increase_month()
      current_month = app.current_user.current_month
      app.main_frame.redraw_grid(current_month)
      self.change_label(current_month)
    return inner
  
  def last_month(self, app: App):
    def inner():
      if app.current_user == None:
        return
      app.current_user.decrease_month()
      current_month = app.current_user.current_month
      app.main_frame.redraw_grid(current_month)
      self.change_label(current_month)
    return inner
  
  def change_label(self, current_month: int):
    self.label.configure(text = list(months.months.items())[current_month][0].capitalize())
      
    
        
class MainFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.app: App = master
    self.calender_month: List[CalenderElement] = []
    self.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
    self.grid_rowconfigure((0,1,2,3,4), weight=1)
    
  def redraw_grid(self, current_month):
    self.app.options_frame.change_label(current_month)
    month_length = list(months.months.items())[current_month][1]
    for day in self.calender_month:
      if day.get_value() > month_length:
        day.hide()
      elif day.hidden and day.get_value() <= month_length:
        day.show()
        
  def hide_all(self):
    for day in self.calender_month:
      day.hide()
          

  def init_grid(self, current_month):
    self.app.options_frame.init_option_buttons()
    month_length = list(months.months.items())[current_month][1]
    day = 1
    for row in range(5):
       for column in range(7):
        if day > month_length:
          return
        button = customtkinter.CTkButton(self, text=day, anchor="se", corner_radius=0)
        button.grid(row = row, column = column, sticky="news", padx = 2, pady=2)
        self.calender_month.append(CalenderElement(row, column, button))
        day += 1


class CalenderElement():
  def __init__(self, row, column, button):
    self.row = row
    self.column = column
    self.button = button
    self.hidden = False
    
  def hide(self):
    self.hidden = True
    self.button.grid_forget()
    
  def show(self):
    self.hidden = False
    self.button.grid(row = self.row, column = self.column, sticky="news", padx = 2, pady=2)
    
  def get_value(self) -> int:
    return int(self.button.cget("text"))
    
class UsersScrollableFrame(customtkinter.CTkScrollableFrame):
  def __init__(self, master: App, **kwargs):
        super().__init__(master, **kwargs)
        self.app = master
        self.grid_columnconfigure(0, weight=1)
        self.last_row = 0
        self.users: List[User] = []
             
  
  def add_user(self):
      # Create input dialog
      dialog = customtkinter.CTkInputDialog(text="Enter a name", title="Schedulr")
      username = dialog.get_input()
      if username == None:
        return
        
      # Check if user already exists and then create it
      if username not in self.users:
        
        # Create users
        user = customtkinter.CTkButton(self, text=username, command=self.select_user(username))
        user.grid(row = self.last_row, column = 0, padx = 5, pady = 5, sticky="we")
        user = User(user, self.app)
        
        # Bookkeeping
        self.last_row = self.last_row + 1
        if not self.users:
          self.app.main_frame.init_grid(user.current_month)
        self.users.append(user)
      
      
      # Select User
      for user in self.users:
        if user.get_username() == username:
          user.select_user()
          self.app.current_user = user
          self.app.main_frame.redraw_grid(user.current_month)
        else:
          user.unselect_user()
      
  def select_user(self, username):
    def inner():
      for user in self.users:
        if user.get_username() == username:
          user.select_user()
          self.app.current_user = user
          self.app.main_frame.redraw_grid(user.current_month)
        else:
          user.unselect_user()
      
    return inner
  
class User():
  def __init__(self, user_button: customtkinter.CTkButton, app: App):
    self.current_month = 0
    self.userbutton = user_button
    self.app = app
    
  def get_username(self):
    return self.userbutton.cget("text")
  
  def select_user(self):
    self.userbutton.configure(fg_color = ["#3B8ED0", "#1F6AA5"], hover_color = ["#36719F", "#144870"])
    
  def unselect_user(self):
    self.userbutton.configure(fg_color = ["#2CC985", "#2FA572"], hover_color = ["#0C955A", "#106A43"])
   
  def increase_month(self):
    if self.current_month == 11:
      self.current_month = 0
    else:
      self.current_month += 1
      
  def decrease_month(self):
    if self.current_month == 0:
      self.current_month = 11
    else:
      self.current_month -= 1
   
  def __eq__(self, value: str) -> bool:
    return self.get_username() == value
  
  def __str__(self) -> str:
    return f"User ({self.get_username()}, {self.current_month})"
  
      
class SolveButtonFrame(customtkinter.CTkFrame):
  def __init__(self, master: App, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(1, weight=2)
    self.grid_columnconfigure((0,2), weight=1)
    self.grid_rowconfigure((0,1,2), weight=1)
    self.button = customtkinter.CTkButton(self, text="Solve", font=("Calibri bold", 20), command=master.main_frame.hide_all).grid(row = 1, column = 1, sticky="news") 
      

class UserAddButtonFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((0,2), weight=2)
    self.grid_rowconfigure((0,1,2), weight=1)
    self.button = customtkinter.CTkButton(self, text="+", command=master.menu_frame.add_user, font=("Calibri bold", 20)).grid(row = 1, column = 1, sticky = "ns")

app = App()
app.mainloop()
