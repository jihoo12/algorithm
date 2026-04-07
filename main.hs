main :: IO ()
main = do
    line <- getLine
    let numbers = map read (words line) :: [Int]
    print(sum numbers)