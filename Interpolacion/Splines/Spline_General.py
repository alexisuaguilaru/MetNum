import scipy
import numpy as np

class Spline_General:
      def __init__(self,conjuntoPuntos:np.ndarray,bc_type):
        """
            Clase general para la definición y evaluación 
            de splines cúbicos con diferentes condiciones de 
            frontera.

            conjuntoPuntos : np.array :: Conjuntos de
            puntos en donde se define el spline
            bc_type :: Tipo de condición de borde 
            definida por SciPy para su clase de CubicSpline
        """
        self.puntosX = conjuntoPuntos[:,0]
        self.puntosY = conjuntoPuntos[:,1]
        self.Spline = scipy.interpolate.CubicSpline(self.puntosX,self.puntosY,bc_type=bc_type)
  
      def __call__(self,puntoX:float) -> float:
        """
          Método que permite evaluar el spline
          en un perteneciente al intervalo de
          definición
  
          puntoX : float :: Punto en donde
          se está evaluando el spline

          Devuelve el valor que toma el spline 
          en el punto dado.
        """
        return self.Spline(puntoX)