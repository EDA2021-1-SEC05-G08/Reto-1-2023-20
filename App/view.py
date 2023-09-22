"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
assert cf

default_limit = 10000
sys.setrecursionlimit(default_limit * 10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def print_menu():

    print("\n1- Cargar información")
    print("2- Listar los últimos N partidos de un equipo segun su condición")
    print("3- Listar los primeros N goles anotados por un jugador")
    print("4- Consultar los partidos que disputó un equipo durante un periodo específico")
    print("5- Consultar los partidos relacionados con un torneo durante un periodo específico")
    print("6- Consultar las anotaciones de un jugador durante un periodo específico")
    print("7- Clasificar los N mejores equipos de un torneo en un periodo específico")
    print("8- Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo específico")
    print("9- Comparar el desempeño histórico de dos selecciones en torneos oficiales")
    print("10- Ordenar la información de acuerdo al algoritmo de ordenamiento requerido")
    print("0- Salir\n")

def menu_cycle(): 
    
    """
    Menu principal
    """

    working = True
        
    print("\nBienvenido, este es el menú de la aplicación:")
    catalog = controller.new_controller()
    
    while working:

        print_menu()

        eleccion = input('Seleccione una opción para continuar: ')

        if int(eleccion) == 1:
            
            print("\nCargando información de los archivos...\n")
            
            catalog, resultdos_tamanio, resultados_tabla, anotaciones_tamanio, anotaciones_tabla, penales_tamanio, penales_tabla = controller.load_data(catalog)
            print("Total de encuentros cargados: " + str(resultdos_tamanio))
            print("Tres primeros y tres últimos partidos ordenados por la fecha del encuentro y por el puntaje final del partido:\n" + resultados_tabla + "\n")
            print("Total de anotaciones cargadas: " + str(anotaciones_tamanio))
            print("Tres primeras y tres últimas anotaciones ordenadas por la fecha del encuentro, minuto en que se anotó y nombre del jugador:\n" + anotaciones_tabla + "\n")
            print("Total goles marcados desde el punto penal: " + str(penales_tamanio))
            print("Tres primeras y tres últimas definiciones por penales ordenadas por el criterio compuesto de la fecha del encuentro y los nombres de los equipos involucrados:\n" + penales_tabla)
                    
        elif int(eleccion) == 2:
            pass
            
        elif int(eleccion) == 3:
            pass

        elif int(eleccion) == 4:
            pass

        elif int(eleccion) == 5:
           pass
        
        elif int(eleccion) == 6:
            pass

        elif int(eleccion) == 7:
            pass

        elif int(eleccion) == 8:
            pass

        elif int(eleccion) == 9:
            pass

        elif int(eleccion) == 10:
            pass

        elif int(eleccion) == 0:
            working = False
            print("\nGracias por utilizar el programa\n") 
            
        else:
            print("Opción errónea, vuelva a elegir.\n")

if __name__ == "__main__":
    menu_cycle()