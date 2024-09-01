from __future__ import annotations

import customtkinter
from typing import *
from calendar_custom import UserCalender

if TYPE_CHECKING:
  from schedulr import App

class User():
  def __init__(self, user_button: customtkinter.CTkButton, app: 'App'):
    self.current_month = 0
    self.userbutton = user_button
    self.app = app
    self.calender = UserCalender()
    
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
  