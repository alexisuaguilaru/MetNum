import numpy as np

from .AjusteCurva import AjusteCurva

class RegresionPolinomial(AjusteCurva):
    def __init__(self,ConjuntoPuntos:np.ndarray,OrdenPolinomio:int,ErroresExperimentales:float|np.ndarray=1.0):
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
            ErroresExperimentales : float | np.ndarray ::
            Conjunto de errores o error experimental 
            asociada a cada punto
        """
        conjuntoFunciones = [self.__PotenciaPolinomio(potencia) for potencia in range(OrdenPolinomio+1)]
        super().__init__(conjuntoFunciones,ConjuntoPuntos,ErroresExperimentales)

    def __PotenciaPolinomio(self,potencia:int):
        """
            Función auxiliar que devuelve 
            una función para evaluar x a 
            una potencia.

            potencia : int :: Potencia a 
            la que se eleva el argumento

            Devuelve una función lambda 
            que evalúa x**potencia
        """
        return lambda x: x**potencia