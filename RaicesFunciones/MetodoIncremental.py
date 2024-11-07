from .FuncionesAuxiliares import __Signo

def MetodoIncremental(funcion,limiteInferiorIntervalo:float,maxLimiteSuperiorIntervalo:float,incremento:float) -> float:
    """
        Método que permite determinar el límite 
        superior del intervalo en donde se encuentra 
        la raíz de una función.
    
        funcion :: Función de la que se quiere determinar 
        el límite superior del intervalo en donde 
        se localiza un raíz
        limiteInferiorIntervalo : float :: Límite inferior 
        del intervalo en donde se encuentra un raíz
        maxLimiteSuperiorIntervalo : float :: El máximo 
        límite superior del intervalo en el que se considera
        la búsqueda
        incremento : float :: Valor de los incrementos del 
        límite superior del intervalo

        Devuelve el límite superior del intervalo en caso de 
        que exista en el rango de búsqueda, en caso contrario 
        devuelve infinito.
    """
    estimacionAnterior = limiteInferiorIntervalo
    signo_estimacionAnterior = __Signo(funcion(estimacionAnterior))
    estimacionActual = estimacionAnterior + incremento
    while signo_estimacionAnterior == (signo_estimacionActual := __Signo(funcion(estimacionActual))):
            signo_estimacionAnterior = signo_estimacionActual
            estimacionActual += incremento
            if estimacionActual > maxLimiteSuperiorIntervalo:
                return float('inf')
    return estimacionActual