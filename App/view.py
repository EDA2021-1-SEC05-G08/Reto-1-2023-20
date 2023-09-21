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
import threading

default_limit = 10000
sys.setrecursionlimit(default_limit * 10000)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar los últimos N partidos de un equipo segun su condición")
    print("3- Listar los primeros N goles anotados por un jugador")
    print("4- Consultar los partidos que disputó un equipo durante un periodo específico")
    print("5- Consultar los partidos relacionados con un torneo durante un periodo específico")
    print("6- Consultar las anotaciones de un jugador durante un periodo específico")
    print("7- Clasificar los N mejores equipos de un torneo en un periodo específico")
    print("8- Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo específico")
    print("9- Comparar el desempeño histórico de dos selecciones en torneos oficiales")
    print("10- Ordenar la información de acuerdo al algoritmo de ordenamiento requerido")
    print("0- Salir")

def print_req_1(control):
    controller.req_1(control)


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def print_req_9(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    print('\nIngrese el numero del tipo de ordenamiento que desee: \n')
    print(' 1. SELECTION_SORT.')
    print(' 2. INSERTION_SORT.')
    print(' 3. SHELL_SORT. ')
    print(' 4. MERGE_SORT. ')
    print(' 5. QUICK_SORT ')
    eleccion = input()
    algoritmo =""
    
    if eleccion == "1":
        algoritmo = "selection"
    elif eleccion == "2":
        algoritmo = "insertion"
    elif eleccion == "3":
        algoritmo = "shell"
    elif eleccion == "4":
        algoritmo = "merge"
    elif eleccion == "5":
        algoritmo = "quick"

    print_final = controller.req_9(control,algoritmo)
    resultados_size = print_final[0][0]
    catalog = print_final[0][1]
    tabla = controller.print_req_9(catalog)
    

    print("El total de resultados cargados es: " + str(resultados_size))
    print(tabla)
    print("El total del tiempo de ejecución en la carga de datos en milisegundos es: " + str(print_final[1]))


# Se crea el controlador asociado a la vista\
control = ""

# main del reto
#if __name__ == "__main__":
def menu_cycle(): 
    
    """
    Menu principal
    """

    working = True
    #ciclo del menu
    while working:
        
        control = controller.new_controller()    
        
        while working:
            print_menu()
            inputs = input('Seleccione una opción para continuar\n')
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
        
                data_penales = controller.load_penales(control)
                data_anotaciones = controller.load_anotaciones(control)
                data_results = controller.load_resultados(control)

                print("\n\n" + "-" * 40 + "\nEl total de encuentros cargados es: " + str(data_results) +
                "\nEl total de anotaciones cargadas: " + str(data_anotaciones) +  
                "\nEl total de goles marcados desde el punto penal: " +
                str(data_penales) + "\n" + "-" * 40 + "\n\n")
                
                
                print("\n Los primeros 3 y los últimos 3 resultados...")
                tabla_desorden = controller.print_general(control)
                print(tabla_desorden[0])
                print("\n Los primeros 3 y las últimos 3 anotaciones...")
                print(tabla_desorden[1])
                print("\n Los primeras 3 y los últimas 3 penales...")
                print(tabla_desorden[2])
                        
            elif int(inputs) == 2:
                print_req_1(control)
                

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                print_req_9(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa") 
            else:
                print("Opción errónea, vuelva a elegir.\n")
        sys.exit(0)

if __name__ == "__main__":
    
    menu_cycle()
    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()