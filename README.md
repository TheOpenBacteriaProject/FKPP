# FKPP on 1 dimension
We want to simulate the FKPP.
## The equation
$$ u_{t}=D u_{xx} + ru(1-u) $$
## The numerical method (Method of lines with explicit euler)
$$ u^{i}_{j+1}=u^{i}_{j}+\frac{kD}{h^{2}} u^{i+1}_{j} + \frac{k}{h^{2}}(rh^{2}-rh^{2}u^{i}_{j}-2D) u^{i}_{j} + \frac{kD}{h^{2}}u^{i-1}_{j} $$

i is the spatial variable and j the time variable.
