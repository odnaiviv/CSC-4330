concat' [] = []
concat' (x : xs) = x ++ concat' xs
