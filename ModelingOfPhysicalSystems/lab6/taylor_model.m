% TAYLOR - QUICKEST METHOD

% define parameters
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
        c(1,j) = tracer/(dx*dep*wid);
    else
        c(1, j) = 0;
    end
end
sums = [];
% calculate in real time
for i = 1:nt
    for j = 3:(len/dx)-1
        c(i+1, j) = c(i, j) + ...
            (Cd*(1-Ca) - (Ca/6)*(Ca^2 - 3*Ca + 2))*c(i,j+1) - ...
            (Cd*(2 - 3*Ca) - (Ca/2)*(Ca^2 - 2*Ca - 1))*c(i,j) + ...
            (Cd*(1 - 3*Ca) - (Ca/2)*(Ca^2 - Ca - 2))*c(i,j-1) + ...
            (Cd*Ca + (Ca/6)*(Ca^2 - 1))*c(i,j-2);
    end
    
    % plot results
    %subplot(2,1,1);
    %plot(1:(len/dx), c(i,:));
    sums(i) = sum(c(i,:));
    %xlabel('t');
    %ylabel('c(t)');
    %subplot(2,1,2);
    %plot(c(:,measure/dx));
    %xlabel('x');
    %ylabel('c(x)');
    drawnow;
    pause(0.1);
end
