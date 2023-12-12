{- 1 -}
True || True = True
True || False = True
False || True = True
False || False = False

{- 2 -}
True || _ = True
False || _ = False

{- 3 -}
False || False = False
_ || _ = True
