function [t,y]=eulerforFKPP(a,b,t0,tfin,u0,m)

% Inicializamos variables
k= (tfin-t0)/(m);          % k= delta t ********el papel de h en otros ejemplos
t=linspace(t0,tfin,m+1);     % note t(1)=t0 and t(m+1)=tfin;  ******** partición del intervalo con m+1 nodos
y=[u0];                    % initial condition ****** guardaremos en y las distintas aproximaciones
% f tiene que actuar sobre columnas (si trabajamos vectorialmente)
%
                  
h = (b-a)/(m+1);
D=1; %constante difusión
r=0.5; #Constante r
e = ones(m,1); %vector de unos
for i= 1:m
    A = spdiags([e*D -2*e*D+r*h^2-y(:,i)*r*h^2 e*D],[-1 0 1],m,m);	%Creamos la matriz A	
    A= A/h^2;
    %function ddot=lineas2(temp,d) %Función que se 
    %global A
    %ddot= A*d;
    %endfunction 
    %y=[y, y(:,i) + k*feval("lineas2",t(i),y(:,i))];
    y=[y, y(:,i) + k*A*y(:,i)];
end;
end