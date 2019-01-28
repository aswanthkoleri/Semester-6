:- use_module(library(clpfd)).



isAlpha('A',B):- 
	B is 1.
isAlpha('B',B):- 
	B is 2.
isAlpha('C',B):- 
	B is 3.
isAlpha('D',B):- 
	B is 4.
isAlpha('E',B):- 
	B is 5.
isAlpha('F',B):- 
	B is 6.
isAlpha('G',B):- 
	B is 7.
isAlpha('H',B):- 
	B is 8.
isAlpha('I',B):- 
	B is 9.
isAlpha('X',_).

isNumber(1,'A').
isNumber(2,'B').
isNumber(3,'C').
isNumber(4,'D').
isNumber(5,'E').
isNumber(6,'F').
isNumber(7,'G').
isNumber(8,'H').
isNumber(9,'I').
 
		
sudoku([[VA1,VB1,VC1,VD1,VE1,VF1,VG1,VH1,VI1],
        [VA2,VB2,VC2,VD2,VE2,VF2,VG2,VH2,VI2],
        [VA3,VB3,VC3,VD3,VE3,VF3,VG3,VH3,VI3],
        [VA4,VB4,VC4,VD4,VE4,VF4,VG4,VH4,VI4],
        [VA5,VB5,VC5,VD5,VE5,VF5,VG5,VH5,VI5],
        [VA6,VB6,VC6,VD6,VE6,VF6,VG6,VH6,VI6],
        [VA7,VB7,VC7,VD7,VE7,VF7,VG7,VH7,VI7],
        [VA8,VB8,VC8,VD8,VE8,VF8,VG8,VH8,VI8],
        [VA9,VB9,VC9,VD9,VE9,VF9,VG9,VH9,VI9]]):-
isAlpha(VA1,A1),isAlpha(VB1,B1),isAlpha(VC1,C1),isAlpha(VD1,D1),isAlpha(VE1,E1),isAlpha(VF1,F1),isAlpha(VG1,G1),isAlpha(VH1,H1),isAlpha(VI1,I1),
isAlpha(VA2,A2),isAlpha(VB2,B2),isAlpha(VC2,C2),isAlpha(VD2,D2),isAlpha(VE2,E2),isAlpha(VF2,F2),isAlpha(VG2,G2),isAlpha(VH2,H2),isAlpha(VI2,I2),
isAlpha(VA3,A3),isAlpha(VB3,B3),isAlpha(VC3,C3),isAlpha(VD3,D3),isAlpha(VE3,E3),isAlpha(VF3,F3),isAlpha(VG3,G3),isAlpha(VH3,H3),isAlpha(VI3,I3),
isAlpha(VA4,A4),isAlpha(VB4,B4),isAlpha(VC4,C4),isAlpha(VD4,D4),isAlpha(VE4,E4),isAlpha(VF4,F4),isAlpha(VG4,G4),isAlpha(VH4,H4),isAlpha(VI4,I4),
isAlpha(VA5,A5),isAlpha(VB5,B5),isAlpha(VC5,C5),isAlpha(VD5,D5),isAlpha(VE5,E5),isAlpha(VF5,F5),isAlpha(VG5,G5),isAlpha(VH5,H5),isAlpha(VI5,I5),
isAlpha(VA6,A6),isAlpha(VB6,B6),isAlpha(VC6,C6),isAlpha(VD6,D6),isAlpha(VE6,E6),isAlpha(VF6,F6),isAlpha(VG6,G6),isAlpha(VH6,H6),isAlpha(VI6,I6),
isAlpha(VA7,A7),isAlpha(VB7,B7),isAlpha(VC7,C7),isAlpha(VD7,D7),isAlpha(VE7,E7),isAlpha(VF7,F7),isAlpha(VG7,G7),isAlpha(VH7,H7),isAlpha(VI7,I7),
isAlpha(VA8,A8),isAlpha(VB8,B8),isAlpha(VC8,C8),isAlpha(VD8,D8),isAlpha(VE8,E8),isAlpha(VF8,F8),isAlpha(VG8,G8),isAlpha(VH8,H8),isAlpha(VI8,I8),
isAlpha(VA9,A9),isAlpha(VB9,B9),isAlpha(VC9,C9),isAlpha(VD9,D9),isAlpha(VE9,E9),isAlpha(VF9,F9),isAlpha(VG9,G9),isAlpha(VH9,H9),isAlpha(VI9,I9),
Vars = 		[A1,B1,C1,D1,E1,F1,G1,H1,I1,
            A2,B2,C2,D2,E2,F2,G2,H2,I2,
            A3,B3,C3,D3,E3,F3,G3,H3,I3,
            A4,B4,C4,D4,E4,F4,G4,H4,I4,
            A5,B5,C5,D5,E5,F5,G5,H5,I5,
            A6,B6,C6,D6,E6,F6,G6,H6,I6,
            A7,B7,C7,D7,E7,F7,G7,H7,I7,
            A8,B8,C8,D8,E8,F8,G8,H8,I8,
			A9,B9,C9,D9,E9,F9,G9,H9,I9],
Vars ins 1..9,
 	all_different([A1,B1,C1,D1,E1,F1,G1,H1,I1]),
    all_different([A2,B2,C2,D2,E2,F2,G2,H2,I2]),
    all_different([A3,B3,C3,D3,E3,F3,G3,H3,I3]),
    all_different([A4,B4,C4,D4,E4,F4,G4,H4,I4]),
    all_different([A5,B5,C5,D5,E5,F5,G5,H5,I5]),
    all_different([A6,B6,C6,D6,E6,F6,G6,H6,I6]),
    all_different([A7,B7,C7,D7,E7,F7,G7,H7,I7]),
    all_different([A8,B8,C8,D8,E8,F8,G8,H8,I8]),
    all_different([A9,B9,C9,D9,E9,F9,G9,H9,I9]),

   
    all_different([A1,A2,A3,A4,A5,A6,A7,A8,A9]),
    all_different([B1,B2,B3,B4,B5,B6,B7,B8,B9]),
    all_different([C1,C2,C3,C4,C5,C6,C7,C8,C9]),
    all_different([D1,D2,D3,D4,D5,D6,D7,D8,D9]),
    all_different([E1,E2,E3,E4,E5,E6,E7,E8,E9]),
    all_different([F1,F2,F3,F4,F5,F6,F7,F8,F9]),
    all_different([G1,G2,G3,G4,G5,G6,G7,G8,G9]),
    all_different([H1,H2,H3,H4,H5,H6,H7,H8,H9]),
    all_different([I1,I2,I3,I4,I5,I6,I7,I8,I9]),

  
    all_different([A1,A2,A3,B1,B2,B3,C1,C2,C3]),
    all_different([D1,D2,D3,E1,E2,E3,F1,F2,F3]),
    all_different([G1,G2,G3,H1,H2,H3,I1,I2,I3]),

    all_different([A4,A5,A6,B4,B5,B6,C4,C5,C6]),
    all_different([D4,D5,D6,E4,E5,E6,F4,F5,F6]),
    all_different([G4,G5,G6,H4,H5,H6,I4,I5,I6]),

    all_different([A7,A8,A9,B7,B8,B9,C7,C8,C9]),
    all_different([D7,D8,D9,E7,E8,E9,F7,F8,F9]),
    all_different([G7,G8,G9,H7,H8,H9,I7,I8,I9]),
label(Vars),
isNumber(A1,VLA1),isNumber(B1,VLB1),isNumber(C1,VLC1),isNumber(D1,VLD1),isNumber(E1,VLE1),isNumber(F1,VLF1),isNumber(G1,VLG1),isNumber(H1,VLH1),isNumber(I1,VLI1),
isNumber(A2,VLA2),isNumber(B2,VLB2),isNumber(C2,VLC2),isNumber(D2,VLD2),isNumber(E2,VLE2),isNumber(F2,VLF2),isNumber(G2,VLG2),isNumber(H2,VLH2),isNumber(I2,VLI2),
isNumber(A3,VLA3),isNumber(B3,VLB3),isNumber(C3,VLC3),isNumber(D3,VLD3),isNumber(E3,VLE3),isNumber(F3,VLF3),isNumber(G3,VLG3),isNumber(H3,VLH3),isNumber(I3,VLI3),
isNumber(A4,VLA4),isNumber(B4,VLB4),isNumber(C4,VLC4),isNumber(D4,VLD4),isNumber(E4,VLE4),isNumber(F4,VLF4),isNumber(G4,VLG4),isNumber(H4,VLH4),isNumber(I4,VLI4),
isNumber(A5,VLA5),isNumber(B5,VLB5),isNumber(C5,VLC5),isNumber(D5,VLD5),isNumber(E5,VLE5),isNumber(F5,VLF5),isNumber(G5,VLG5),isNumber(H5,VLH5),isNumber(I5,VLI5),
isNumber(A6,VLA6),isNumber(B6,VLB6),isNumber(C6,VLC6),isNumber(D6,VLD6),isNumber(E6,VLE6),isNumber(F6,VLF6),isNumber(G6,VLG6),isNumber(H6,VLH6),isNumber(I6,VLI6),
isNumber(A7,VLA7),isNumber(B7,VLB7),isNumber(C7,VLC7),isNumber(D7,VLD7),isNumber(E7,VLE7),isNumber(F7,VLF7),isNumber(G7,VLG7),isNumber(H7,VLH7),isNumber(I7,VLI7),
isNumber(A8,VLA8),isNumber(B8,VLB8),isNumber(C8,VLC8),isNumber(D8,VLD8),isNumber(E8,VLE8),isNumber(F8,VLF8),isNumber(G8,VLG8),isNumber(H8,VLH8),isNumber(I8,VLI8),
isNumber(A9,VLA9),isNumber(B9,VLB9),isNumber(C9,VLC9),isNumber(D9,VLD9),isNumber(E9,VLE9),isNumber(F9,VLF9),isNumber(G9,VLG9),isNumber(H9,VLH9),isNumber(I9,VLI9),
Ans = [VLA1,VLB1,VLC1,VLD1,VLE1,VLF1,VLG1,VLH1,VLI1,
            VLA2,VLB2,VLC2,VLD2,VLE2,VLF2,VLG2,VLH2,VLI2,
            VLA3,VLB3,VLC3,VLD3,VLE3,VLF3,VLG3,VLH3,VLI3,
            VLA4,VLB4,VLC4,VLD4,VLE4,VLF4,VLG4,VLH4,VLI4,
            VLA5,VLB5,VLC5,VLD5,VLE5,VLF5,VLG5,VLH5,VLI5,
            VLA6,VLB6,VLC6,VLD6,VLE6,VLF6,VLG6,VLH6,VLI6,
            VLA7,VLB7,VLC7,VLD7,VLE7,VLF7,VLG7,VLH7,VLI7,
            VLA8,VLB8,VLC8,VLD8,VLE8,VLF8,VLG8,VLH8,VLI8,
VLA9,VLB9,VLC9,VLD9,VLE9,VLF9,VLG9,VLH9,VLI9],
printSudoku(Ans).

printSudoku([VLA1,VLB1,VLC1,VLD1,VLE1,VLF1,VLG1,VLH1,VLI1,
            VLA2,VLB2,VLC2,VLD2,VLE2,VLF2,VLG2,VLH2,VLI2,
            VLA3,VLB3,VLC3,VLD3,VLE3,VLF3,VLG3,VLH3,VLI3,
            VLA4,VLB4,VLC4,VLD4,VLE4,VLF4,VLG4,VLH4,VLI4,
            VLA5,VLB5,VLC5,VLD5,VLE5,VLF5,VLG5,VLH5,VLI5,
            VLA6,VLB6,VLC6,VLD6,VLE6,VLF6,VLG6,VLH6,VLI6,
            VLA7,VLB7,VLC7,VLD7,VLE7,VLF7,VLG7,VLH7,VLI7,
            VLA8,VLB8,VLC8,VLD8,VLE8,VLF8,VLG8,VLH8,VLI8,
VLA9,VLB9,VLC9,VLD9,VLE9,VLF9,VLG9,VLH9,VLI9]):-
format('The solved sudoku is :- '),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA1,VLB1,VLC1,VLD1,VLE1,VLF1,VLG1,VLH1,VLI1]),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA2,VLB2,VLC2,VLD2,VLE2,VLF2,VLG2,VLH2,VLI2]),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA3,VLB3,VLC3,VLD3,VLE3,VLF3,VLG3,VLH3,VLI3]),nl,
format('----------------------'),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA4,VLB4,VLC4,VLD4,VLE4,VLF4,VLG4,VLH4,VLI4]),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA5,VLB5,VLC5,VLD5,VLE5,VLF5,VLG5,VLH5,VLI5]),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA6,VLB6,VLC6,VLD6,VLE6,VLF6,VLG6,VLH6,VLI6]),nl,
format('----------------------'),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA7,VLB7,VLC7,VLD7,VLE7,VLF7,VLG7,VLH7,VLI7]),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA8,VLB8,VLC8,VLD8,VLE8,VLF8,VLG8,VLH8,VLI8]),nl,
format('~w ~w ~w | ~w ~w ~w | ~w ~w ~w',[VLA9,VLB9,VLC9,VLD9,VLE9,VLF9,VLG9,VLH9,VLI9]),nl.