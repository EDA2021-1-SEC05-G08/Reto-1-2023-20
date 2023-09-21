﻿"""
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
 """

import config as cf
import model
import csv

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    return model.new_controller()

def load_data(catalog):

    catalog = load_resultados(catalog)
    catalog = load_anotaciones(catalog)
    catalog = load_penales(catalog)

    return catalog


def load_resultados(catalog):
    
    resultsfile = cf.data_dir + "results-utf8-"+ "small" + ".csv"
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    
    for result in input_file:
        model.add_result(catalog, result)

    return catalog


def load_anotaciones (catalog):
    
    anotacionesfile = cf.data_dir + "goalscorers-utf8-" + "small" + ".csv"
    input_file = csv.DictReader(open(anotacionesfile, encoding='utf-8'))
    
    for anotacion in input_file:
        model.add_anotacion(catalog, anotacion)

    return catalog     


def load_penales (catalog):
    
    penalesfile = cf.data_dir + "shootouts-utf8-" + "small" + ".csv"
    input_file = csv.DictReader(open(penalesfile, encoding='utf-8'))
    
    for penal in input_file:
        model.add_penal(catalog, penal)

    return catalog


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass