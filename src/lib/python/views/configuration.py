import customtkinter
from src.lib.python.xlsxtojson import XlsxToJson

class Servers(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs, fg_color='transparent')
    self.label = False
    
    button = customtkinter.CTkButton(
      self,
      text='Atualizar servidores',
      fg_color='#437512',
      hover_color="#437512",
      text_color='#D4DBB9',
      command=self.update_servers
    )
    button.pack(side='left')

  def update_servers(self):
    handleUpdate = XlsxToJson()
    if handleUpdate:
      self.label = 'Atualizado'
    else:
      self.label = 'Erro ao atualizar'

    label = customtkinter.CTkLabel(
        self, 
        text=f'{self.label}',
        font=("Arial", 16),
        text_color='#D4DBB9'
      )
    label.pack(side='left', padx=4)

class Configuration(customtkinter.CTkToplevel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs, fg_color="#062400")
    self.geometry('600x400')

    servers = Servers(self)
    servers.pack(fill='x', padx=8, pady=8)