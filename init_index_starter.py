'''
Programado por: Samuel Alejandro Chamalé Rac

Carné: 21881

Funcion del programa: Este programa maneja datos de una tabla los cuales pueden ser editados, desplegados y agregados
                    ademas se pueden obtener calculos con los datos de esta tabla. El programa esta enfocado a un caso 
                    de control de ejercicios de una familia.
                    
Descripcion de archivos:
- init_index_starter.py
    este archivo es el inicializador, desde acá se ejecuta el programa.
- structure.py
    este archivo es el que contiene el las funciones para el funcionamiento estructural del programa.
- fun.struc.py
    contiene algunas otras funciones que operan estructuralmente, pero son mas complejas.
- fun.opera.py
    se encuentran las funcion que se utilizan en la estructura, son calculos o funciones repetitivas.
- unicoded_respaldo.py
    archivo de respaldo *ver descripción*
- archivo.csv
    contiene los datos manejados
'''
import structure

# SE LLAMA A LA FUNCION MADRE *HAY COMENTARIOS EN CADA ARCHIVO*
structure.itermenu()
