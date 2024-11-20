% populate the code below with your input values
% the percent symbol is just for comments
% the semicolon (;) at the end of a line just indicates end of statement
% if you want to suppress and hide the MATLAB output for an expression
% just add a semicolon after the expression.
% make a run with no damping and a second run with a damping value
% search online for input values from pendulum experiments and/or solved problems
close all; clear, clc
m=    1    ; % pendulum bob mass (kg)
l=    1    ; % pendulum cord length (m)
g=    9.81 ; % acceleration of gravity
b=    0    ; % damping coefficient (N-s/m) or kg/s
tsim= 10   ; % simulation time (seconds)
disp= 10000    ; % initial condition (displacement angle in degrees)
% radians = degrees x (pi/180)
ic = disp*(pi/180);
% remember, with small angle approximation sin theta is theta
% make a run with a small angle and a large angle
f=@(t,x) [x(2); 1/m*(-b*x(2)-m*(g/l)*sin(x(1)))]
% the vector field for the differential equation will be generated using the following points
x1=linspace(-pi,pi,80);
x2=linspace(-pi,pi,80);
[X,Y]=meshgrid(x1,x2);
% size(obj,dim) returns the length of the dimension specified by the scalar dimension
% code continues
% for example, size(obj,1) returns the number of rows.
% additionally, d = size(X) returns the sizes of each dimension of array X in a vector d
% as long as ndims(X) elements was given, for example
% = ndims(X) returns the number of dimensions in the array X
u=zeros(size(X));
v=zeros(size(X));
% solving for t=0
t=0;
% the numel function below returns the number of elements in an array X,
% which is equivalent to prod(size(objArray)), namely, the product of the array
% dimensions; the size and numel functions work consistently with arrays of
% user-defined objects.
% so numel(X) is equivalent to prod(size(X))
% whereas length(X) is equivalent to max(size(X))
for i = 1:numel(X)
    Xsys = f(t,[X(i); Y(i)]); % evaluate function
% just taking the 3 variables from this earlier equation t, x(1) and x(2)
% at each time step
% f=@(t,x) [x(2); 1/m*(-b*x(2)-m*(g/l)*sin(x(1)))]
    u(i) = Xsys(1);
    v(i) = Xsys(2);
end
figure(1)
% plot the vector field
quiver(X,Y,u,v,'r');
grid on
xlabel('x_2 velocity'); ylabel('x_1 displacement')
title('Phase portrait')
% code continues
% trajectory of the system
hold on
% ODE45 is usually the function of choice among the ODE solvers; it compares methods
% of orders four and five to estimate error and determine step size.
% ODE45 is so accurate that its default behavior is to use its interpolant to provide results
%at intermediate points.
% invoke solver ode45(fun,time interval,initial condition)
[ts,ys] = ode45(f,[0,tsim],[0; ic]);    %Solution of the ODE
plot(ys(:,1),ys(:,2),'b','LineWidth',2)
w = ys(:,1);
th = ys(:,2);
plot(ys(1,1),ys(1,2),'go')                   %Starting point
plot(ys(end,1),ys(end,2),'k*')          %Ending point
plot(0,0,'yd')
%hold off
legend({'Vector field','Trajectory','Starting point','End point','Origin'})
axis([-0.5*pi 0.5*pi -0.5*pi 0.5*pi])
hold off
figure(2)
subplot(2,1,1);plot(ts,th);
xlabel('time (s)'); ylabel('angle (rad)');
title('simple damped pendulum');
subplot(2,1,2); plot(ts,w);
xlabel('time (s)'); ylabel('rate (rad/s)');
hold off
pause();