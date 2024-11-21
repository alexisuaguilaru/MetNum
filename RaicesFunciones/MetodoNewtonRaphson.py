import numpy as np

from ..SistemasLineales.Solucionadores.EliminacionGauss import EliminacionGauss


def MetodoNewtonRaphson(funcion,derivada_funcion,aproximacion_inicial:float,tolerancia:float=1e-9) -> float:
    """
        Método que encuentra la raíz de una función
        con una aproximación inicial dada haciendo uso
        del Método de Newton-Raphson.

        funcion :: Función de la que se quiere
        determinar la raíz con la aproximación
        inicial dada
        derivada_funcion :: Derivada de la función
        de la que queremos encontrar una raíz
        aproximacion_inicial : float :: Aproximación
        inicial de la raíz de la función
        tolerancia : float :: Tolerancia de la
        evaluación de la función en un punto para
        ser considerado raíz

        Devuelve la raíz de la función encontrada
        con la aproximación inicial dada.
    """
    aproximacion = aproximacion_inicial
    funcion_evaluada = funcion(aproximacion)
    while tolerancia <= abs(funcion_evaluada):
        aproximacion = aproximacion - funcion_evaluada/derivada_funcion(aproximacion)
        funcion_evaluada = funcion(aproximacion)
    return aproximacion

def MetodoRaicesSistemasEcuaciones(funcion_vectorial,Jacobiano_funcion,aproximacion_inicial:np.ndarray,tolerancia:float=1e-9) -> np.ndarray:
    """
        Método para determinar la solución del
        sistema de ecuaciones no lineales con
        una aproximación inical dada.

        funcion_vectorial :: Función vectorial que
        representa al sistema de ecuaciones del
        que se quiere determinar su raíz
        Jacobiano_funcion :: Jacobiano asociado
        al sistema de ecuaciones o de la
        función vectorial
        aproximacion_inicial : np.ndarray :: Vector
        inicial de la solución del sistema de ecuaciones
        tolerancia : float :: Tolerancia de la norma de la
        evaluación de la función en una aproximación para
        ser considerada raíz
    """
    aproximacion = aproximacion_inicial
    funcion_evaluada = funcion_vectorial(aproximacion)
    while tolerancia <= np.linalg.norm(funcion_evaluada):
        incremento_aproximacion = EliminacionGauss(Jacobiano_funcion(aproximacion),-funcion_evaluada)
        aproximacion += incremento_aproximacion
        funcion_evaluada = funcion_vectorial(aproximacion)
    return aproximacion