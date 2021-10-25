class Usuario:
    
    # Constructor
    def __init__(self, id, correo, pwd, nombre, edad):
        self.id = id
        self.correo = correo
        self.pwd = pwd
        self.nombre = nombre
        self.edad = edad
    
    # Métodos
    def saludar(self):
        print("Mi nombre es " + self.nombre)

    def dump(self):
        return {
            'id': self.id,
            'correo': self.correo,
            'pwd': self.pwd,
            'nombre': self.nombre,
            'edad': self.edad
        }
