%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% dato inicial para la resolucion        

%Número de particiones del intervalo
m = 100; 
%Extremos del intervalo
a = 0; b = 1;  
alpha = 0; beta =0;
x=linspace(a,b,m+2);
xint=x(2:m+1);
u=sin(pi*xint)';
plot(xint,u)    
% Resolvemos mediante Euler explicito
[t,sol]=eulerforFKPP(a,b,0,1,u,m);
% Representamos la evolucion de la soluciones numerica y exacta
clf
hold off
for i=0:1:m
plot(x,[0;sol(:,i+1);0],pause(0.2));
endfor