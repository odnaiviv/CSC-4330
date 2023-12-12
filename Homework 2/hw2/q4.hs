isperfect n = n == sum (factors s) - n

perfects :: Int -> [Int]
perfects x = [n | n <- [1 .. x], isperfect n]
