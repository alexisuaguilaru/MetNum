def DiferenciacionHaciaPaso(Funcion,valorX:float,paso:float=1e-9) -> float:
    """
        Función para calcular la derivada aproximada 
        en un punto usando diferenciación hacia delante 
        o hacia atrás según el signo del paso.

        Funcion :: Función de la que se calcula 
        su derivada
        valorX : float :: Valor en donde se calcula 
        la derivada
        paso : float :: Valor del tamaño del punto 
        que se usa para calcular la derivada

        Devuelve el valor aproximado de la derivada 
        en el punto dado.
    """
    return DiferenciaHaciaDelante(Funcion,valorX,paso) if paso > 0 else DiferenciaHaciaAtras(Funcion,valorX,-paso)

def DiferenciaHaciaDelante(Funcion,valorX:float,pasoHaciaDelante:float=1e-9) -> float:
    """
        Función para calcular la derivada aproximada 
        en un punto dado usando diferencia hacia 
        delante.

        Funcion :: Función de la que se calcula 
        su derivada
        valorX : float :: Valor en donde se calcula 
        la derivada
        pasoHaciaDelante : float :: Valor del paso 
        del siguiente valor para considerar la derivada

        Devuelve el valor aproximado de la derivada 
        en el punto dado.
    """
    return (Funcion(valorX + pasoHaciaDelante) - Funcion(valorX)) / pasoHaciaDelante

def DiferenciaHaciaAtras(Funcion,valorX:float,pasoHaciaAtras:float=1e-9) -> float:
    """
        Función para calcular la derivada aproximada 
        en un punto dado usando diferencia hacia 
        atrás.

        Funcion :: Función de la que se calcula 
        su derivada
        valorX : float :: Valor en donde se calcula 
        la derivada
        pasoHaciaDelante : float :: Valor del paso 
        del valor anterior para considerar la derivada

        Devuelve el valor aproximado de la derivada 
        en el punto dado.
    """
    return (Funcion(valorX) - Funcion(valorX - pasoHaciaAtras)) / pasoHaciaAtras