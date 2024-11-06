import numpy as np

from .RegresionLineal import RegresionLineal

class CurvaExponencial(RegresionLineal):
    def __init__(self,ConjuntoPuntos:np.ndarray,ErroresExperimentales:float|np.ndarray=1.0):
        """
            Clase para realizar ajuste de curvas 
            exponenciales sobre un conjunto de 
            datos usando a_0e^{a_1t}

            ConjuntoPuntos : np.ndarray :: Conjunto 
            de datos que se usan para ajustar la 
            curva
            ErroresExperimentales : float | np.ndarray ::
            Conjunto de errores o error experimental 
            asociada a cada punto.
        """
        ConjuntoPuntos_Logaritmicos = np.array([ConjuntoPuntos[:,0],np.log(ConjuntoPuntos[:,1])],dtype=float).T
        super().__init__(ConjuntoPuntos_Logaritmicos,ErroresExperimentales)
    
    def __call__(self,valorX):
        return np.exp(super().__call__(valorX))