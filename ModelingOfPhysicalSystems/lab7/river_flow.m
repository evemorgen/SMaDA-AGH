% another river flow 
format bank;
rain = importdata('opady.prn');
dunaj_river = importdata('dunaj.prn');

figure;
semilogy(rain(:,2));
hold on;
semilogy(dunaj_river(:,2));
xasm();
xlabel('t [months]');
ylabel('Tracer concentration [TU]');
legend('rain data','river measures');
title('Tracer concentration in Danube river');

lambda = 4.696e-3;          % 1/month?
dt = rain(2,1) - rain(1,1); % month

mean_residence = [];
old_rmse = 0;
for tt = 1:1000
    num = rain(end, 1);
    output1 = zeros(num,1);      % vector with output values

    for i= 1:num
        output1(i) = easy_integral(rain(:,2), i, dt, tt, lambda);
    end 

    errors = (dunaj_river(161:num,2) - output1(161:num));
    errors = errors.^2;
    %root mean square error
    rmse = sqrt(sum(errors)/(num-161));
    if tt == 1
        old_rmse = rmse;
    else
        if rmse > old_rmse
            disp(tt);
            break;
        else
            old_rmse = rmse;
        end
    end
    mean_residence(tt,1) = tt;
    mean_residence(tt,2) = rmse;
end

figure;
subplot(2,1,1);
semilogy(dunaj_river(:,2));
hold on;
semilogy(output1);
xasm();
xlabel('t [months]');
ylabel('Tracer concentration [TU]');
legend('river measures', 'model estimation');
title('Tracer concentration in Danube river with tt=411');

subplot(2,1,2);
plot(output1 - dunaj_river(:,2));
xasm();
xlabel('t [months]');
ylabel('output - measured');
title('diferrence between measured value and estimated value');


figure;
%semilogy(dunaj_river(:,2));
subplot(2,1,1);
plot(diff(dunaj_river(:,2)));
xasm();
subplot(2,1,2);
plot(diff(output));
xasm();
%semilogy(rain(:,2));
%hold on;
%semilogy(output);
%legend('measured amount of tritium','model estimation');
xlabel('t [days]');
ylabel('Tritium concentration [TU]');

figure;
plot(mean_residence(:,2));
xlabel('tt [months]');
ylabel('RMSE value');
title('Relationship between RMSE and tt value');



%{
figure;
plot(abs(output - dunaj_river(:,2)));

disp(sum(abs(output - dunaj_river(:,2))));


figure;
plot((output - dunaj_river(:,2)));

figure;
semilogy(rain(:,2));
hold on;
semilogy(dunaj_river(:,2));
%}

[val, idx] = min(mean_residence);
disp(val);
disp(idx);


figure;
semilogy(dunaj_river(:,2));
hold on;
semilogy(output1);
hold on;
semilogy(output2);
xasm();
xlabel('t [months]');
ylabel('Tracer concentration [TU]');
legend('river measures', 'model estimation with tt = 217', 'model estimation with tt = 8');
title('Tracer concentration in Danube river with various tt');



