import customtkinter
from src.lib.python.views.configuration import Configuration

class Body(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs, fg_color='transparent')

    self.button = customtkinter.CTkButton(
      self,
      text='Iniciar',
      fg_color='#437512',
      hover_color="#437512",
      text_color='#D4DBB9'
    )
    self.button.pack(side='left')

    self.button = customtkinter.CTkButton(
      self,
      text='Configurações',
      fg_color='#437512',
      hover_color="#437512",
      text_color='#D4DBB9',
      command=self.openConfiguration
    )
    self.button.pack(side='left', padx=4)

    self.toplevel_window = None

  def openConfiguration(self):
    if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
      self.toplevel_window = Configuration(self)
    else:
      self.toplevel_window.focus()

class Header(customtkinter.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs, fg_color='transparent')

    self.label = customtkinter.CTkLabel(
      self, 
      text='Sistema Bot-Iomat', 
      font=("Arial", 16),
      text_color='#D4DBB9'
    )
    self.label.pack(side='left')

    self.button = customtkinter.CTkButton(
      self,
      text='Ajuda',
      fg_color='#437512',
      hover_color="#437512",
      text_color='#D4DBB9',
      width=50
    )
    self.button.pack(side='right')

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__(fg_color="#062400")
    self.geometry("800x600")
    self.title("Primeiro Exemplo")
    customtkinter.set_appearance_mode('dark')

    self.header = Header(self)
    self.header.pack(side='top', fill='x', padx=8, pady=6)

    self.body = Body(self)
    self.body.pack(fill='x', padx=8)

if __name__ == "__main__":
  app = App()
  app.mainloop()