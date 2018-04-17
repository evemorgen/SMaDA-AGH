% TAYLOR - QUICKEST METHOD

len     = 100;    % m
wid     = 5;      % m
dep     = 1;      % m

t       = 1000;   % s
dt      = 1;    % s
dx      = 1;    % m
nt      = t/dt;   % num
U       = 0.1;    % m/s  [advection coefficient ]
D       = 0.01;   % m2/s [dispersion coefficient] 
inject  = 10;     % m
measure = 90;     % m
tracer  = 1;      % kg

Ca = U * dt / dx;
Cd = D * dt / dx^2;
c = [];

% initial condition
for j = 1:(len/dx)
    if j*dx == inject
        c(1,j) = tracer;
    else
        c(1, j) = 0;
    end
end

% calculate real time
for i = 1:(t/dt)
    for j = 3:(len/dx)-1
        c(i+1, j) = c(i, j) + ...
            (Cd*(1-Ca) - (Ca/6)*(Ca^2 - 3*Ca + 2))*c(i,j+1) - ...
            (Cd*(2 - 3*Ca) - (Ca/2)*(Ca^2 - 2*Ca - 1))*c(i,j) + ...
            (Cd*(1 - 3*Ca) - (Ca/2)*(Ca^2 - Ca - 2))*c(i,j-1) + ...
            (Cd*Ca + (Ca/6)*(Ca^2 - 1))*c(i,j-2);
    end
    plot(c(i,:));
    drawnow;
    pause(0.1);
end
