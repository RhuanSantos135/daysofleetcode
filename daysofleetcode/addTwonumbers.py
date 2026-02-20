from tokenize import OP
from typing import Any, List, Optional


class Solution:
    def addtwonumber(l1: List[int], l2: List[int]) -> List[int]:

        reverse_lista_um = list(reversed(l1))
        print(reverse_lista_um)
        reverser_lista_dois = list(reversed(l2))
        print(reverser_lista_dois)

        numero_um = int("".join(map(str, reverse_lista_um)))
        numero_dois = int("".join(map(str, reverser_lista_dois)))
        
        resultado = numero_um + numero_dois

        result_list = []



        for idx, n in enumerate(str(resultado)):
            result_list.append(int(n))
            

        print(resultado)
        print(result_list)


        
        result_list_reverser = list[int](reversed(result_list))

        return result_list_reverser
        

Solution.addtwonumber(l1=[2,4,3], l2=[5,6,4])