import numpy as np

import sys
sys.path.insert(2,'../..')
from MetNum.SistemasLineales.Solucionadores.EliminacionGauss import EliminacionGaussPivoteo

class AjusteCurva:
    def __init__(self,ConjuntoFunciones:list,ConjuntoPuntos:np.ndarray):
        """
            Clase base para realizar cualquier ajuste 
            de curva sobre un conjunto de datos usando 
            una combinación lineal de funciones 
            linealmente independientes.

            ConjuntoFunciones : list :: Conjunto de 
            funciones linealmente independiente que 
            se usan como modelo para el ajuste de 
            curva
            ConjuntoPuntos : np.ndarray :: Conjunto 
            de datos que se usan para ajustar la 
            curva del modelo dado por las funciones
        """
        self.puntosX  = ConjuntoPuntos[:,0]
        self.puntosY  = ConjuntoPuntos[:,1]
        self.ConjuntoFunciones = ConjuntoFunciones
        self.__Fit()

    def __call__(self,valorX:float) -> float:
        """
            Método para evaluar la curva de 
            ajuste encontrada en un punto dado.

            valorX : float :: Valor en el que 
            se quiere evaluar

            Devuelve el valor de la evaluación 
            de ajuste de la curva.
        """
        evaluacionCurvaAjuste = 0
        for coeficientePesoFuncion , funcionBase in zip(self.__coeficientesCombinacionesLineales,self.ConjuntoFunciones):
            evaluacionCurvaAjuste += coeficientePesoFuncion*funcionBase(valorX)
        return evaluacionCurvaAjuste

    def __Fit(self):
        """
            Método auxiliar para encontrar la 
            curva de ajuste como combinación 
            lineal de las funciones base usando 
            mínimos cuadrados

            No devuelve nada  
        """
        funcionesEvaluadas = []
        for funcionBase in self.ConjuntoFunciones:
            funcionesEvaluadas.append([funcionBase(valorX) for valorX in self.puntosX])
        funcionesEvaluadas = np.array(funcionesEvaluadas,dtype=float)
        matrizErrorDerivado = funcionesEvaluadas@funcionesEvaluadas.T
        vectorIndependienteErrorDerivado = funcionesEvaluadas@self.puntosY.T
        self.__coeficientesCombinacionesLineales = EliminacionGaussPivoteo(matrizErrorDerivado,vectorIndependienteErrorDerivado)