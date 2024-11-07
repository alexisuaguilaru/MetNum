def __Signo(valor:float) -> int:
    """
        Función auxiliar que devuelve 
        el signo de una cantidad.

        valor : float :: Valor a calcular 
        su signo

        Devuelve el singo de valor.
    """
    return 1 if 0 < valor else -1

def __DerivadaAproximada_Invertida(valorX_1:float,valorX_2:float,valorY_1:float,valorY_2:float):
    """
        Función auxiliar que calcula 
        la pendiente (derivada aproximada) 
        entre dos puntos y devuelve su inverso 
        multiplicativo.
    
        valorX_1 : float :: Coordenada de las 
        abscisas del primer punto
        valorX_2 : float :: Coordenada de las 
        abscisas del segundo punto
        valorY_1 : float :: Coordenada de las 
        ordenadas del primer punto
        valorY_2 : float :: Coordenada de las 
        ordenadas del segundo punto

        Devuelve el inverso multiplicativo 
        de la derivada aproximada
    """
    return (valorX_2 - valorX_1)/(valorY_2 - valorY_1)