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

    print("\n0- Cargar información")
    print("1- Listar los últimos N partidos de un equipo segun su condición")
    print("2- Listar los primeros N goles anotados por un jugador")
    print("3- Consultar los partidos que disputó un equipo durante un periodo específico")
    print("4- Consultar los partidos relacionados con un torneo durante un periodo específico")
    print("5- Consultar las anotaciones de un jugador durante un periodo específico")
    print("6- Clasificar los N mejores equipos de un torneo en un periodo específico")
    print("7- Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo específico")
    print("8- Comparar el desempeño histórico de dos selecciones en torneos oficiales")
    print("9- Ordenar la información de acuerdo al algoritmo de ordenamiento requerido")
    print("10- Salir\n")

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

        if int(eleccion) == 0:
            
            print("\nCargando información de los archivos...\n")
            
            catalog, resultdos_tamanio, resultados_tabla, anotaciones_tamanio, anotaciones_tabla, penales_tamanio, penales_tabla = controller.load_data(catalog)
            print("Total de encuentros cargados: " + str(resultdos_tamanio))
            print("Tres primeros y tres últimos partidos ordenados por la fecha del encuentro y por el puntaje final del partido:\n" + resultados_tabla + "\n")
            print("Total de anotaciones cargadas: " + str(anotaciones_tamanio))
            print("Tres primeras y tres últimas anotaciones ordenadas por la fecha del encuentro, minuto en que se anotó y nombre del jugador:\n" + anotaciones_tabla + "\n")
            print("Total goles marcados desde el punto penal: " + str(penales_tamanio))
            print("Tres primeras y tres últimas definiciones por penales ordenadas por el criterio compuesto de la fecha del encuentro y los nombres de los equipos involucrados:\n" + penales_tabla)
                    
        elif int(eleccion) == 1:
            nombre_equipo = input("Digite el nombre del equipo sobre el que desea hacer la consulta: ")
            numero_partidos = int(input("Digite la cantidad de partidos que desea conocer: "))
            condicion_equipo = int(input("Digite la condición del equipo en los partidos:\n1.Local\n2.Visitante\n3.Indiferente\n"))
            respuesta = controller.req_1(catalog, numero_partidos, nombre_equipo, condicion_equipo)
            print("\n" + "Del total de " + str(respuesta[1]) + " partidos que se encontraron del equipo " + nombre_equipo + " en condición " + respuesta[3] + " estos son los registros más antiguos y recientes entoncontrados (si son más de seis, se muestran los primeros y ultimos tres):\n\n" + respuesta[0])
            
        elif int(eleccion) == 2:
            nombre_jugador = input("Digite el nombre del jugador sobre el que desea hacer la consulta: ")
            numero_goles = int(input("Digite la cantidad de primeros n goles que desea conocer del jugador: "))
            respuesta = controller.req_2(catalog, nombre_jugador, numero_goles)
            print("\n" + "Del total de " + str(respuesta[1]) + " goles anotados por el jugador " + nombre_jugador + " estos son los registros más antiguos y recientes entoncontrados (si son más de seis, se muestran los primeros y ultimos tres):\n\n" + respuesta[0])

        elif int(eleccion) == 3:
            nombre_equipo = input("Digite el nombre del equipo sobre el que desea hacer la consulta: ")
            fecha_inicial = input("Digite la fecha inicial del periodo a consultar (con formato %Y-%m-%d): ")
            fecha_final = input("Digite la fecha inicial del periodo a consultar (con formato %Y-%m-%d): ")
            respuesta = controller.req_3(catalog, nombre_equipo, fecha_inicial, fecha_final)
            print("\n" + "Del total de " + str(respuesta[1]) + " partidos jugados por el equipo " + nombre_equipo + " entre " + fecha_inicial + " y " + fecha_final + " " + str(respuesta[2]) + " son como equipo local y " + str(respuesta[3]) + " son como equipo visitante." + " Estos son los registros más antiguos y recientes entoncontrados (si son más de seis, se muestran los primeros y ultimos tres):\n\n" + respuesta[0])

        elif int(eleccion) == 4:
            nombre_torneo = input("Digite el nombre del torneo sobre el que desea hacer la consulta: ")
            fecha_inicial = input("Digite la fecha inicial del periodo a consultar (con formato %Y-%m-%d): ")
            fecha_final = input("Digite la fecha inicial del periodo a consultar (con formato %Y-%m-%d): ")
            respuesta = controller.req_4(catalog, nombre_torneo, fecha_inicial, fecha_final)
            print("\n" + "En el torneo " + nombre_torneo + " entre las fechas " + fecha_inicial + " y " + fecha_final + " se vieron involucrados " + str(respuesta[1]) + " partidos, " + str(respuesta[2]) + " paises, " + str(respuesta[3]) + " ciudades y " + str(respuesta[3]) + " partidos definidos por penales." + " Estos son los registros más antiguos y recientes entoncontrados (si son más de seis, se muestran los primeros y ultimos tres):\n\n" + respuesta[0])
        
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
            working = False
            print("\nGracias por utilizar el programa\n") 
            
        else:
            print("Opción errónea, vuelva a elegir.\n")

if __name__ == "__main__":
    menu_cycle()