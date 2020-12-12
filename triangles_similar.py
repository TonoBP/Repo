from typing import List, Tuple
import math
Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:

    # your code here
    # calculate the dimension of every side of triangle 1
    a_1 = (math.sqrt(((coords_1[0][0] - coords_1[1][0])**2)+((coords_1[0][1] - coords_1[1][1])**2)))
    b_1 = (math.sqrt(((coords_1[0][0] - coords_1[2][0])**2)+((coords_1[0][1] - coords_1[2][1])**2)))
    c_1 = (math.sqrt(((coords_1[1][0] - coords_1[2][0])**2)+((coords_1[1][1] - coords_1[2][1])**2)))
    lista_1 = [(a_1), (b_1), (c_1)]
    lista_1.sort()


    # calculate the dimension of every side of triangle 1
    a_2 = (math.sqrt(((coords_2[0][0] - coords_2[1][0])**2)+((coords_2[0][1] - coords_2[1][1])**2)))
    b_2 = (math.sqrt(((coords_2[0][0] - coords_2[2][0])**2)+((coords_2[0][1] - coords_2[2][1])**2)))
    c_2 = (math.sqrt(((coords_2[1][0] - coords_2[2][0])**2)+((coords_2[1][1] - coords_2[2][1])**2)))
    lista_2 = [(a_2), (b_2), (c_2)]
    lista_2.sort()
    print(lista_1, lista_2)

    # check if sides are equal or proportional
    compare = [lista_1[i]/lista_2[i] for i in range(3)]

    #if (lista_1[0]/lista_2[0] - lista_1[1]/lista_2[1]) and (lista_1[0]/lista_2[0] - lista_1[2]/lista_2[2]) in range(-1, 1):
    #and (lista_1[0]/lista_2[0] - lista_1[2]/lista_2[2])
    if len(set(compare)) == 1:
        print(True)
    #else:
        #return False
similar_triangles([[1,3],[2,5],[3,3]],[[1,2],[-1,0],[1,0]])
