% plane variables
outer_size    = 25;              % cm
inner_size    = 5;               % cm
thickness     = 0.2;             % cm
outer_temp    = 20;              % C
inner_temp    = 20;              % C
heating_power = 10000000;             % W
 
% time variables
number_of_steps = 10000;           % num
dt = 0.1;                        % s
t  = 10;                         % s
dx = 0.01;                       % m
dy = 0.01;                       % m

% metal variables
K = 237;                         % W/mK
cw = 900;                        % J/kgK
ro = 2700;                       % kg/m3

small_start = (outer_size - inner_size)/2;

plane(1:outer_size,1:outer_size,1) = outer_temp;
plane(small_start:small_start+inner_size,small_start:small_start+inner_size, 1) = inner_temp;

% time loop
for i = 2:number_of_steps
    % loop over dimentions
    for x = 2:outer_size-1
        for y = 2:outer_size-1
            
            % for first 10s transfer heat where the heater is
            if i * dt < t && ...
               x >= small_start && ...
               x <= small_start + inner_size && ...
               y >= small_start && ...
               y <= small_start + inner_size
                plane(x,y,i) = plane(x, y, i-1) + ...
                                    (heating_power * dt) / ...
                                    (cw * inner_size * inner_size * thickness * ro);
            else
                plane(x,y,i) = ...
                    plane(x,y,i-1) + ...
                    (K*dt)*(plane(x+1,y,i-1) - 2*plane(x,y,i-1) + plane(x-1,y,i-1))/(cw*ro*dx*dx) + ...
                    (K*dt)*(plane(x,y+1,i-1) - 2*plane(x,y,i-1) + plane(x,y-1,i-1))/(cw*ro*dy*dy);
            end
        end
    end
    [XX, YY] = meshgrid(1:outer_size,1:outer_size);
    surf(XX,YY,plane(:,:,i));
    title(strcat('Simulation after ', num2str(i*dt), 's'));
    zlim([20, 30]);
    drawnow;
    pause(0.1);
end

% analyze delta T of the model and diff between 
