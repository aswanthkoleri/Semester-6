% A state can be of the form [HL,BML,ML,S,HR,BMR,MR]
%% HR -> Humans on right side
%% HL -> Humans on left side
%% BML -> Big monkey on left side
%% BMR -> Big monkey on right side
%% ML -> Monkey on left side
%% MR -> Monkey on right side
%% S -> The side on which boat is situated 

%% To check state is valid
possible(HL,BML,ML,HR,BMR,MR) :-
	HL>=0, BML>=0, ML>=0,
	HL=<3, BML=<1, ML=<2,
	HR>=0, BMR>=0, MR>=0,
	HR=<3, BMR=<1, MR=<2,
	MonkeysOnLeft is ML+BML,
	MonkeysOnRight is MR+BMR,
	HumansOnRight is HR,
	HumansOnLeft is HL,
	(HumansOnLeft>=MonkeysOnLeft ; HumansOnLeft==0),
	(HumansOnRight>=MonkeysOnRight ; HumansOnRight==0).

% Possible rows:
%% From left to right
%% -------------------------------------------------------------
%% 1. Two humans cross left to right 
%% 2. One big monkey and one monkey cross left to right
%% 3. One Human and One monkey cross left to right 
%% 4. One Human and One big monkey left to right
%% 5. One human cross left to right 
%% 6. One Big monkey cross left to right 

%% 
%% From right to left 
%% --------------------------------------------------------------
%% 1. Two humans cross right to left 
%% 2. One big monkey and one monkey cross right to left
%% 3. One Human and One monkey cross right to left 
%% 4. One Human and One big monkey right to left
%% 5. One human cross right to left 
%% 6. One Big monkey cross right to left 


row([HL,BML,ML,left,HR,BMR,MR],[HL1,BML,ML,right,HR1,BMR,MR]):-
	%% 1. Two humans cross left to right 
	HR1 is HR+2,
	HL1 is HL-2,
	possible(HL1,BML,ML,HR1,BMR,MR).

row([HL,BML,ML,left,HR,BMR,MR],[HL,BML1,ML1,right,HR,BMR1,MR1]):-
	%% 2. One big monkey and one monkey cross left to right
	BML1 is BML-1,
	ML1 is ML-1,
	BMR1 is BMR+1,
	MR1 is MR+1,
	possible(HL,BML1,ML1,HR,BMR1,MR1).

row([HL,BML,ML,left,HR,BMR,MR],[HL1,BML,ML1,right,HR1,BMR,MR1]):-
	%% 3. One Human and One monkey cross left to right  
	HL1 is HL-1,
	ML1 is ML-1,
	HR1 is HR+1,
	MR1 is MR+1,
	possible(HL1,BML,ML1,HR1,BMR,MR1).

row([HL,BML,ML,left,HR,BMR,MR],[HL1,BML1,ML,right,HR1,BMR1,MR]):-
	%% 4. One Human and One big monkey cross left to right
	HL1 is HL-1,
	BML1 is BML-1,
	HR1 is HR+1,
	BMR1 is BMR+1,
	possible(HL1,BML1,ML,HR1,BMR1,MR).

row([HL,BML,ML,left,HR,BMR,MR],[HL1,BML,ML,right,HR1,BMR,MR]):-
	%% 5. One Human cross left to right
	HL1 is HL-1,
	HR1 is HR+1,
	possible(HL1,BML,ML,HR1,BMR,MR).

row([HL,BML,ML,left,HR,BMR,MR],[HL,BML1,ML,right,HR,BMR1,MR]):-
	%% 6. One Big monkey cross left to right 
	BML1 is BML-1,
	BMR1 is BMR+1,
	possible(HL,BML1,ML,HR,BMR1,MR).

row([HL,BML,ML,right,HR,BMR,MR],[HL,BML1,ML,left,HR,BMR1,MR]):-
	%% 6. One Big monkey cross right to left 
	BML1 is BML-1,
	BMR1 is BMR+1,
	possible(HL,BML1,ML,HR,BMR1,MR).

row([HL,BML,ML,right,HR,BMR,MR],[HL1,BML,ML,left,HR1,BMR,MR]):-
	%% 1. Two humans cross right to left 
	HR1 is HR-2,
	HL1 is HL+2,
	possible(HL1,BML,ML,HR1,BMR,MR).

row([HL,BML,ML,right,HR,BMR,MR],[HL,BML1,ML1,left,HR,BMR1,MR1]):-
	%% 2. One big monkey and one monkey cross right to left
	BML1 is BML+1,
	ML1 is ML+1,
	BMR1 is BMR-1,
	MR1 is MR-1,
	possible(HL,BML1,ML1,HR,BMR1,MR1).

row([HL,BML,ML,right,HR,BMR,MR],[HL1,BML,ML1,left,HR1,BMR,MR1]):-
	%% 3. One Human and One monkey cross right to left  
	HL1 is HL+1,
	ML1 is ML+1,
	HR1 is HR-1,
	MR1 is MR-1,
	possible(HL1,BML,ML1,HR1,BMR,MR1).

row([HL,BML,ML,right,HR,BMR,MR],[HL1,BML1,ML,left,HR1,BMR1,MR]):-
	%% 4. One Human and One big monkey cross right to left
	HL1 is HL+1,
	BML1 is BML+1,
	HR1 is HR-1,
	BMR1 is BMR-1,
	possible(HL1,BML1,ML,HR1,BMR1,MR).

row([HL,BML,ML,right,HR,BMR,MR],[HL1,BML,ML,left,HR1,BMR,MR]):-
	%% 5. One Human cross right to left
	HL1 is HL+1,
	HR1 is HR-1,
	possible(HL1,BML,ML,HR1,BMR,MR).

row([HL,BML,ML,right,HR,BMR,MR],[HL,BML1,ML,left,HR,BMR1,MR]):-
	%% 6. One Big monkey cross right to left 
	BML1 is BML+1,
	BMR1 is BMR-1,
	possible(HL,BML1,ML,HR,BMR1,MR).

% Solving function
solve([HL1,BML1,ML1,S1,HR1,BMR1,MR1],[HL2,BML2,ML2,S2,HR2,BMR2,MR2],Visited,History) :- 
   row([HL1,BML1,ML1,S1,HR1,BMR1,MR1],[HL3,BML3,ML3,S3,HR3,BMR3,MR3]), 
   not(member([HL3,BML3,ML3,S3,HR3,BMR3,MR3],Visited)),
   solve([HL3,BML3,ML3,S3,HR3,BMR3,MR3],[HL2,BML2,ML2,S2,HR2,BMR2,MR2],[[HL3,BML3,ML3,S3,HR3,BMR3,MR3]|Visited],[ [[HL3,BML3,ML3,S3,HR3,BMR3,MR3],[HL1,BML1,ML1,S1,HR1,BMR1,MR1]] | History ]).

%% If goal is found then print
solve([HL,BML,ML,S,HR,BMR,MR],[HL,BML,ML,S,HR,BMR,MR],_,History):- 
	format('             Side1                 ----------------------------           Side2                       '),nl,
	printResult(History).

% Print
printResult([]) :- format('~n'). 
printResult([[[HL1,BML1,ML1,S1,HR1,BMR1,MR1],[HL,BML,ML,S,HR,BMR,MR]]|History]) :- 
	printResult(History), 
   	 format(' ~w Humans, ~w Big Monkey ,~w Monkeys ----------river------------- ~w Humans, ~w Big Monkey ,~w Monkeys ',[HL,BML,ML,HR,BMR,MR]),nl,
   	 format(' ~w Humans, ~w Big Monkey ,~w Monkeys ----------river------------- ~w Humans, ~w Big Monkey ,~w Monkeys ',[HL1,BML1,ML1,HR1,BMR1,MR1]),nl.
%% Input 
find :- 
solve([3,1,2,left,0,0,0],[0,0,0,right,3,1,2],[[3,1,2,left,0,0,0]],_).