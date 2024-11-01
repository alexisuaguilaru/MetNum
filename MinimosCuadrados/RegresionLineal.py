import numpy as np

from .RegresionPolinomial import RegresionPolinomial

class RegresionLineal(RegresionPolinomial):
  def __init__(self,ConjuntoPuntos:np.ndarray):
    """
        Clase para realizar regresión lineal 
        sobre un conjunto de datos usando un 
        polinomio de orden 1.

        ConjuntoPuntos : np.ndarray :: Conjunto 
        de datos que se usan para ajustar la 
        curva
    """
    ordenPolinomio = 2
    super().__init__(ConjuntoPuntos,ordenPolinomio)