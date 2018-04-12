include "globals.mzn";

% maximal number of steps 
int: n_steps;
% set of the steps' indexes
set of int: steps = 1..n_steps;
% index of the last last step
var 1..n_steps : end; % last step (end) from int to something more constrained

% how many blocks do we have?
int: n_blocks;
% set of the blocks' indexes
set of int: blocks = 1..n_blocks;

% index 0 indentifies the table
int: Table = 0;

% set of all the elements we have
set of int: table_or_blocks = {Table} union blocks;

% initial blocks' locations
array [blocks] of table_or_blocks: initial_loc;

% final blocks' locations
array [blocks] of table_or_blocks: final_loc;

% table has as many columns as we have blocks
% the negative value means that block lies directly on the table
set of int: locs = -n_blocks..n_blocks;

% blocks' positions in various moments
array [steps, blocks] of var locs: on;

% we have to set up initial locations
constraint
    forall (b in blocks) (
        if initial_loc[b] = Table then
            on[1, b] = -b
        else
            on[1, b] = initial_loc[b]
        endif
    );

% we have to set up final locations
constraint
    forall (b in blocks) (
        if final_loc[b] = Table then
            on[end, b] = -b
        else
            on[end, b] = final_loc[b]
        endif
    );

% in every moment block lies on the other block
% or on the table
constraint
    forall (b in blocks, s in steps where s < end) (
        on[s, b] in {c | c in blocks where c != b} union {-b}
    );

% no two blocks can lie at the same place
constraint
    forall (s in steps)(alldifferent (b in blocks) (on[s, b]));

% clear location is a location which
% - is a designated place on the table table 
% - no block lies on it
predicate clear(steps: s, var locs: l) =
    l < 0  \/  forall (b in blocks) (on[s, b] != l);

% to move the block, start and end position have to be clear
constraint
    forall (s in steps, b in blocks where s < end ) (
        on[s, b] != on[s + 1, b]
    ->
        (   clear(s, b)
        /\  clear(s, on[s + 1, b])
        /\ s < end % transitions won't occur after the time stated in the end variable
        )
    );

solve   :: int_search(
            [on[s, b] | s in steps, b in blocks],
            first_fail,
            indomain_min, % smallest end possible 
            complete
        )
        minimize end;

output
    [   "[Negative locations denote the table.]\n"
    ] ++
    [   if b = 1 then
            "Step " ++ show(s) ++ ":\n"
        else
            ""
        endif ++
        "  block " ++ show(b) ++ " on " ++ show(on[s, b]) ++ "\n"
    |   s in 1..fix(end), b in 1..n_blocks % only relevant states
    ];