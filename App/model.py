"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time as time
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from tabulate import tabulate

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_controller():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    catalog = {'resultados': None,
               'anotaciones': None,
               'penales': None}

    catalog['resultados'] = lt.newList("ARRAY_LIST")
    catalog['anotaciones'] = lt.newList("ARRAY_LIST")
    catalog['penales'] = lt.newList("ARRAY_LIST")
    
    return catalog

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    pass

def add_results(catalog, resultado):
    
    lt.addLast(catalog['resultados'], resultado)
    
    return catalog

def add_anotaciones(catalog, anotacion):
    
    lt.addLast(catalog['anotaciones'], anotacion)
    
    return catalog

def add_penales(catalog, penal):
    
    lt.addLast(catalog['penales'], penal)
    
    return catalog


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def orden_resultados(catalog):

    resultados = catalog["resultados"]
    resultados = sa.sort(resultados, compare_resultados)

    return resultados

def orden_anotaciones(catalog):

    anotaciones = catalog["anotaciones"]
    anotaciones = sa.sort(anotaciones, compare_resultados)

    return anotaciones

def orden_penales(catalog):

    penales = catalog["penales"]
    penales = sa.sort(penales, compare_resultados)

    return penales


def req_1(catalog , n_ultimos_partidos , condicion):
    
    resultados = catalog["resultados"]
    
    resultados = sa.sort(resultados, compare_fechas)
    for i in range(1,20):
        print(lt.getElement(resultados, i))

    #print(lt.size(resultados))



def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def req_9(catalog, algoritmo):
    """
    Función que soluciona el requerimiento 9
    """
    resultados = catalog["resultados"]

    if algoritmo == "selection":
        resultados = se.sort(resultados, compare_fechas)
        resultados = se.sort(resultados, compare_pais)
        
    elif algoritmo == "insertion":
        resultados = ins.sort(resultados, compare_fechas)
        resultados = ins.sort(resultados, compare_pais)
        
    elif algoritmo == "shell":
        resultados = sa.sort(resultados, compare_fechas)
        resultados = sa.sort(resultados, compare_pais) 
        
    elif algoritmo == "merge":
        resultados = merg.sort(resultados, compare_fechas)
        resultados = merg.sort(resultados, compare_pais) 
        
    elif algoritmo == "quick":
        resultados = quk.sort(resultados, compare_fechas)
        resultados = quk.sort(resultados, compare_pais) 
        
    catalog = {"resultados": resultados}
        
    resultados_size = lt.size(catalog['resultados'])
        
    return resultados_size, catalog

def print_req_9(catalog):
    
    answer = [("date","home_team","away_team","home_score","away_score","tournament","city","country","neutral")]
    for i in range(2, 5):
        index = (lt.getElement(catalog["resultados"], i)["date"],
                 lt.getElement(catalog["resultados"], i)["home_team"],
                 lt.getElement(catalog["resultados"], i)["away_team"],
                 lt.getElement(catalog["resultados"], i)["home_score"],
                 lt.getElement(catalog["resultados"], i)["away_score"],
                 lt.getElement(catalog["resultados"], i)["tournament"],
                 lt.getElement(catalog["resultados"], i)["city"],
                 lt.getElement(catalog["resultados"], i)["country"],
                 lt.getElement(catalog["resultados"], i)["neutral"])
        answer.append(index)
    for i in range(-3, 0):
        index2 = (lt.getElement(catalog["resultados"], i)["date"],
                 lt.getElement(catalog["resultados"], i)["home_team"],
                 lt.getElement(catalog["resultados"], i)["away_team"],
                 lt.getElement(catalog["resultados"], i)["home_score"],
                 lt.getElement(catalog["resultados"], i)["away_score"],
                 lt.getElement(catalog["resultados"], i)["tournament"],
                 lt.getElement(catalog["resultados"], i)["city"],
                 lt.getElement(catalog["resultados"], i)["country"],
                 lt.getElement(catalog["resultados"], i)["neutral"])
        answer.append(index2)
    tabla_resultados_req_9 = (tabulate(answer, headers="firstrow", tablefmt="grid"))
    
    return tabla_resultados_req_9


def print_general(control):
    
    answer = [("date","home_team","away_team","home_score","away_score","tournament","city","country","neutral")]
    for i in range(0, 3):
        index = (lt.getElement(control["resultados"], i)["date"],
                 lt.getElement(control["resultados"], i)["home_team"],
                 lt.getElement(control["resultados"], i)["away_team"],
                 lt.getElement(control["resultados"], i)["home_score"],
                 lt.getElement(control["resultados"], i)["away_score"],
                 lt.getElement(control["resultados"], i)["tournament"],
                 lt.getElement(control["resultados"], i)["city"],
                 lt.getElement(control["resultados"], i)["country"],
                 lt.getElement(control["resultados"], i)["neutral"])
        answer.append(index)
    for i in range(-3, 0):
        index2 = (lt.getElement(control["resultados"], i)["date"],
                 lt.getElement(control["resultados"], i)["home_team"],
                 lt.getElement(control["resultados"], i)["away_team"],
                 lt.getElement(control["resultados"], i)["home_score"],
                 lt.getElement(control["resultados"], i)["away_score"],
                 lt.getElement(control["resultados"], i)["tournament"],
                 lt.getElement(control["resultados"], i)["city"],
                 lt.getElement(control["resultados"], i)["country"],
                 lt.getElement(control["resultados"], i)["neutral"])
        answer.append(index2)
    tabla_resultados = (tabulate(answer, headers="firstrow", tablefmt="grid"))
    
    #Imprime los primeros 3 y ultimos 3 anotaciones
    answer = [("date","home_team","away_team","team","scorer","minute","own_goal","penalty")]
    for i in range(0, 3):
        index = (lt.getElement(control["anotaciones"], i)["date"],
                 lt.getElement(control["anotaciones"], i)["home_team"],
                 lt.getElement(control["anotaciones"], i)["away_team"],
                 lt.getElement(control["anotaciones"], i)["team"],
                 lt.getElement(control["anotaciones"], i)["scorer"],
                 lt.getElement(control["anotaciones"], i)["minute"],
                 lt.getElement(control["anotaciones"], i)["own_goal"],
                 lt.getElement(control["anotaciones"], i)["penalty"])
        answer.append(index)
    for i in range(-3, 0):
        index2 = (lt.getElement(control["anotaciones"], i)["date"],
                 lt.getElement(control["anotaciones"], i)["home_team"],
                 lt.getElement(control["anotaciones"], i)["away_team"],
                 lt.getElement(control["anotaciones"], i)["team"],
                 lt.getElement(control["anotaciones"], i)["scorer"],
                 lt.getElement(control["anotaciones"], i)["minute"],
                 lt.getElement(control["anotaciones"], i)["own_goal"],
                 lt.getElement(control["anotaciones"], i)["penalty"])
        answer.append(index2)
    tabla_anotaciones = (tabulate(answer, headers="firstrow", tablefmt="grid"))
    
    #Imprime los primeros 3 y ultimos 3 penales
    answer = [("date","home_team","away_team","winner")]
    for i in range(0, 3):
        index = (lt.getElement(control["penales"], i)["date"],
                 lt.getElement(control["penales"], i)["home_team"],
                 lt.getElement(control["penales"], i)["away_team"],
                 lt.getElement(control["penales"], i)["winner"])
        answer.append(index)
    for i in range(-3, 0):
        index2 = (lt.getElement(control["penales"], i)["date"],
                 lt.getElement(control["penales"], i)["home_team"],
                 lt.getElement(control["penales"], i)["away_team"],
                 lt.getElement(control["penales"], i)["winner"])
        answer.append(index2)
    tabla_penales = (tabulate(answer, headers="firstrow", tablefmt="grid"))
    
    return tabla_resultados, tabla_anotaciones, tabla_penales

# Funciones para comparar datos

def compare_pais(resultado1, resultado2):

    country1 = resultado1["country"]
    country2 = resultado2["country"]

    if resultado1["date"] == resultado2["date"]:
        if country1 < country2:
            return True
        else: 
            return False 

# Funciones utilizadas para comparar elementos dentro de una lista

def compare_fechas(resultado1, resultado2):

    # Divide las cadenas de fecha en partes: año, mes y día
    resultado1 = resultado1["date"]
    resultado2 = resultado2["date"]
    
    year1 = resultado1.split("-")[0]
    year2 = resultado2.split("-")[0]
    month1 = resultado1.split("-")[1]
    month2 = resultado2.split("-")[1]
    day1 = resultado1.split("-")[2]
    day2 = resultado2.split("-")[2]
    
    # Compara las fechas
    if year1 < year2:
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True
    else:
        return False
    

def compare_resultados(resultado1,resultado2):

    # Compara los puntajes finales del partido

    resultado1 = resultado1["date"]
    resultado2 = resultado2["date"]
    
    year1 = resultado1.split("-")[0]
    year2 = resultado2.split("-")[0]
    month1 = resultado1.split("-")[1]
    month2 = resultado2.split("-")[1]
    day1 = resultado1.split("-")[2]
    day2 = resultado2.split("-")[2]

    local1 = resultado1["home_score"]
    local2 = resultado2["home_score"]

    visitante1 = resultado1["away_score"]
    visitante2 = resultado2["away_score"]
    
    if year1 < year2:          
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True
    else:
        if local1 < local2:
            return True
        elif local1 == local2 and visitante1 < visitante2:
            return True
        else:
            return False

def compare_anotaciones(anotacion1,anotacion2):

    # Compara los puntajes finales del partido

    anotacion1 = anotacion1["date"]
    anotacion2 = anotacion2["date"]
    
    year1 = anotacion1.split("-")[0]
    year2 = anotacion2.split("-")[0]
    month1 = anotacion1.split("-")[1]
    month2 = anotacion2.split("-")[1]
    day1 = anotacion1.split("-")[2]
    day2 = anotacion2.split("-")[2]

    minute1 = anotacion1["minute"]
    minute2 = anotacion2["minute"]
    
    if year1 < year2:          
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True
    else:
        if minute1 < minute2:
            return True
        else:
            return False

def compare_penales(penal1,penal2):

    # Compara los puntajes finales del partido

    penal1 = penal1["date"]
    penal2 = penal2["date"]
    
    year1 = penal1.split("-")[0]
    year2 = penal2.split("-")[0]
    month1 = penal1.split("-")[1]
    month2 = penal2.split("-")[1]
    day1 = penal1.split("-")[2]
    day2 = penal2.split("-")[2]

    minute1 = penal1["minute"]
    minute2 = penal2["minute"]
    
    if year1 < year2:          
        return True
    elif year1 == year2 and month1 < month2:
        return True
    elif year1 == year2 and month1 == month2 and day1 < day2:
        return True




def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

def results_size_resultados(catalog):
    return lt.size(catalog['resultados'])

def results_size_anotaciones(catalog):
    return lt.size(catalog['anotaciones'])

def results_size_penales(catalog):
    return lt.size(catalog['penales'])
