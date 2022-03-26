-- https://www.codewars.com/kata/58e230e5e24dde0996000070

nextPrime :: Integer -> Integer
nextPrime n
  | n < 7                                                   = forSmall n
  | otherwise                                               = nextPrime' (n + 1)

forSmall :: Integer -> Integer
forSmall n
  | n < 2                                                    = 2
  | even n                                                   = n + 1
  | otherwise                                                = n + 2

nextPrime' :: Integer  -> Integer
nextPrime' n
  | even n                                                  = nextPrime' (n + 1)
  | n `mod` 3 == 0                                          = nextPrime' (n + 2)
  | otherwise                                               = nextPrime'' n 5

nextPrime'' :: Integer -> Integer -> Integer
nextPrime'' n i
  | n `mod` i == 0 || n `mod` (i + 2) == 0                  = nextPrime' (n + 2)
  | i * i <= n                                              = nextPrime'' n (i + 6)
  | otherwise                                               = n