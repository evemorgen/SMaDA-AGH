% plane variables
outer_size = 25;                 % cm
inner_size = 5;                  % cm
outer_temp = 10;                 % C
inner_temp = 80;                 % C

% time variables
number_of_steps = 100;           % num
dt = 0.1;                        % s
dx = 0.01;                       % m
dy = 0.01;                       % m

% metal variables
K = 237;                         % W/mK
cw = 900;                        % J/kgK
ro = 2700;                       % kg/m3


small_start = (outer_size - inner_size)/2;

plane(1:outer_size,1:outer_size,1) = outer_temp;
plane(small_start:small_start+inner_size,small_start:small_start+inner_size, 1) = inner_temp;

for i = 2:number_of_steps
    for x = 2:outer_size-1
        for y = 2:outer_size-1
            plane(x,y,i) = ...
                plane(x,y,i-1) + ...
                (K*dt)*(plane(x+1,y,i-1) - 2*plane(x,y,i-1) + plane(x-1,y,i-1))/(cw*ro*dx*dx) + ...
                (K*dt)*(plane(x,y+1,i-1) - 2*plane(x,y,i-1) + plane(x,y-1,i-1))/(cw*ro*dy*dy);
        end
    end
    plane(small_start:small_start+inner_size,small_start:small_start+inner_size, i) = inner_temp;
    plane(1,:,i) = outer_temp;
    plane(:,1,i) = outer_temp;
    plane(outer_size,:,i) = outer_temp;
    plane(:,outer_size,i) = outer_temp;

end

[XX, YY] = meshgrid(1:outer_size,1:outer_size);
surf(XX,YY,plane(:,:,number_of_steps));
