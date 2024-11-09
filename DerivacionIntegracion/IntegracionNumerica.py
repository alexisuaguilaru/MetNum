def ReglaTrapezoidal(Funcion,limiteInferiorIntegracion:float,limiteSuperiorIntegracion:float) -> float:
    """
        Función para integral de forma definida 
        una función entre los límites de integración 
        dados usando la regla trapezoidal

        Funcion :: Función a integrar
        limiteInferiorIntegracion : float :: Límite 
        inferior de integración
        limiteSuperiorIntegracion : float :: Límite 
        superior de integración

        Devuelve el valor aproximado de la integral 
        de la función en el intervalo dado.
    """
    diferenciaIntervalo = (limiteSuperiorIntegracion - limiteInferiorIntegracion)/2
    return diferenciaIntervalo * (Funcion(limiteInferiorIntegracion) + Funcion(limiteSuperiorIntegracion))

def ReglaSimpson(Funcion,limiteInferiorIntegracion:float,limiteSuperiorIntegracion:float) -> float:
    """
        Función para integral de forma definida 
        una función entre los límites de integración 
        dados usando la regla de Simpson

        Funcion :: Función a integrar
        limiteInferiorIntegracion : float :: Límite 
        inferior de integración
        limiteSuperiorIntegracion : float :: Límite 
        superior de integración

        Devuelve el valor aproximado de la integral 
        de la función en el intervalo dado.
    """
    diferenciaIntervalo = (limiteSuperiorIntegracion - limiteInferiorIntegracion)/2
    puntoMedio = (limiteInferiorIntegracion + limiteSuperiorIntegracion)/2
    return (diferenciaIntervalo/3) * (Funcion(limiteInferiorIntegracion) + 4*Funcion(puntoMedio) + Funcion(limiteSuperiorIntegracion))