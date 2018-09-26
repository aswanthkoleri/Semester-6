row(state(h,h,h,bm,m,m),boat(bm,m,right),state(h,h,h,e,e,m)).
row(state(h,h,h,e,e,m),boat(bm,e,left),state(h,h,h,bm,e,m)).
row(state(h,h,h,bm,e,m),boat(bm,m,right),state(h,h,h,e,e,e)).
row(state(h,h,h,e,e,e),boat(bm,e,left),state(h,h,h,bm,e,e)).
row(state(h,h,h,bm,e,e),boat(h,h,right),state(h,e,e,bm,e,e)).
row(state(h,e,e,bm,e,e),boat(h,m,left),state(h,h,e,bm,m,e)).
row(state(h,h,e,bm,m,e),boat(h,bm,right),state(h,e,e,e,m,e)).
row(state(h,e,e,e,m,e),boat(h,m,left),state(h,h,e,e,m,m)).
row(state(h,h,e,e,m,m),boat(h,h,right),state(e,e,e,e,m,m)).
row(state(e,e,e,e,m,m),boat(bm,e,left),state(e,e,e,bm,m,m)).
row(state(e,e,e,bm,m,m),boat(bm,m,right),state(e,e,e,e,e,m)).
row(state(e,e,e,e,e,m),boat(bm,e,left),state(e,e,e,bm,e,m)).
row(state(e,e,e,bm,e,m),boat(bm,m,right),state(e,e,e,e,e,e)).

canget(state(e,e,e,e,e,e)).

canget(S):-
	row(S,X,S2),
	canget(S2).
