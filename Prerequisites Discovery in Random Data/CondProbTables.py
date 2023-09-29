# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:24:50 2020

@author: Sara
"""

# En este fichero lo que pretendo es, una vez sacados los prerequisitos,
# ya puedo dibujar la estructura de la red (sus nodos y sus aristas direccionales)
# Lo que me falta es sacar las tablas de prob condicionadas y es lo que vamos a hacer:

from sacoprerequisitos import *
#print(prerequisitos)

padres = [] # Voy a reestructurar prerequisitos, tendré la misma información pero
            # ordenada de la siguiente manera: [[[t1],[padres del t1]],[[t2],[padres del t2]],...]
            
for i in range(numtemas):
    temp = []
    for [[t1,t2],[j]] in prerequisitos:
        if (t2==i and j==1):
            temp.append(t1)
    padres.append([[i],temp])
    
print(padres)

## Ahora, para sacar la tabla de prob condicionada de cada nodo, vamos a tener que observar 2^n casos si n es el numero de padres que tiene

posibilidades = []

for [[t1],padrest1] in padres:
    pos = [[]]
    for padre in padrest1:
        for ex in pos:
            extra = ex.copy()
            ex.append(0)
            extra.append(1)
            pos.append(extra)       
    posibilidades.append([[t1],pos])
            
print(posibilidades)