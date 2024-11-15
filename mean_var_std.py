import numpy as np

def calculadora(lista):

    # Validar largo de la lista, debe ser de 9 elementos
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve numeros")
    
    # Convertir lista en una matriz de 3x3
    matriz = np.array(lista).reshape(3, 3)

    # Generar diccionario con los datos estadísticos
    Diccionario_calc = {
        'media': [
            matriz.mean(axis=0).tolist(),  # Media columnas
            matriz.mean(axis=1).tolist(),  # Media filas
            matriz.mean()  # Media elementos
        ],
        'varianza': [
            matriz.var(axis=0).tolist(),  # Varianza columnas
            matriz.var(axis=1).tolist(),  # Varianza filas
            matriz.var()  # Varianza elementos
        ],
        'desviacion estandar': [
            matriz.std(axis=0).tolist(),  # Desviación estándar columnas
            matriz.std(axis=1).tolist(),  # Desviación estándar filas
            matriz.std()  # Desviación estándar elementos
        ],
        'maximo': [
            matriz.max(axis=0).tolist(),  # Máximo columnas
            matriz.max(axis=1).tolist(),  # Máximo filas
            matriz.max()  # Máximo elementos
        ],
        'minimo': [
            matriz.min(axis=0).tolist(),  # Mínimo columnas
            matriz.min(axis=1).tolist(),  # Mínimo filas
            matriz.min()  # Mínimo elementos
        ],
        'suma': [
            matriz.sum(axis=0).tolist(),  # Suma columnas
            matriz.sum(axis=1).tolist(),  # Suma filas
            matriz.sum()  # Suma elementos
        ]
    }

    return Diccionario_calc