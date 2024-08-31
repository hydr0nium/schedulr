import customtkinter
import months
from typing import *


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
menu_width = 0.25
current_month = 0



class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()
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
    self.grid_columnconfigure((0,1,2,3), weight=1)
    customtkinter.CTkButton(self, text="<--",command=self.last_month(master)).grid(row = 1, column = 0, sticky="news", padx = 2, pady=2, columnspan=2)
    customtkinter.CTkButton(self, text="-->",command=self.next_month(master)).grid(row = 1, column = 2, sticky="news", padx = 2, pady=2, columnspan=2)
    self.label = customtkinter.CTkLabel(self, text=list(months.months.items())[current_month][0].capitalize())
    self.label.grid(row = 0, column = 1, sticky= "news", padx = 2, pady=2, columnspan=2)
    
  def next_month(self, app: App):
    def inner():
      global current_month
      if len(list(months.months.items()))-1 == current_month:
        current_month = 0
      else:
        current_month += 1
      app.main_frame.redraw_grid()
      self.label.configure(text = list(months.months.items())[current_month][0].capitalize())
    return inner
      
  def last_month(self, app: App):
    def inner():
      global current_month
      if current_month == 0:
        current_month = len(list(months.months.items()))-1
      else:
        current_month -= 1
      app.main_frame.redraw_grid()
      self.label.configure(text = list(months.months.items())[current_month][0].capitalize())
    return inner
      
    
        
class MainFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
    self.grid_rowconfigure((0,1,2,3,4), weight=1)
    self.first_grid_draw()
    
  def redraw_grid(self):
    global current_month
    month_length = list(months.months.items())[current_month][1]
    if month_length < len(self.grid_slaves()):
      for slave in self.grid_slaves():
        if int(slave.cget("text")) > month_length:
          slave.destroy()
    elif month_length > len(self.grid_slaves()):
      for day in range(int(self.grid_slaves()[0].cget("text"))+1, month_length+1):
        column = (day-1) % 7
        row = (day-1) // 7
        customtkinter.CTkButton(self, text=day, anchor="se", corner_radius=0).grid(row = row, column = column, sticky="news", padx = 2, pady=2)
        
  def first_grid_draw(self):
    global current_month
    month_length = list(months.months.items())[current_month][1]
    day = 1
    for row in range(5):
       for column in range(7):
        if day > month_length:
          break
        customtkinter.CTkButton(self, text=day, anchor="se", corner_radius=0).grid(row = row, column = column, sticky="news", padx = 2, pady=2)
        day += 1
       if day > month_length:
         break

    
class UsersScrollableFrame(customtkinter.CTkScrollableFrame):
  def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.last_row = 0
        self.users = []
        self.selected_user = None
            
  def add_user(self):
      dialog = customtkinter.CTkInputDialog(text="Enter a name", title="Schedulr")
      username = dialog.get_input()
      if username == None:
        return
      user = customtkinter.CTkButton(self, text=username, command=self.select_user(username))
      user.grid(row = self.last_row, column = 0, padx = 5, pady = 5, sticky="we")
      self.last_row = self.last_row + 1
      self.users.append(user)
      self.selected_user = user
      for user in self.users:
        if user.cget("text") == username:
          user.configure(fg_color = ["#3B8ED0", "#1F6AA5"], hover_color = ["#36719F", "#144870"])
        else:
          user.configure(fg_color = ["#2CC985", "#2FA572"], hover_color = ["#0C955A", "#106A43"])
      
  def select_user(self, username):
    def inner():
      for user in self.users:
        if user.cget("text") == username:
          user.configure(fg_color = ["#3B8ED0", "#1F6AA5"], hover_color = ["#36719F", "#144870"])
        else:
          user.configure(fg_color = ["#2CC985", "#2FA572"], hover_color = ["#0C955A", "#106A43"])
    return inner
      
class SolveButtonFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(1, weight=2)
    self.grid_columnconfigure((0,2), weight=1)
    self.grid_rowconfigure((0,1,2), weight=1)
    self.button = customtkinter.CTkButton(self, text="Solve", font=("Calibri bold", 20)).grid(row = 1, column = 1, sticky="news") 
      

class UserAddButtonFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(1, weight=1)
    self.grid_columnconfigure((0,2), weight=2)
    self.grid_rowconfigure((0,1,2), weight=1)
    self.button = customtkinter.CTkButton(self, text="+", command=master.menu_frame.add_user, font=("Calibri bold", 20)).grid(row = 1, column = 1, sticky = "ns")

app = App()
app.mainloop()
