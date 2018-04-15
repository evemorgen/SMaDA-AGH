global ta ta_p as aa aa_p S c sigma
ta = 0.53;       
ta_p = 0.06;
as = 0.19;
aa = 0.30;
aa_p = 0.31;
oldS  = 1366;           % W/m^2
c  = 2.7;               % Wm-2K-1
sigma = 5.67 * (10^-8); % W/m^2K^4
Ts = 273;               % start with 0 deg. of Celsius
Ta = 273;               % surface and atmosphere
s_vector = round(0.8 * oldS):round(1.2*oldS);
temp_e_vector = [];
temp_a_vector = [];
for i = s_vector
    S = i;
    Xp = [Ts Ta];
    X = fsolve(@heatfun, Xp);
    temp_e_vector = [temp_e_vector X(1) - 273.15];
    temp_a_vector = [temp_a_vector X(2) - 273.15];
    if X(1) - 273.15 < -5
        as = 0.8;
    else
        as = 0.19;
    end
end

%%
figure;
plot(s_vector, temp_e_vector);
title('Relationship between solar constant and mean earth temp result');
xlabel('Solar constant [W/m^2]');
ylabel('Mean Earth temp [deg. of C]');

figure;
plot(s_vector, temp_a_vector);
title('Relationship between solar constant and mean atmoshpere temp result');
xlabel('Solar constant [W/m^2]');
ylabel('Mean Atm temp [deg. of C]');

function F = heatfun(x)
    global ta as aa S c sigma ta_p aa_p
    F = [ -1 * ta * (1 - as) * (S/4) + ...
            c * (x(1) - x(2)) + ...
            sigma * (x(1) ^ 4) * (1 - aa_p) ...
            - sigma * (x(2) ^ 4);
          -1 * (1 - aa - ta + as*ta) * S / 4 ...
            - c * (x(1) - x(2)) ...
            - sigma * (x(1) ^ 4) * (1 - ta_p - aa_p) ...
            + 2 * sigma * x(2)^4;
        ];
end