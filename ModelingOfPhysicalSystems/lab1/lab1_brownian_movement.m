% lab1 Physics simulation
% brownian motion

% clear canvas
clear;
clf;

% set initial variables
N = 1000;
pos = zeros(1,2);
X(1) = 0;
Y(1) = 0;

% generate next points in a loop
for i=2:N
    X(i) = X(i-1) + randn();
    Y(i) = Y(i-1) + randn();
end

% plot the result
plot(X,Y);
xlabel('x coordinate');
ylabel('y coordinate');

%make next figure
figure;
corr(X, Y);
X2 = X'
Y2 = Y'

result_vector = [];
for i=-50:50
    stuff = corr(X2(100:N-100), X2(100+i:N-100+i));
    result_vector = [result_vector stuff];
end
plot(result_vector);

