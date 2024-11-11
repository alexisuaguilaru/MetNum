import numpy as np

from ..Interpolacion.Polinomial.Lagrange import InterpolacionPolinomial_Lagrange

class InterpolacionPolinomial_Lagrange_DiffInt(InterpolacionPolinomial_Lagrange):
    def __init__(self,conjuntoPuntos:np.ndarray):
        """
            Clase para calcular y evaluar el 
            polinomio interpolante de Lagrange, 
            así como también derivarlo e 
            integrarlo.

            conjuntoPuntos : np.ndarray :: Conjuntos 
            de puntos que serán interpolados con 
            la interpolación de Lagrange
        """
        super().__init__(conjuntoPuntos)
        self.__CalcularCoeficientesPolinomioInterpolador()
        self.__CalcularFactoriales()

    def __CalcularCoeficientesPolinomioInterpolador(self):
        """
            Método auxiliar para calcular los 
            coeficientes de los términos del 
            polinomio interpolador
        """
        descomposicionPolinomios = [np.array([1,-puntoX[0]],dtype=float) for puntoX in self.puntosX]
        coeficientesPolinomiosComponentes = []
        for j_index_PolinomioComponente in range(len(self.puntosX)):
            coeficientesPolinomioComponente_j = np.array([1],dtype=float)
            for i_index_Raiz , raizPolinomio in enumerate(descomposicionPolinomios):
                if j_index_PolinomioComponente != i_index_Raiz:
                    coeficientesPolinomioComponente_j = np.fliplr(np.outer(coeficientesPolinomioComponente_j,raizPolinomio))
                    gradoPolinomioActual = len(coeficientesPolinomioComponente_j)
                    coeficientesPolinomioComponente_j = np.array([np.trace(coeficientesPolinomioComponente_j,offset=diagonal) for diagonal in range(1,-gradoPolinomioActual,-1)],dtype=float)
            coeficientesPolinomioComponente_j = coeficientesPolinomioComponente_j*self.puntosY[j_index_PolinomioComponente]/self.coeficientesPolinomiosComponentes[j_index_PolinomioComponente]
            coeficientesPolinomiosComponentes.append(coeficientesPolinomioComponente_j)
        self.coeficientesPolinomioInterpolador = sum(coeficientesPolinomiosComponentes)

    def DerivadaEvaluada(self,valorX:float,ordenDerivada:int=1) -> float:
        """
            Método para evaluar la derivada del 
            orden k en un punto del polinomio. 

            valorX : float :: Punto en donde 
            se evalúa la derivada del polinomio
            ordenDerivada : int :: Orden de la 
            derivada del polinomio

            Devuelve el valor de la derivada 
            evaluada con los parámetros dados.
        """
        derivadaEvaluada = 0
        potenciaValorX = 1
        ordenPolinomioInterpolador = len(self.coeficientesPolinomioInterpolador)
        for i_esimoTerminoPolinomio in range(ordenDerivada,ordenPolinomioInterpolador):
            derivadaEvaluada += self.coeficientesPolinomioInterpolador[-i_esimoTerminoPolinomio-1] * (self.Factoriales[i_esimoTerminoPolinomio]/self.Factoriales[i_esimoTerminoPolinomio-ordenDerivada]) * potenciaValorX 
            potenciaValorX *= valorX
        return derivadaEvaluada
    
    def IntegralDefinida(self,limiteInferiorIntegracion:float,limiteSuperiorIntegracion:float)  -> float:
        """
            Método para evaluar la integral del 
            polinomio en los límites de integración 
            dados.

            limiteInferiorIntegracion : float :: Límite 
            inferior de integración
            limiteSuperiorIntegracion : float :: Límite 
            superior de integración

            Devuelve el valor de la integral evaluada 
            en los límites de integración dados.
        """
        integralEvaluada = 0
        potenciaValorInferiorIntegracion = 1
        potenciaValorSuperiorIntegracion = 1
        for i_esimoTerminoPolinomio , i_esimoCoeficientePolinomio in enumerate(self.coeficientesPolinomioInterpolador[::-1]):
            potenciaValorInferiorIntegracion *= limiteInferiorIntegracion
            potenciaValorSuperiorIntegracion *= limiteSuperiorIntegracion
            integralEvaluada += (i_esimoCoeficientePolinomio/(i_esimoTerminoPolinomio+1)) * (potenciaValorSuperiorIntegracion - potenciaValorInferiorIntegracion) 
        return integralEvaluada