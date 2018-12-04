:- include('bases.pl').

piece('bureau').
piece('salon').
piece('cuisine').

present('Bruno','cuisine').

/*

règles non atomiques
*/


mobile(X):-personne(X), \+ objet(X).
immobile(X):- !,\+ mobile(X).

localise(X):- personne(X), piece(Y), present(X,Y), write('Localisation de  '),write(X), write(' : '), write(Y), nl.