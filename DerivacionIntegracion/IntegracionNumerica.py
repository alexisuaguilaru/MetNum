import numpy as np

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

def IntegracionAproximada(Funcion,limiteInferiorIntegracion:float,limiteSuperiorIntegracion:float,divisiones:int=10) -> float:
    """
        Función que aproxima la integral 
        definida de una función dado el 
        intervalo que lo divide en intervalos 
        más pequeños.

        Funcion :: Función a integrar 
        limiteInferiorIntegracion : float :: Límite 
        inferior de integración
        limiteSuperiorIntegracion : float :: Límite 
        superior de integración
        divisiones : int :: Cantidad de subintervalos 
        que se usan para calcular la integral

        Devuelve el valor aproximado de la integral 
        de la función en el intervalo dado.
    """
    subintervalosDivisiones = np.linspace(limiteInferiorIntegracion,limiteSuperiorIntegracion,divisiones)
    integralEvaluada = 0
    for i_division in range(divisiones-1):
        integralEvaluada += ReglaSimpson(Funcion,subintervalosDivisiones[i_division],subintervalosDivisiones[i_division+1])
    return integralEvaluada