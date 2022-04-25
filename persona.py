class Persona:
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.nacionalidad=nacionalidad
        
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_nacionalidad(self):
        return self.nacionalidad
    
    def set_nombre(self, nuevo_nombre):
        self.nombre=nuevo_nombre
        
    def set_apellido(self, nuevo_apellido):
        self.apellido=nuevo_apellido
    
    def set_nacionalidad(self, nueva_nacionalidad):
        self.nacionalidad=nueva_nacionalidad
        
        