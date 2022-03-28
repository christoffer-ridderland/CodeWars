-- https://www.codewars.com/kata/5412509bd436bd33920011bc
module Maskify where

maskify :: String -> String
maskify []             = ""                -- Base case, empty string
maskify (c:cs)
    | length cs > 3    = "#" ++ maskify cs -- last four eleménts should be visible
    | otherwise        = c:maskify cs      -- not last 4, replace with #