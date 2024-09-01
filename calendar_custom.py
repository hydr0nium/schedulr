from __future__ import annotations
from typing import *
import customtkinter

if TYPE_CHECKING:
  from schedulr import App

class UserCalender():
  def __init__(self):
    self.calender: Dict[Tuple[int,int]] = {}
    
  def add_day(self, date: Tuple[int,int]):
    self.calender[date] = True
    
  def remove_day(self, date: Tuple[int,int]):
    self.calender[date] = False
    
  def __contains__(self, value: Tuple[int,int]) -> bool :
    return self.calender.get(value, False)
  
  def __str__(self) -> str:
    return self.calender.__str__()

class CalenderElement():
  def __init__(self, row, column, button, app):
    self.row = row
    self.column = column
    self.button: customtkinter.CTkButton = button
    self.hidden = False
    self.selected = False
    self.app: 'App' = app
    
  def hide(self):
    self.hidden = True
    self.button.grid_forget()
    
  def show(self):
    self.hidden = False
    self.button.grid(row = self.row, column = self.column, sticky="news", padx = 2, pady=2)
    
  def get_value(self) -> int:
    return int(self.button.cget("text"))
  
  def select_save(self):
    self.select()
    self.app.current_user.calender.add_day(self.get_date())
  
  def select(self):
    self.selected = True
    self.button.configure(fg_color = ["#3B8ED0", "#1F6AA5"], hover_color = ["#36719F", "#144870"])
  
  def unselect_save(self):
    self.unselect()
    self.app.current_user.calender.remove_day(self.get_date())
  
  def unselect(self):
    self.selected = False
    self.button.configure(fg_color = ["#2CC985", "#2FA572"], hover_color = ["#0C955A", "#106A43"])
    
  def toggle(self):
    if self.selected:
      self.unselect_save()
      self.selected = False
    else:
      self.select_save()
      self.selected = True
  
  def get_day(self) -> int:
    return self.get_value()
    
  def get_month(self) -> int:
    return self.app.current_user.current_month
  
  def get_date(self) -> Tuple[int, int]:
    return (self.get_month(), self.get_day())