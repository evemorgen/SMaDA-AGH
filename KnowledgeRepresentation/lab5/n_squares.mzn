% Parameters
%%%%%%%%%%%
int: n = 5;                              % How many squares do we have?
set of int: SQUARES = 1..n;               % Set of the available squares
int: min = n;                             % Minimal length is dimention of biggest square
int: max = sum(1..n);                     % Worst case scenario is when all sqares lay next to each other

% Variables
%%%%%%%%%%%
var min..max: height;                     % height of the container
var min..max: width;                      % width of the conainer
var (min*min)..(max*max): area = height * width;      % container's area
array[SQUARES] of var 0..max-1: x;      % squares' coordinates in the container
array[SQUARES] of var 0..max-1: y;      % squares' coordinated in the container
  
% Constraints 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

% Constraint 1: Squares should fit inside the container
constraint forall(i in SQUARES)(x[i] + i <= width /\ y[i] + i <= height /\ x[i] >= 0 /\ y[i] >= 0);

% Constraint 2: Squares should not overlap
constraint forall(i in SQUARES, j in SQUARES where i > j)(
  (
     (x[i] >= x[j] /\ x[i] + i >= x[j]) /\     % first starts inside other one - x axis
     (x[i] >= x[j] + j /\ x[i] >= x[j] + j)    % second starts inside first one - x axis
  ) 
  \/ 
  (
     (y[i] >= y[j] /\ y[i] + i >= y[j]) /\     % first starts inside other one - y axis
     (y[i] >= y[j] + j /\ y[i] >= y[j] + j)    % second starts inside first one - y axis
  ) 
);

% Goal
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
solve minimize area; 
  

% Boring output  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
output [ show(i) ++ " > (" ++ show(x[i]) ++ "," ++ show(y[i]) ++ ")\n" | i in 1..n] ++
  ["area = " ++ show(width) ++ " * " ++ show(height) ++ " = " ++ show(area)]