elem' _ [] = False
elem' y (x : xs) = x == y || elem' y xs
