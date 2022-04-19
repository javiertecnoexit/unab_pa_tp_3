'''Ejercicio 5:
Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre 
cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial ,
 lugar (ciudad y país) y fecha de edición (como texto). 
 La clase debe proporcionar los siguientes servicios: 
 getters y setters, método para leer la información y método para mostrar la información. 
Este último método mostrará la información del libro con este formato: 
'''
from persona import Persona
class Libro:

    def __init__(self, titulo, autor,ISBN, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self.titulo=titulo
        self.autor=autor
        self.ISBN=ISBN
        self.paginas=paginas
        self.edicion=edicion
        self.editorial=editorial
        self.ciudad=ciudad
        self.pais=pais
        self.fecha_edicion=fecha_edicion

    
        
        
