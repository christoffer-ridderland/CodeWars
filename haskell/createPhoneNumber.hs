--https://www.codewars.com/kata/525f50e3b73515a6db000b83
module CreatePhoneNumber where
import Text.Printf
createPhoneNumber :: [Int] -> String
createPhoneNumber [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9] = printf "(%d%d%d) %d%d%d-%d%d%d%d" d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 -- formatting
createPhoneNumber _                                        = "not valid" -- not a valid phone number, 10 digits required