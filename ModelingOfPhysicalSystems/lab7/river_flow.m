% another river flow 


global t;
lambda = 1;

Cin = @(t) opady(t,2);

% exponential model
g = @(t, tt) tt^-1 * exp(-t/tt);


C = @(t) Cin()
