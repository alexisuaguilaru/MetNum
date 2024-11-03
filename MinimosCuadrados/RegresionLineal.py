import numpy as np

from .RegresionPolinomial import RegresionPolinomial

class RegresionLineal(RegresionPolinomial):
  def __init__(self,ConjuntoPuntos:np.ndarray,ErroresExperimentales:float|np.ndarray=1.0):
    """
        Clase para realizar regresión lineal 
        sobre un conjunto de datos usando un 
        polinomio de orden 1.

        ConjuntoPuntos : np.ndarray :: Conjunto 
        de datos que se usan para ajustar la 
        curva
        ErroresExperimentales : float | np.ndarray ::
        Conjunto de errores o error experimental 
        asociada a cada punto.
    """
    ordenPolinomio = 2
    super().__init__(ConjuntoPuntos,ordenPolinomio,ErroresExperimentales)