include "at_most.mzn";
include "lex_less.mzn";

predicate knapsack(array[int] of var int: Weights, array[int] of var 0..1: Taken, int: Capacity) =
           sum(i in index_set(Weights))( Weights[i] * Taken[i]) <= Capacity
;

int: items_n;
int: knapsacks_n; 
int: capacity;

array[1..items_n] of int: values;
array[1..items_n] of int: weights;
array[1..knapsacks_n, 1..items_n] of var 0..1: taken;

constraint forall(i in 1..items_n)(
 at_most(1, [taken[j,i] | j in 1..knapsacks_n],1)
);

constraint forall(i in 1..knapsacks_n)(
 knapsack(weights, [taken[i,j] | j in 1..items_n], capacity)
);

constraint forall(i in 1..knapsacks_n - 1)(lex_less(row(taken, i), row(taken, i+1)));

solve maximize sum(i in 1..knapsacks_n, j in 1..items_n) (taken[i,j] * values[j]);

output [if j == 1 then show(i) ++ ") " else "" endif ++ show(taken[i,j]) ++ if j = items_n then "\n" else "" endif  | i in 1..knapsacks_n, j in 1..items_n] 