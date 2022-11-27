# Deterministic-Finite-Automata

In The Troll's Bridge, the player is forced to leave their home country because of a famine and seek sanctuary in a city. There is a bridge between the player's village and the city that is manned by a troll-like creature. Anyone who wants to cross must toss the troll's coin and get three straight tails in order to do so unhurt, otherwise the game is over because the Troll will eat them. The following conduct corresponds to this behaviour:

3 consecutive tails → you cross the bridge unharmed and win

'a' means tails and,
'b' means heads.

Therefore, for any 3 consecutive tails the path followed is Q0 → Q1 → Q3 → Q5 where Q5 is the win state of the game. 


The regular expression is q5 = (a + ab + baa)(b + ab)(a + aa)aaab
