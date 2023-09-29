
from random import uniform
import xlsxwriter

libro = xlsxwriter.Workbook('100alumnos5temas.xlsx')
hoja = libro.add_worksheet()

numalumnos = 100
numtemas = 5

datos = []
for alumnos in range(numalumnos):
    for temas in range(numtemas):
        datos.append(uniform(-1,1))
      

for i in range(len(datos)):
    hoja.write(i//numtemas, i%numtemas, datos[i])

libro.close()