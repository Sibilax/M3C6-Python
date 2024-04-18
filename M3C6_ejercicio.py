"""Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 
Crea un objeto usando la clase."""


class Usuario:

  def __init__(self, user, contraseña):
    self.user = user
    self.contraseña = contraseña

un_usuario = Usuario("Sandro", "98765Z")

print(un_usuario.user)
print(un_usuario.contraseña)