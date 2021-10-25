from usuario import Usuario

class CRUD_Usuario:
    # Constructor
    def __init__(self):
        # Simular base de datos
        self.usuarios = []

    # CRUD => CREATE READ UPDATE DELETE

    # Crear un nuevo usuario
    def createUsuario(self, correo, pwd, nombre, edad):
        id = len(self.usuarios)
        nuevo = Usuario(id, correo, pwd, nombre, edad)
        self.usuarios.append(nuevo)
        return id

    # Leer usuario por id
    def readUsuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario.dump()
        
        return None
        
    # Leer todos los usuarios
    def readUsuarios(self):
        usuarios_aux = []

        # Convirtiendo a JSON los usuarios
        for usuario in self.usuarios:
            usuarios_aux.append(usuario.dump())

        return usuarios_aux

    # Actualizar usuario
    def updateUsuario(self, id, correo, pwd, nombre, edad):
        for usuario in self.usuarios:
            if usuario.id == id:
                usuario.correo = correo
                usuario.pwd = pwd
                usuario.nombre = nombre
                usuario.edad = edad
                return usuario.dump()
        return None

    # Eliminar usuario
    def deleteUsuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                self.usuarios.remove(usuario)
                return id
        return None  

    # Login
    def login(self, correo, pwd):
        for usuario in self.usuarios:
            if usuario.correo == correo and usuario.pwd == pwd:
                print('Usuario ' + correo + " loggeado correctamente.")
                return usuario.dump()
        return None

    # Carga masiva
    def cargaMasiva(self, usuarios_cm):
        for usuario_cm in usuarios_cm:
            self.createUsuario(usuario_cm['correo'], usuario_cm['pwd'], usuario_cm['nombre'], usuario_cm['edad'])
        return "OK"

    # Reporte edades
    # {
    #   "1 año": 21,
    #    "2 años": 5,
    # }

    def reporteEdades(self):
        edades = {}
        for usuario in self.usuarios:
            if str(usuario.edad) in edades:
                edades[str(usuario.edad)] += 1
            else: # No existe la edad en el diccionario
                edades[str(usuario.edad)] = 1
        return edades
