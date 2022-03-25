% https://www.codewars.com/kata/555624b601231dc7a400017a

-module(kata).
-export([josephus_survivor/2, josephus_killer/4]).

josephus_survivor(N, K) ->
    josephus_killer(lists:seq(1, N), K, K, N).

josephus_killer([Survivor | []], _, _, _) ->
    Survivor;

josephus_killer([N | Ns], 1, CK, I) ->
    josephus_killer(Ns, CK, CK, I - 1);

josephus_killer([N | Ns], K, CK, I) when K > I ->
    josephus_killer([N | Ns], K - I, CK, I);

josephus_killer(Ns, K, CK, I) ->
    josephus_killer(lists:append([N || N <- Ns, N < K], lists:reverse([N || N <- Ns, N > K])), CK, CK, I - 1).

