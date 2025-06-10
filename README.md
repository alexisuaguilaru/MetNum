# MetNum
## Resumen
Repositorio a modo de librería de Python que cuenta con implementaciones de algunos de los algoritmos relacionados con el área de Métodos Numéricos.

Todas las implementaciones aquí presenta solo hacen uso de Python y NumPy, es decir, es lo más puro posible respecto al uso de librerías especializadas a Cómputo y Métodos Numéricos.

## Autor, Afiliación y Contacto
Alexis Aguilar [Estudiante de Licenciatura en "Tecnologías para la Información en Ciencias" en la Universidad Nacional Autónoma de México [UNAM](https://www.unam.mx/)]: alexis.uaguilaru@gmail.com

Repositorio desarrollado para la materia "Métodos Numéricos" para la clase impartida en el semestre 2025-1.

## License
Proyecto bajo [MIT License](LICENSE)

## Introducción
El uso de [Métodos Numéricos](https://es.wikipedia.org/wiki/An%C3%A1lisis_num%C3%A9rico) permite aproximar soluciones de manera eficiente, bajo ciertas condiciones, a problemas cuya solución analítica se vuelve costosa computacionalmente. Por ello, se vuelve imprescindible el estudio y análisis de este tipo de algoritmos y procesos. 

De lo anterior, de lo que se busca hacer con este proyecto es el implementar algunos de los principales algoritmos de este campo de la computación para entender su funcionamiento y utilidad.

## Instalación y Uso
Primero, se tiene que clonar el repositorio usando el siguiente comando:
```bash
git clone https://github.com/alexisuaguilaru/MetNum.git
```
Con ello, preferentemente en un ambiente virtual de Python, instalar las librerías requeridas con el siguiente comando:
```bash
pip install -r requirements.txt
```

Para empezar a usar es tipo módulo, se tiene que estar en el mismo nivel que donde está la carpeta `MetNum/`, con ello se puede acceder a cualquier de las funciones y clases implementadas en la librearía llamándolo como si fuera cualquier otra librería por medio de la instrucción:
```python
from MetNum import *
```

### Módulos Implementados
El presente repositorio se divide en los siguientes módulos:
* **Sistemas Lineales**: Relacionado con la solución de sistemas lineales usando métodos directos e iterativos.
* **Interpolación**: Relacionado con la interpolación polinómica y splines cúbicos.
* **Mínimos Cuadrados**: Relacionado con el ajuste de curvas, tanto el caso general como polinómicos.
* **Encontrar Raíces de Funciones Escalares**: Relacionado con los métodos iterativos para encontrar la raíz de una función escalar y de sistemas de ecuaciones no lineales.
* **Derivación e Integración Numérica**: Relacionado con los algoritmos para derivar e integrar funciones de manera numérica.