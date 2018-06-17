A = 0.30;                       % albedo
S = 1366;                       % W/m^2
sigma = 5.67 * (10^-8);         % W/m^2K^4
T4 = S * (1 - A) / (sigma * 4); % K^4
T = T4 ^ (1/4);                 % K
output = ['Mean earth temperature without atmosphere in:', newline, ...
          '  Kelvins: ', num2str(T), ' K' newline, ...
          '  Celsius: ', num2str(T - 273.15), ' deg of C' newline
          ];
disp(output);
