import numpy as np

from ...SistemasLineales import MetodoGaussSeidel

class Spline_GeneralAut:
    def __init__(self,conjuntoPuntos:np.array):
        """
            Clase base para calcular y evaluar 
            la interpolación por splines cúbicos
            de forma artesanal.         

            conjuntoPuntos : np.ndarray :: Conjuntos
            de puntos que serán interpolados con
            la interpolación de Newton
        """
        self.puntosX = conjuntoPuntos[:,0]
        self.puntosY = conjuntoPuntos[:,1]
        self.PolinomiosCubicos()

    def __call__(self,valorX:float) -> float:
        """
            Método que permite evaluar el
            spline cúbico en un punto dado

            valorX : float :: Valor
            en donde se evalúa el polinomio

            Devuelve el valor del spline en
            el valor dado
        """
        if valorX < self.puntosX[0]:
            evaluacion = None
        elif valorX < self.puntosX[-1]:
            indice_polinomio = __BusquedaBinaria(valorX,self.puntosX)
            _valor_binomio = valorX-self.puntosX[indice_polinomio]
            evaluacion = self.puntosY[indice_polinomio] + self.VectorCoeficientes_B[indice_polinomio]*_valor_binomio + self.VectorCoeficientes_C[indice_polinomio]*_valor_binomio**2 + self.VectorCoeficientes_D[indice_polinomio]*_valor_binomio**3
        elif valorX == self.puntosX[-1]:
            evaluacion = self.puntosY[-1]
        else:
            evaluacion = None
        return evaluacion

    def PolinomiosCubicos(self):
        """
            Método que calcula los polinomios
            asociados a los splines cúbicos en
            cada par de puntos consecutivos.
            Se usa definir la matriz de coeficientes
            en términos del término c_i (coeficiente
            cuadrático de los polinomios)
        """
        self._deltas_X = self.__Deltas(self.puntosX)
        self._deltas_Y = self.__Deltas(self.puntosY)
        n = len(self.puntosX)
        _primera_fila_Matriz_Coeficientes_C , _ultima_fila_Matriz_Coeficientes_C = self._CondicionFrontera_MatrizC()
        Matriz_Coeficientes_C = [_primera_fila_Matriz_Coeficientes_C]
        _primera_entrada_VectorIndependiente , _ultima_entrada_VectorIndependiente = self._CondicionFrontera_VectorIndependiente()
        vectorIndependiente_MatrizC = [_primera_entrada_VectorIndependiente]
        for i in range(n-2):
            fila_i_MatrizCoeficientes_C = [0]*i + [self._deltas_X[i],2*(self._deltas_X[i]+self._deltas_X[i+1]),self._deltas_X[i+1]] + [0]*(n-i-3)
            Matriz_Coeficientes_C.append(fila_i_MatrizCoeficientes_C)
            vectorIndependiente_MatrizC.append(3*(self._deltas_Y[i+1]/self._deltas_X[i+1] - self._deltas_Y[i]/self._deltas_X[i]))
        Matriz_Coeficientes_C.append(_ultima_fila_Matriz_Coeficientes_C)
        vectorIndependiente_MatrizC.append(_ultima_entrada_VectorIndependiente)
        self.Matriz_Coeficientes_C = np.array(Matriz_Coeficientes_C,dtype=float)
        self.vector_IndpendienteSistema_C = np.array(vectorIndependiente_MatrizC,dtype=float)
        self.VectorCoeficientes_C = self.__SolucionarSistema_Coeficientes_C()
        self.VectorCoeficientes_B = self.__SolucionarCoeficientes_B()
        self.VectorCoeficientes_D = self.__SolucionarCoeficientes_D()

    def __Deltas(self,puntos:np.array) -> np.ndarray:
        """
            Método auxiliar para calcular los
            incrementos sobre un mismo eje en
            un conjunto de observaciones.
            puntos : np.array :: Conjunto de
            observaciones sobre las que se
            calculan los incrementos.

            Devuelve el vector de los incrementos
        """
        return puntos[1:] - puntos[:-1]
    
    def _CondicionFrontera_MatrizC(self) -> tuple[list[float],list[float]]:
        """
            Método que devuelve la primera y última 
            fila de la matriz de coeficientes 
            asociada a los coeficientes C_i dada 
            una condición de frontera.

            Devuelve las filas de la matriz.
        """
        pass

    def _CondicionFrontera_VectorIndependiente(self) -> tuple[float,float]:
        """
            Método que devuelve la primera y última 
            entrada del vector de términos 
            independientes asociado al sistema para 
            calcular los coeficientes C_i

            Devuelve las entradas del vector
        """
        pass

    def __SolucionarSistema_Coeficientes_C(self) -> np.ndarray:
        """
            Método auxiliar para calcular los valores
            de los coeficientes C_i de los polinomios
            cúbicos.

            Devuelve el vector con los valores de los
            coeficientes C_i.
        """
        return MetodoGaussSeidel(self.Matriz_Coeficientes_C,self.vector_IndpendienteSistema_C)

    def __SolucionarCoeficientes_B(self) -> np.ndarray:
        """
            Método auxiliar que calcula los coeficientes
            B_i en base a los valores de los coeficientes
            C_i

            Devuelve los coeficientes B_i
        """
        coeficientes_B = []
        n = len(self.puntosX)
        for i in range(n-1):
            valor_B = self._deltas_Y[i]/self._deltas_X[i] - (self._deltas_X[i]/3)*(2*self.VectorCoeficientes_C[i]+self.VectorCoeficientes_C[i+1])
            coeficientes_B.append(valor_B)
        return np.array(coeficientes_B,dtype=float)

    def __SolucionarCoeficientes_D(self) -> np.ndarray:
        """
            Método auxiliar que calcula los coeficientes
            D_i en base a los valores de los coeficientes
            C_i

            Devuelve los coeficientes D_i
        """
        coeficientes_D = []
        n = len(self.puntosX)
        for i in range(n-1):
            valor_D = (self.VectorCoeficientes_C[i+1]-self.VectorCoeficientes_C[i])/(3*self._deltas_X[i])
            coeficientes_D.append(valor_D)
        return np.array(coeficientes_D,dtype=float)
    
def __BusquedaBinaria(valor,ListaOrdenadaElementos) -> int:
    """
        Función que permite hacer búsqueda binaria
        sobre una lista ordenada.

        valor : Valor del cual se quiere obtener
        su indice en la lista.
        ListaOrdenadaElementos : Lista o contenedor
        ordenada en que se quiere obtener el indice
        del elemento de la lista que se verifica
        la desigualdad menor o igual que el valor.

        Devuelve el indice que verifica que el valor
        sea mayor o igual.
    """
    inicio = 0
    final = len(ListaOrdenadaElementos)
    while inicio+1<final:
        medio = (inicio+final)//2
        if ListaOrdenadaElementos[medio]<=valor:
            inicio = medio
        else:
            final = medio
    return inicio