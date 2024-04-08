#Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.

class Usuario:  
  def __init__(self, nombre, contraseña):
    self.nombre = nombre
    self.contraseña = contraseña

usuario = Usuario('Juan', '1234')

print(usuario.nombre)
print(usuario.contraseña)
