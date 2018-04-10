global ta ta_p as aa aa_p S c ro
ta = 0.53;
ta_p = 0.06;
as = 0.19;
aa = 0.30;
aa_p = 0.31;
S  = 1366;
c  = 2.7;    % Wm-2K-1
ro = 5.67 * (10^-8);
Ts = 273;
Ta = 273;
Xp = [Ts Ta];
for i = 1000:1400
    S = i;
    X = fsolve(@heatfun, Xp);
    plot(X);
end
X = X - [273 273];

function F = heatfun(x)
    global ta as aa S c ro ta_p aa_p
    F = [ -1 * ta * (1 - as) * (S/4) + ...
            c * (x(1) - x(2)) + ...
            ro * (x(1) ^ 4) * (1 - aa_p) ...
            - ro * (x(2) ^ 4);
          -1 * (1 - aa - ta + as*ta) * S / 4 ...
            - c * (x(1) - x(2)) ...
            - ro * (x(1) ^ 4) * (1 - ta_p - aa_p) ...
            + 2 * ro * x(2)^4;
        ];
end