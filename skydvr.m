% parachutist problem
% when upward drag force balances the downward weight component
% parachutist will be at terminal velocity and acceleration = 0.
% input the acceleration of gravity
% g is the acceleration of gravity and rho is the air density
g = 9.806;
rho = 1.225;
figure(1)
hold on
% enter lag time from jump to parachute opening (seconds)
opentime = 5.0;
% input mass of skydiver & pack (kg) 

m = 70;
% drag coefficient
% try no drag first
% lump all constants 
% k =1/2*air density * area*cd
cd = 1.75;
%
% input projected area
area = 3.25;
ki = 0.5*rho*area*cd;
k = ki;
% start clock for initial time at 0.00 seconds
ti = 0.0;
% try simulating for 10 seconds, we might have to raise this
% final time = 10.0 seconds
tf = 10;
% for first run use initial velocity = 0
% then try setting an initial velocity to represent
% parachutist jumping off a building or cliff prior
% to opening chute
vi = 10.0;
% time increment for computation intervals
% the smaller the computation interval the more accurate the output
% will be .05 secs
dt = 0.01;
% start the clock at t = initial time
t = ti;
% v = initial velocity at start (obviously)
v = vi;
delt = dt;
% let s start a computation loop for time = 0 to 10 seconds with computations at 0.05 s intervals
while(1)
    if t + dt > tf
delt = tf - t
    end
% next line is the ordinary differential equation presented in class
% just calling dv/dt = vprime
 vprime = g - (k./m)*v^2;
    v = v + vprime*delt
% just progressing along the timeline by delta t which is our step size
    t = t + delt;
    drawnow;
    plot(t,v)
    if t >=tf,break

    endif
    if t > opentime
      k = ki * 10
    endif
end
disp('velocity (m/s): ')
disp(v)
figure (1)
hold on
xlabel('time (seconds)'); ylabel('v (m/s)');
% run this script from the command window if you have to put in a value for the mass
hold off
pause();