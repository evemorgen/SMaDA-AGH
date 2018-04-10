A = 0.30;                     % albedo
S = 1366;                     % W/m2
%r = 6.3781 * 10^6;            % m
%Pow = 4 * pi * r * r;         % m2
ro = 5.67 * (10^-8);            % W/m2K4
%p_sun = S * Pow * (1 - A);
%p_ert = ro * T^4 * Pow;
T4 = S * (1 - A) / ro / 4;
T = nthroot(T4, 4);
disp(T);
