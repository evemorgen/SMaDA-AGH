%%%%%%%%%%%%%%%%%%
%% BLOCKS WORLD %%
%%%%%%%%%%%%%%%%%%

% ACTION DESCRIPTION SCHEMA
% strips_rule(action(args), preconds, add-list, delete-list)

% ACTION I 
strips_rule(stack(X,Y), % name and arguments
	[holding(X)], % list of conditions
	[on(X,Y), clear(X), handempty], % list of added facts
	[clear(Y), holding(X)]). % list of removed

%TODO: ACTION II 
strips_rule(take_off(X,Y),           % name and arguments
	[on(X,Y),handempty], % list of conditions
	[holding(X), clear(Y)],          % list of added facts
	[clear(X),handempty,on(X,Y)]). % list of removed

%%TODO: ACTION III
strips_rule(put_on_table(X),      % name and arguments
    [holding(X)],                   % list of conditions
    [ontable(X), handempty, clear(X)], % list of added facts
    [holding(X)]).                  % list of removed

%TODO: ACTION IV
strips_rule(take_off_table(X), % name and arguments
	[ontable(X),handempty], % list of conditions
	[holding(X)], % list of added facts
	[ontable(X),clear(X),handempty]). % list of removed

%%%%%%%%%%%%%%%%%%%%%%%
%% EXAMPLES OF USAGE %%
%%%%%%%%%%%%%%%%%%%%%%%

%% EXAMPLE I
problem1 :-
  plan(
  [ontable(a),ontable(b),ontable(c),clear(a),clear(b),clear(c),handempty],
  [on(b,c), on(a,b)]).

%% EXAMPLE II
problem2 :-
  plan(
  [on(a,c),ontable(b),ontable(c),clear(a),clear(b),handempty],
  [on(b,c), on(a,b)]).

%% EXAMPLE III
problem3 :-
  plan(
    [on(c,a),ontable(a),ontable(b),clear(b),clear(c),handempty],
    [on(b,c), on(a,b)]).

%TODO: EXAMPLE IV
problem4 :- 
    plan(
    [on(a,b),on(b,c),ontable(c),clear(a),handempty]    ,
    [on(c,b), on(b,a)]
    ).

%%%%%%%%%%%%%%%%%%%%
%% STRIPS PLANNER %%
%%%%%%%%%%%%%%%%%%%%

% Strips as a regression planner.
% Top-level interface.
strips(InitState, GoalList, Plan) :-
	strips1(InitState, GoalList, [], [], _, RevPlan),
	reverse(RevPlan, Plan).

% Base case: All goals satisfied in State.
strips1(State, GoalList, Plan, _, State, Plan) :-
 subset(GoalList, State).

% Plan
strips1(State, GoalList, Plan, BadActions, NewState, NewPlan) :-
	member(Goal, GoalList),
	not(member(Goal, State)),    % Find unsatisfied goal.
	write('\nAttempting goal:  '),write(Goal),nl,
	adds(Ac, Goal),              % Find action that achieves it.
	write(' Choosing Action:  '),write(Ac),
	not(member(Ac, BadActions)), % Do not repeat actions (dangerous).
	write(' -- not a bad action.'),nl,
	preclist(Ac, PrecList),      % Find preconds and achieve them.       
	strips1(State, PrecList, Plan, [Ac|BadActions], TmpState1, TmpPlan1),
	apply_rule(Ac, TmpState1, TmpState2),  % Recurse w/new state and goals.
	strips1(TmpState2,GoalList,[Ac|TmpPlan1],BadActions,NewState,NewPlan).
	
% Apply Rule
apply_rule(Ac, State, NewState) :-
	write('\nSimulating '),write(Ac),nl,
	write('From: '), write(State), write('\n----> '),
	dellist(Ac, DelList),                     % find deleted props
	subtract(State, DelList, TmpState),       % remove deleted props
	addlist(Ac, AddList),                     % find added props
	union(AddList, TmpState, NewState),       % add props to old state
	write(NewState).
   
% Utilities
preclist(Action, Plist) :- strips_rule(Action, Plist, _, _).
prec(Action, Cond) :- preclist(Action, Plist), member(Cond, Plist).
addlist(Action, Alist) :- strips_rule(Action, _, Alist, _).
adds(Action, Cond) :- addlist(Action, Alist), member(Cond, Alist).
dellist(Action, Dlist) :- strips_rule(Action, _, _, Dlist).
dels(Action, Cond) :- dellist(Action, Dlist), member(Cond, Dlist).

% Pretty-print Init, Goal, and Plan.
plan(InitState, Goal) :-
	strips(InitState,Goal,Plan),
	write('\n\nInit: '), write(InitState),nl,
	write('Goal: '),write(Goal),nl,
	write('Plan:\n'),
        writeplan(Plan),nl.

% Pretty-print the plan.
writeplan([]).
writeplan([A|B]):-
  write('       '),write(A),nl,
  writeplan(B).
