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

from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort

from datetime import datetime
import time as time
from tabulate import tabulate

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

def add_result(catalog, resultado):
    lt.addLast(catalog['resultados'], resultado)
    return catalog

def add_anotacion(catalog, anotacion):

    if anotacion["scorer"] == "":
        anotacion["scorer"] = "Desconocido"

    if anotacion["minute"] == "":
        anotacion["minute"] = -1

    lt.addLast(catalog['anotaciones'], anotacion)
    return catalog

def add_penal(catalog, penal):
    lt.addLast(catalog['penales'], penal)
    return catalog

# Funciones de consulta

def req_1(catalog, numero_partidos, nombre_equipo, condicion_equipo):
    """
    Función que soluciona el requerimiento 1
    """

    resultados = catalog['resultados']
    pos = lt.size(resultados)-1
    cantidad_total = 0

    partidos = lt.newList("ARRAY_LIST")
    if condicion_equipo == 1:
        condicion_equipo = "home_team"
    elif condicion_equipo == 2:
        condicion_equipo = "away_team"
    elif condicion_equipo == 3:
        condicion_equipo = "indiferente"

    while pos > 0:

        partido = lt.getElement(resultados, pos)

        if condicion_equipo == "indiferente" and (partido["home_team"] == nombre_equipo or partido["away_team"] == nombre_equipo):
            cantidad_total += 1
            if lt.size(partidos) < numero_partidos:
                lt.addFirst(partidos, partido)

        elif condicion_equipo != "indiferente" and partido[condicion_equipo] == nombre_equipo:
            cantidad_total += 1
            if lt.size(partidos) < numero_partidos:
                lt.addFirst(partidos, partido)
        pos-=1

    return partidos, cantidad_total, lt.size(partidos), condicion_equipo
        

def req_2(catalog, nombre_jugador, numero_goles):
    """
    Función que soluciona el requerimiento 2
    """
    
    goles_lista= lt.newList("ARRAY_LIST")
    goles_total = 0

    anotaciones = catalog["anotaciones"]

    for pos in range (1, lt.size(anotaciones)):

        anotacion = lt.getElement(anotaciones, pos)

        if anotacion["scorer"] == nombre_jugador:
            goles_total += 1
            if lt.size(goles_lista) < numero_goles:
                lt.addLast(goles_lista, anotacion)

    return goles_lista, goles_total

def req_3(catalog, equipo_nombre, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 3
    """

    resultados = catalog['resultados']
    anotaciones = catalog['anotaciones']
    fecha_inicial = getFecha(fecha_inicial)
    fecha_final = getFecha(fecha_final)

    partidos = lt.newList("ARRAY_LIST")
    cantidad_total = 0
    cantidad_total_locales = 0
    cantidad_total_visitantes = 0

    for i in range(1, lt.size(resultados)):

        partido = lt.getElement(resultados, i)
        fecha_partido = getFecha(partido['date'])


        if fecha_inicial <= fecha_partido <= fecha_final and (partido["home_team"] == equipo_nombre or partido["away_team"] == equipo_nombre):

            autogol = False
            penalti = False

            cantidad_total += 1
            if partido["home_team"] == equipo_nombre:
                cantidad_total_locales += 1
            else:
                cantidad_total_visitantes += 1

            for j in range(1, lt.size(anotaciones)):
                anotacion = lt.getElement(anotaciones, j)
                anotacion_fecha = getFecha(anotacion['date'])
                anotacion_local = anotacion['home_team']
                anotacion_visitante = anotacion['away_team']
                if anotacion_fecha == fecha_partido and (anotacion_local == equipo_nombre or anotacion_visitante == equipo_nombre):
                    if not autogol and getBool(anotacion["own_goal"]):
                        autogol = True
                    if not penalti and getBool(anotacion["penalty"]):
                        penalti = True

            partido["penalty"] = penalti
            partido["own_goal"] = autogol

            lt.addLast(partidos, partido)

    return partidos, cantidad_total, cantidad_total_locales, cantidad_total_visitantes


def req_4(catalog, torneo, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 4
    """

    resultados = catalog['resultados']
    penales = catalog['penales']
    fecha_inicial = getFecha(fecha_inicial)
    fecha_final = getFecha(fecha_final)

    partidos = lt.newList("ARRAY_LIST")
    paises = lt.newList("ARRAY_LIST")
    ciudades = lt.newList("ARRAY_LIST")
    definidos_penales = 0

    for i in range(1, lt.size(resultados)):

        partido = lt.getElement(resultados, i)
        fecha_partido = getFecha(partido['date'])


        if fecha_inicial <= fecha_partido <= fecha_final and partido["tournament"] == torneo:

            if not lt.isPresent(paises, partido['country']):
                lt.addLast(paises, partido['country'])
            if not lt.isPresent(ciudades, partido['city']):
                lt.addLast(ciudades, partido['city'])

            partido_local = partido['home_team']
            partido_visitante = partido['away_team']
            partido["definido en penales"] = False
            partido["ganador en penales"] = "No aplica"
            for j in range(1, lt.size(penales)):
                tiempo_penal = lt.getElement(penales, j)
                tiempo_penal_fecha = getFecha(tiempo_penal['date'])
                tiempo_penal_local = tiempo_penal['home_team']
                tiempo_penal_visitante = tiempo_penal['away_team']
                if tiempo_penal_fecha == fecha_partido and partido_local == tiempo_penal_local and partido_visitante == tiempo_penal_visitante:
                    partido["definido en penales"] = True
                    partido["ganador en penales"] = tiempo_penal['winner']
                    definidos_penales += 1

            lt.addLast(partidos, partido)

    partidos = mergesort.sort(partidos, compare_paises)
    partidos = mergesort.sort(partidos, compare_ciudades)

    return partidos, lt.size(partidos), lt.size(paises), lt.size(ciudades), definidos_penales


def req_5(catalog, jugador_nombre, fecha_inicial, fecha_final):
    """
    Función que soluciona el requerimiento 5
    """

    resultados = catalog['resultados']
    anotaciones = catalog['anotaciones']
    fecha_inicial = getFecha(fecha_inicial)
    fecha_final = getFecha(fecha_final)

    jugador_anotaciones_lista = lt.newList("ARRAY_LIST")
    jugador_torneos = lt.newList("ARRAY_LIST")
    jugador_anotaciones = 0
    jugador_anotaciones_nopenal = 0
    jugador_anotaciones_penal = 0
    jugador_anotaciones_autogol = 0

    for i in range(1, lt.size(anotaciones)):

        anotacion = lt.getElement(anotaciones, i)

        anotacion_fecha = getFecha(anotacion['date'])
        resultado_home_score = 0
        resultado_away_score = 0
        anotacion_penal = False
        anotacion_autogol = False
        anotacion_toreno = ""

        if fecha_inicial <= anotacion_fecha <= fecha_final and anotacion["scorer"] == jugador_nombre:

            jugador_anotaciones += 1
            if getBool(anotacion['penalty']):
                jugador_anotaciones_penal += 1
                anotacion_penal = True
            else:
                jugador_anotaciones_nopenal += 1
            if getBool(anotacion['own_goal']):
                jugador_anotaciones_autogol += 1
                anotacion_autogol = True

            anotacion_local = anotacion['home_team']
            anotacion_visitante = anotacion['away_team']
            for j in range(1, lt.size(resultados)):
                resultado = lt.getElement(resultados, j)
                resultado_fecha = getFecha(resultado['date'])
                resultado_local = resultado['home_team']
                resultado_visitante = resultado['away_team']
                if resultado_fecha == anotacion_fecha and resultado_local == anotacion_local and resultado_visitante == anotacion_visitante:
                    print("--")
                    resultado_home_score = resultado['home_score']
                    resultado_away_score = resultado['away_score']
                    resultado_torneo = resultado['tournament']
                    anotacion_toreno = resultado_torneo
                    if not lt.isPresent(jugador_torneos, resultado_torneo):
                        lt.addLast(jugador_torneos, resultado_torneo)

            anotacion["home_score"] = resultado_home_score
            anotacion["away_score"] = resultado_away_score
            anotacion["tournament"] = anotacion_toreno
            anotacion["penalty"] = anotacion_penal
            anotacion["own_goal"] = anotacion_autogol

            lt.addLast(jugador_anotaciones_lista, anotacion)

    return jugador_anotaciones_lista, jugador_anotaciones, lt.size(jugador_torneos), jugador_anotaciones_penal, jugador_anotaciones_autogol


def req_6(catalog):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(catalog):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(catalog):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

# Funciones para comparación

def compare_paises(resultado1, resultado2):

    country1 = resultado1["country"]
    country2 = resultado2["country"]

    if resultado1["date"] == resultado2["date"]:
        if country1 < country2:
            return True
        else: 
            return False 

def compare_fechas(diccionario_1, diccionario_2):

    fecha_1 = diccionario_1["date"] 
    fecha_2 = diccionario_2["date"] 

    fecha_1 = datetime.strptime(fecha_1, "%Y-%m-%d")
    fecha_2 = datetime.strptime(fecha_2, "%Y-%m-%d")
    
    if fecha_1 < fecha_2:
        return True
    else:
        return False
    
def compare_puntajes(resultado_1, resultado_2):

    fecha_1 = resultado_1["date"]
    puntaje_local_1 = resultado_1["home_score"]
    puntaje_visitante_1 = resultado_1["away_score"]

    fecha_2 = resultado_2["date"]
    puntaje_local_2 = resultado_2["home_score"]
    puntaje_visitante_2 = resultado_2["away_score"]

    if fecha_1 == fecha_2:
        if puntaje_local_1 > puntaje_local_2:
            return True
        elif puntaje_local_1 < puntaje_local_2:
            return False
        elif puntaje_local_1 == puntaje_local_2:
            if puntaje_visitante_1 > puntaje_visitante_2:
                return True
            elif puntaje_visitante_1 <= puntaje_visitante_2:
                return False
    
def compare_minutos(anotacion_1, anotacion_2):

    fecha_1 = anotacion_1["date"]
    minuto_1 = float(anotacion_1['minute'])

    fecha_2 = anotacion_2["date"]
    minuto_2 = float(anotacion_2['minute'])

    if fecha_1 == fecha_2:
        if minuto_1 < minuto_2:
            return True
        elif minuto_1 > minuto_2:
            return False
        
def compare_jugadores(anotacion_1, anotacion_2):

    fecha_1 = anotacion_1["date"]
    minuto_1 = float(anotacion_1['minute'])
    jugador_1 = anotacion_1['scorer']

    fecha_2 = anotacion_2["date"]
    minuto_2 = float(anotacion_2['minute'])
    jugador_2 = anotacion_2['scorer']

    if fecha_1 == fecha_2 and minuto_1 == minuto_2:
        if jugador_1 < jugador_2:
            return True
        elif jugador_1 >= jugador_2:
            return False

def compare_equipos(penal_1, penal_2):

    fecha_1 = penal_1["date"]
    equipo_local_1 = penal_1['home_team']
    equipo_visitante_1 = penal_1['away_team']

    fecha_2 = penal_2["date"]
    equipo_local_2 = penal_2['home_team']
    equipo_visitante_2 = penal_2['away_team']

    if fecha_1 == fecha_2:
        if equipo_local_1 < equipo_local_2:
            return True
        elif equipo_local_1 > equipo_local_2:
            return False
        elif equipo_local_1 == equipo_local_2:
            if equipo_visitante_1 < equipo_visitante_2:
                return True
            elif equipo_visitante_1 >= equipo_visitante_2:
                return False

def compare_ciudades(resultado_1, resultado_2):

    fecha_1 = resultado_1["date"]
    fecha_2 = resultado_2["date"]
    country_1 = resultado_1["country"]
    country_2 = resultado_2["country"]
    city_1 = resultado_1["city"]
    city_2 = resultado_2["city"]

    if fecha_1 == fecha_2 and country_1 == country_2:
        if city_1 < city_2:
            return True
        else: 
            return False 


# Funciones de ordenamiento

def ordenar_resultados(resultados):

    resultados = mergesort.sort(resultados, compare_fechas)
    resultados = mergesort.sort(resultados, compare_puntajes)

    primero = lt.getElement(resultados, 0)
    lt.addLast(resultados, primero)

    return resultados

def ordenar_anotaciones(anotaciones):

    anotaciones = mergesort.sort(anotaciones, compare_fechas)
    anotaciones = mergesort.sort(anotaciones, compare_minutos)
    anotaciones = mergesort.sort(anotaciones, compare_jugadores)

    primero = lt.getElement(anotaciones, 0)
    lt.addLast(anotaciones, primero)

    return anotaciones

def ordenar_penales(penales):

    penales = mergesort.sort(penales, compare_fechas)
    penales = mergesort.sort(penales, compare_equipos)

    primero = lt.getElement(penales, 0)
    lt.addLast(penales, primero)

    return penales

# Funciones de auxiliares

def getSize(lista):
    return lt.size(lista)-1

def getTabla(lista):

    headers = list(lt.getElement(lista, 0).keys())
    data = []

    if lt.size(lista) < 6:

        for i in range(lt.size(lista)):
            data.append(list(lt.getElement(lista, i).values()))

    else:

        for i in range(1, 4):
            data.append(list(lt.getElement(lista, i).values()))

        for i in range(getSize(lista)-1, lt.size(lista)+1):
            data.append(list(lt.getElement(lista, i).values()))

    return tabulate(data, headers)

def getFecha(fecha):
    return datetime.strptime(fecha , "%Y-%m-%d")

def getBool(string):
    return True if string == 'True' else False