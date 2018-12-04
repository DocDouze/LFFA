
houses([
	house(_,_,_,_,_),
	house(_,_,_,_,_),
	house(_,_,_,_,_),
	house(_,_,_,_,_),
	house(_,_,_,_,_)
]).

right_of(A,B, [B,A | _]).
right_of(A,B, [_| Y]) :- right_of(A,B,Y).

next_to(A,B, [A,B | _]).
next_to(A,B, [B,A | _]).
next_to(A,B, [_| Y]) :- next_to(A,B,Y).

mymember(X, [X|_]).
mymember(X, [_|Y]):- mymember(X,Y).


print_houses([]).
print_houses([A|B]) :-
	write(A), nl,
	print_houses(B).

but:- houses(Houses),
      Houses=([house(_,norvegien,_,_,_) | _]),
      Houses=([_,_,house(_,_,lait,_,_) | _]),
      right_of(house(blanche,_,_,_,_),house(verte,_,_,_,_),Houses),
      next_to(house(_,norvegien,_,_,_),house(bleue,_,_,_,_), Houses),
      next_to(house(_,_,_,chesterfields,_),house(_,_,_,_,renard), Houses),
      next_to(house(_,_,_,kools,_),house(_,_,_,_,cheval), Houses),
      member(house(rouge,anglais,_,_,_), Houses),
      member(house(verte,_,cafe,_,_), Houses),
      member(house(jaune,_,_,kools,_), Houses),
      member(house(_,espagnol,_,_,chien), Houses),
      member(house(_,ukrainien,the,_,_), Houses),
      member(house(_,japonais,_,cravens,_), Houses),
      member(house(_,_,_,oldgolds,escargot), Houses),
      member(house(_,_,vin,gitanes,_), Houses),
      member(house(_,_,eau,_,_), Houses),
      member(house(_,_,_,_,zebre), Houses),
      
      print_houses(Houses).
