msort [] = []
msort [x] = [x]
msort xs = merge (msort left) (msort right)
  where
    (left, right) = halve xs

halve xs = splitAt (length xs `div` 2) xs
