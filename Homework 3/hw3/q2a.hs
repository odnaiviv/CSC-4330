and' [] = True
and' (x : xs) = x && and' xs
