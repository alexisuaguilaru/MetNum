import numpy as np

class InterpolacionPolinomial_Newton:
    def __init__(self,conjuntoPuntos:np.ndarray):
        """
            Clase para calcular y evaluar el 
            polinomio interpolante de Newton.

            conjuntoPuntos : np.ndarray :: Conjuntos 
            de puntos que serán interpolados con 
            la interpolación de Newton
        """
        self.puntosX = np.array([],dtype=float)
        self.tablaDiferenciasDivididas = dict()
        self.cantidadNodos = 0
        self.CoefcientesPolinomios = np.array([],dtype=float)
        [self.addNodo(nodo) for nodo in conjuntoPuntos]

    def __call__(self,valorX:float) -> float:
        """
            Método para evaluar un valor x en 
            el polinomio interpolante de Newton.

            valorX : float :: Valor en donde se
            evalúa el polinomio

            Devuelve el valor de P_n(x)
        """
        polinomioEvaluado = self.CoefcientesPolinomios[0]
        valorVariable = 1
        for coeficientePolinomio , puntoX in zip(self.CoefcientesPolinomios[1:],self.puntosX):
            valorVariable *= (valorX-puntoX)
            polinomioEvaluado += coeficientePolinomio*valorVariable
        return polinomioEvaluado

    def addNodo(self,nodo:np.ndarray) -> None:
        """
            Método para añadir un nuevo 
            nodo a la interpolación. 
            Calcula el coeficiente asociado 
            a este nodo.

            nodo : np.ndarray :: Nodo que se 
            va a añadir a la interpolación

            No devuelve nada.
        """
        valorX , valorY = nodo
        self.puntosX = np.append(self.puntosX,[valorX])
        nodo_index = self.cantidadNodos
        self.tablaDiferenciasDivididas[(nodo_index,nodo_index)] = valorY
        for i_index in range(self.cantidadNodos-1,-1,-1):
            self.tablaDiferenciasDivididas[(i_index,nodo_index)] = (self.tablaDiferenciasDivididas[(i_index+1,nodo_index)]-self.tablaDiferenciasDivididas[(i_index,nodo_index-1)])/(self.puntosX[nodo_index]-self.puntosX[i_index])
        self.CoefcientesPolinomios = np.append(self.CoefcientesPolinomios,[self.tablaDiferenciasDivididas[(0,self.cantidadNodos)]])
        self.cantidadNodos += 1