int: menu_length = 6;
int: money_limit = 1505;

array[1..menu_length] of int: menu_prices = [215, 275, 335, 355, 420, 580];
array[1..menu_length] of string: menu_names = ["fruit", "fries", "salad", "wings", "sticks", "sampler"];

array[1..menu_length] of var int: order;

constraint forall([order[i] >= 0 | i in 1..menu_length]);
constraint sum([order[i] * menu_prices[i] | i in 1..menu_length]) == money_limit;

solve satisfy;

output [menu_names[i] ++ ": " ++ show(order[i]) ++ "\n" | i in 1..menu_length];