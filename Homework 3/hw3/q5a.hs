sum' [] = 0
sum' (x : xs) = x + sum' xs
