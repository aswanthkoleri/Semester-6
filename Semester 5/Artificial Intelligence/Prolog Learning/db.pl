loves(romeo,juliet).
loves(juliet,romeo). :-loves(romeo,juliet).
happy(albert).
runs(albert) :- 
	happy(albert).
does_alice_dance. :- happy(albert),
					write('Alice Dances').