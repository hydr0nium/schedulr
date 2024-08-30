import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
menu_width = 0.25




class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    self.geometry("1024x576")
    self.title("Schedulr")
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=3)
    self.grid_rowconfigure(0, weight=10)
    self.grid_rowconfigure(1, weight=1)
    self.main_frame = MainFrame(master=self)
    self.menu_frame = MenuFrame(master=self)
    self.button_frame = ButtonFrame(master=self)
    self.options_frame = OptionsFrame(master=self)
    self.main_frame.grid(column = 1, row = 0, padx = 5, pady = 5, sticky="news")
    self.menu_frame.grid(column = 0, row = 0, padx = 5, pady = 5, sticky="news")
    self.button_frame.grid(column = 0, row = 1, padx = 5, pady = 5, sticky="news")
    self.options_frame.grid(column = 1, row = 1, padx = 5, pady = 5, sticky="news")

    
class MenuFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.label = customtkinter.CTkLabel(self).pack()
  
class ButtonFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.grid_columnconfigure(1, weight=2)
    self.grid_columnconfigure((0,2), weight=1)
    self.grid_rowconfigure((0,1,2), weight=1)
    self.button = customtkinter.CTkButton(self, text="Solve").grid(row = 1, column = 1, sticky="news")
    
class OptionsFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.label = customtkinter.CTkLabel(self).pack()
        
class MainFrame(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.label = customtkinter.CTkLabel(self).pack()
    
class UsersScrollableFrame(customtkinter.CTkScrollableFrame):
  def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)
  def get(self):
      checked_checkboxes = []
      for checkbox in self.checkboxes:
          if checkbox.get() == 1:
              checked_checkboxes.append(checkbox.cget("text"))
      return checked_checkboxes

app = App()
app.mainloop()
