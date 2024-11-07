from .FuncionesAuxiliares import __DerivadaAproximada_Invertida

def MetodoSecante(funcion,limiteInferiorIntervalo:float,limiteSuperiorIntervalo:float,tolerancia:float=1e-9) -> float:
    """
        Método que encuentra la raíz de una función 
        en un intervalo de búsqueda dado haciendo uso 
        del Método de la Secante

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
    estimacionAnterior , estimacionActual = limiteInferiorIntervalo , limiteSuperiorIntervalo
    evaluacionAnterior , evaluacionActual = funcion(estimacionAnterior) , funcion(estimacionActual)
    estimacionSiguiente = estimacionActual - evaluacionActual * __DerivadaAproximada_Invertida(estimacionAnterior,estimacionActual,evaluacionAnterior,evaluacionActual)
    while tolerancia <= abs(evaluacionsiguiente := funcion(estimacionSiguiente)):
        estimacionAnterior , estimacionActual = estimacionActual , estimacionSiguiente
        evaluacionAnterior , evaluacionActual = evaluacionActual , evaluacionsiguiente
        estimacionSiguiente = estimacionActual - evaluacionActual * __DerivadaAproximada_Invertida(estimacionAnterior,estimacionActual,evaluacionAnterior,evaluacionActual)
    return estimacionSiguiente