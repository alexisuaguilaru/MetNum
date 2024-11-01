import numpy as np

from AjusteCurvaMinimosCuadrados import AjusteCurva

class RegresionPolinomial(AjusteCurva):
    def __init__(self,ConjuntoPuntos:np.ndarray,OrdenPolinomio:int):
        """
            Clase para realizar regresión polinomial 
            sobre un conjunto de datos usando un 
            polinomio de orden N.

            ConjuntoPuntos : np.ndarray :: Conjunto 
            de datos que se usan para ajustar la 
            curva
            OrdenPolinomio : int :: Orden del 
            polinomio que se usa para ajustarlo a 
            un conjunto de datos
        """
        conjuntoFunciones = [lambda x: x**i for i in range(OrdenPolinomio+1)]
        super().__init__(conjuntoFunciones,ConjuntoPuntos)