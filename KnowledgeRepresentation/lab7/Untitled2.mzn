% constants
int: menu_len;
int: money_limit;
array[1..menu_len] of int: menu_prices;
array[1..menu_len] of string: menu_elements;
array[1..menu_len] of int: yum_yum_factor;

% variables
array[1..menu_len] of var int: order;
 
% constraints
constraint forall([order[i] >= 0 | i in 1..menu_len]);
constraint sum([order[i] * menu_prices[i] | i in 1..menu_len]) <= money_limit;

% solve
solve maximize sum([order[i] * yum_yum_factor[i] | i in 1..menu_len]);

% print output
output [ menu_elements[i] ++ ": " ++ show(order[i]) ++ "\n" | i in 1..menu_len ]