figure;
rc = [];
random_values = rand(1, 1000);
for i = -50:50
    rc = [rc corr(random_values(100:900)', random_values(100+i:900+i)')];
end
plot(rc);
xlabel('random position');
ylabel('auto correlation value');
title('Auto correlation of random values');

x = [0];
for i=2:1000
   x = [x x(i-1)+randn()];
end

bc = []
for i = -50:50
    bc = [bc corr(x(100:900)', x(100+i:900+i)')];
end

figure;
plot(bc);
xlabel('random walk position');
ylabel('auto correlation value');
title('Auto correlation of Brownian motion');