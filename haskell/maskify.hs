-- https://www.codewars.com/kata/5412509bd436bd33920011bc
module Maskify where

maskify :: String -> String
maskify []             = ""
maskify (c:cs)
    | length cs > 3    = "#" ++ maskify cs
    | otherwise        = c:maskify cs