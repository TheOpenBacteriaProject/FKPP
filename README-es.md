# FKPP on 1 dimension

![](https://raw.githubusercontent.com/TheOpenBacteriaProject/Branding/master/Documentation-Media/Document-Header.png)

## Directorios

* *Documentation* contiene toda la documentación matemática.
* *Python* contiene los códigos de nuestros programas.
* *images* contiene algunos outputs de los programas.
* * *Demo* contiene una demo para el Festival Impaciencia.

## Descripción del repositorio

Los modelos de crecimiento ha venido siendo estudiados desde el siglo XVIII. Estos modelos han sido de gran utilidad en Biología como el modelo de Malthus o el modelo logstico. Malthus propuso un modelo en el cual la población podía crecer sin límites de un modo exponencial, lo cual se puede alejar mucho de la realidad ya que las poblaciones suelen vivir en ambientes limitados. Esto fue corregido en parte con el modelo logstico ya que asume que el medio tiene una carga así, aunque nuestra población pueda crecer de manera exponencial al principio, este crecimiento no será ilimitado. Como estos modelosmuchos otros han surgido como el de Gompertz.

Nuestro objetivo será modelar el crecimiento y difusión bidimensional de bacterias, por ello hemos decidido basarnos en un crecimiento logístico con un componente uniforme y de difución aleatorio. Este modelo responde a la llamada ecuación FKPP.

### La ecuación
![Primera ecuación](https://latex.codecogs.com/gif.latex?u_%7Bt%7D%3DD%20u_%7Bxx%7D%20&plus;%20ru%281-u%29)

*Más información en la documentación.*

### EL método numérico

![Segunda ecuación](https://latex.codecogs.com/gif.latex?u%5E%7Bi%7D_%7Bj&plus;1%7D%3Du%5E%7Bi%7D_%7Bj%7D&plus;%5Cfrac%7BkD%7D%7Bh%5E%7B2%7D%7D%20u%5E%7Bi&plus;1%7D_%7Bj%7D%20&plus;%20%5Cfrac%7Bk%7D%7Bh%5E%7B2%7D%7D%28rh%5E%7B2%7D-rh%5E%7B2%7Du%5E%7Bi%7D_%7Bj%7D-2D%29%20u%5E%7Bi%7D_%7Bj%7D%20&plus;%20%5Cfrac%7BkD%7D%7Bh%5E%7B2%7D%7Du%5E%7Bi-1%7D_%7Bj%7D)
<br><br>
**i** es la variable espacial y **j** la variable temporal.

*Más información en la documentación.*

### El código

Para esta parte hemos escrito el código de todos los algoritmos y funciones en Python. La mayoría de ellos se pueden ejecutar en tu IDE favorito siempre que sea capaz de guardar definiciones de variables. La mayoría de los cdigos comienza con ``fkppdosdimensines.py`` el cual ejecuta el algoritmo y muestra los resultados. Entonces varias funciones se pueden ejecutar si les puedes proporcionas la matriz que representa el estado y el momento en el que estás interesado. Por esta razón, si ejecutas el primer archivo en Spyder3, esta IDE guarda el valor de la matriz y entonces puedes ejecutar diferentes funcionesque ofrecen diferentes datos.

Finalmente los archivos llamados como ``_web.py`` están pensados para ser ejecutados en el backend de nuestra base de datos.

### Ejemplos

- ``fkppdosdimensiones.py`` (first executed)

Execute the main algorithm and offer a 3D view of it

![3d output](https://github.com/TheOpenBacteriaProject/FKPP/blob/master/images/3dvision.png)

- ``fkpplineascontorno.py`` (matrix needed, take the one that it is saved)

Offers a description of our matrix seen from above. A classical look. It also create countour lines to visualize the heigth
.

![countour lines](https://github.com/TheOpenBacteriaProject/FKPP/blob/master/images/contorno.png)

- ``cortetransversal.py`` (matrix needed, take the one that it is saved)

Search for a relevant transversal cut and show it (both from X and Y axes)

![t. cut](https://github.com/TheOpenBacteriaProject/FKPP/blob/master/images/corte.png)

- ``funciones_aux.py`` (matrix needed, take the one that it is saved)

Show the percentage of surface cover by bacteria.

  ``Cantidad de placa de petri con bacterias: 8.625265392781316%``
  
  ``Cantidad de superfice experimental con bacterias: 6.24%``
