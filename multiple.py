"""
Ejercicio 2
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del
otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo
del segundo.
"""

def EsMultiplo(n1: int, n2: int):
    if n1 % n2 == 0:
        return f"{n1} => {n2}"
    elif n2 % n1 == 0:
        return f"{n1} <= {n2}" 
    else:
        return f"{n1} != {n2}"


def multiplo3(n1: int, n2: int, n3: int):
    res1 = EsMultiplo(n1, n2)
    res2 = EsMultiplo(n2, n3)

    if "=>" in res1 and "=>" in res2:
        return f"{n1} => {n2} => {n3}"
    elif "<=" in res1 and "<=" in res2:
        return f"{n1} <= {n2} <= {n3}"
    elif "<=" in res1 and "!=" in res2:
        return f"{n1} <= {n2} != {n3}"
    elif "!=" in res1 and "<=" in res2:
        return f"{n1} != {n2} <= {n3}"
    elif "=>" in res1 and "!=" in res2:
        return f"{n1} => {n2} != {n3}"
    elif "!=" in res1 and "=>" in res2:
        return f"{n1} != {n2} => {n3}"
    elif "!=" in res1 and "!=" in res2:
        return f"{n1} != {n2} != {n3}"


print(multiplo3(5, 4, 8))
