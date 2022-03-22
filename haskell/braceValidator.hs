-- https://www.codewars.com/kata/5277c8a221e209d3f6000b56
validBraces :: String -> Bool
validBraces = validBraces' []

validBraces' :: [Char] -> String -> Bool
validBraces' [] (c:cs)
    | c == '(' || c == '{' || c == '['  = validBraces' [c] cs       -- Open bracket -> add to stack
    | otherwise = False                                             -- Closed bracket with no opening bracket -> False
validBraces' (p:ps) (c:cs)
    | c == '(' || c == '{' || c == '['  = validBraces' (c:p:ps) cs  -- Open bracket, add to stack
    | c == ')' && (p /= '(')            = False                     -- Closed does not match last open, return False
    | c == '}' && (p /= '{')            = False
    | c == ']' && p /= '['              = False
    | otherwise                         = validBraces' ps cs        -- Closed bracket matched, remove open from stack and continue
validBraces' [] [] = True                                           -- Everything processed  -> True
validBraces' any [] = False                                         -- if anything left open -> False