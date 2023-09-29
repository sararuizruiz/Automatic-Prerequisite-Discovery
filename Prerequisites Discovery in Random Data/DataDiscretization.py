# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:55:59 2020

@author: Sara
"""

import xlrd
import xlsxwriter
librodatos = xlrd.open_workbook('100alumnos5temas.xlsx')
hojadatos = librodatos.sheet_by_index(0)

librodiscretizado = xlsxwriter.Workbook('discretizado1005.xlsx')
hojadiscretizada = librodiscretizado.add_worksheet()

numalumnos = hojadatos.nrows
numtemas = hojadatos.ncols

for alumno in range(numalumnos):
    for tema in range(numtemas):
        if hojadatos.cell_value(alumno,tema)<= 0:
            hojadiscretizada.write(alumno,tema,0)
        else:
            hojadiscretizada.write(alumno,tema,1)

librodiscretizado.close()