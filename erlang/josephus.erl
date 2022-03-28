% https://www.codewars.com/kata/555624b601231dc7a400017a

% This solution is very inefficient and times out in CW, will optimize some time

-module(kata).
-export([josephus_survivor/2, josephus_killer/4]).

josephus_survivor(N, K) ->
    josephus_killer(lists:seq(1, N), K, K, N).          % (List from 1 to N, counting variable K, starting value of K, Number of elements left)

josephus_killer([Survivor | []], _, _, _) ->            % Only one survivor, return it
    Survivor;

josephus_killer([N | Ns], 1, CK, I) ->                  % time for N to be killed of, remove N and decrement I
    josephus_killer(Ns, CK, CK, I - 1);

josephus_killer([N | Ns], K, CK, I) when K > I ->       % If K > I we can subtract I from K
    josephus_killer([N | Ns], K - I, CK, I);

josephus_killer(Ns, K, CK, I) ->                        % List comprehension to remone nth element from NS, decrement I
    josephus_killer(lists:append([N || N <- Ns, N < K], lists:reverse([N || N <- Ns, N > K])), CK, CK, I - 1).

