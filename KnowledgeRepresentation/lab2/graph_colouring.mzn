% load parameters
int: nodesNumber;
array[1..nodesNumber,1..nodesNumber] of bool: edges;

% declare variables
array[1..nodesNumber] of var 1..nodesNumber: colors;

% add some constraints
constraint forall(i,j in 1..nodesNumber where edges[i,j] /\ i < j)(colors[i] != colors[j]);
var int: colorsNumber = max(colors);

% solve the shit out of it
solve minimize colorsNumber;

% output results
output [show(colorsNumber), " colors\n",] ++
       [show(colors[i]) ++ " " | i in 1..nodesNumber]