# FKPP on multiples dimensions

![](https://raw.githubusercontent.com/TheOpenBacteriaProject/Branding/master/Documentation-Media/Document-Header.png)

## Folders

* *Documentation* contains all the mathematical documentation.
* *Python* contains our programs.
* *images* contains all output pics from our programs.

## Repository description

Since the 18th century, population growth models have been studied. These
models have great utility in biology such as the Malthus model
or the logistic model. Malthus proposed a model in which the population
could grow without limits at an exponential rate, which can get away from the
reality if our population lives in a limited environment. This was corrected with the
logistic model, since it assumes that the medium has a load (it can support a
maximum number of beings) so although growth can acquire a speed
exponential at the beginning, this growth will not be unlimited. Like these models
Many others have emerged, such as Gompertz's one.
Our objective will be to model the growth and diffusion in 2 dimensions
of bacteria, for this we have decided to use a logistic growth with a
uniform and random diffusion component. This model responds to the call
FKPP equation.
### The equation
![first equation](https://latex.codecogs.com/gif.latex?u_%7Bt%7D%3DD%20u_%7Bxx%7D%20&plus;%20ru%281-u%29)

*More information about this equation can be found at the documentation file.*

### The numerical method (Method of lines with explicit euler)
![first equation](https://latex.codecogs.com/gif.latex?u%5E%7Bi%7D_%7Bj&plus;1%7D%3Du%5E%7Bi%7D_%7Bj%7D&plus;%5Cfrac%7BkD%7D%7Bh%5E%7B2%7D%7D%20u%5E%7Bi&plus;1%7D_%7Bj%7D%20&plus;%20%5Cfrac%7Bk%7D%7Bh%5E%7B2%7D%7D%28rh%5E%7B2%7D-rh%5E%7B2%7Du%5E%7Bi%7D_%7Bj%7D-2D%29%20u%5E%7Bi%7D_%7Bj%7D%20&plus;%20%5Cfrac%7BkD%7D%7Bh%5E%7B2%7D%7Du%5E%7Bi-1%7D_%7Bj%7D)
<br><br>
**i** is the spatial variable and **j** the time variable.

*More information about this numerical method can be found at the documentation file.*

### The codes
For this part we have code all the algorithms and function in python. The majority of them can be executed in your favorite IDE at least if it is capable of save variable definitions. Most of the code begins with ``fkppdosdimensiones.py`` which do the algorithm and plot the results. Them multiple functions can be executed if you can give them the matrix that represents the state in the moment you are interested in. For this reason, if you execute the first file in Spyder3, this IDE save the matrix value and then you can execute different functions that offer different data.
Finally the files named with ``_web.py`` at the end, are formated exclusively to be executed at the backend of our database.
### Example of diferent outputs:
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
