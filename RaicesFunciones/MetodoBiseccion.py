from .FuncionesAuxiliares import __Signo

def MetodoBiseccion(funcion,limiteInferiorIntervalo:float,limiteSuperiorIntervalo:float,tolerancia:float=1e-9) -> float:
    """ 
        Método que encuentra la raíz de una función 
        en un intervalo de búsqueda dado haciendo uso 
        del Método de Bisección.

        funcion :: Función de la que se quiere 
        determinar la raíz en el intervalo dado 
        limiteInferiorIntervalo : float :: Límite 
        inferior del intervalo de búsqueda 
        limiteSuperiorIntervalo : float :: Límite 
        superior del intervalo de búsqueda 
        tolerancia : float :: Tolerancia de la 
        evaluación de la función en un punto para 
        ser considerado raíz

        Devuelve la raíz de la función encontrada 
        en el intervalo dado
    """
    signo_Inferior = __Signo(funcion(limiteInferiorIntervalo))
    signo_Superior = __Signo(funcion(limiteSuperiorIntervalo))
    inferiorIntervalo , superiorIntervalo = limiteInferiorIntervalo , limiteSuperiorIntervalo
    puntoMedio = (inferiorIntervalo + superiorIntervalo)/2
    while tolerancia <= abs(evaluacion := funcion(puntoMedio)):
        signo_PuntoMedio = __Signo(evaluacion)
        if signo_Inferior != signo_PuntoMedio:
            superiorIntervalo = puntoMedio
            signo_Superior = signo_PuntoMedio
        else:
            inferiorIntervalo = puntoMedio
            signo_Inferior = signo_PuntoMedio
        puntoMedio = (inferiorIntervalo + superiorIntervalo)/2
    return puntoMedio