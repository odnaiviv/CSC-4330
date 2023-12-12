positions x xs = [i | (x', i) <- zip xs [0 ..], x == x']
