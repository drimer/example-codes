## dput and dget-ting objects

> y <- data.frame(a = 1, b = 2)
> y <- data.frame(a = 1, b = "a")
> dput(y)
structure(list(a = 1, b = structure(1L, .Label = "a", class = "factor")), .Names = c("a", 
"b"), row.names = c(NA, -1L), class = "data.frame")
> dput(y, file = "y.R")
> new.y <- dget("y.R")
> new.y
  a b
1 1 a


## dumping objects

> y <- data.frame(a = 1, b = 2)
> y <- data.frame(a = 1, b = "a")
> dput(y)
structure(list(a = 1, b = structure(1L, .Label = "a", class = "factor")), .Names = c("a", 
"b"), row.names = c(NA, -1L), class = "data.frame")
> dput(y, file = "y.R")
> new.y <- dget("y.R")
> new.y
  a b
1 1 a


## reading lines from a file

> con <- file("words.txt")
> x <- readLines(con, 10)
> x
[1] "First line."   "Second line."  "Third line."   "Fourth line."  "Fifth line."  
[6] "Sixth line."   "Sevenht line." "Eighth line."  "Ninth line." 


## reading lines from a webpage

> con <- url("http://www.albertoaj.com", "r")
> x <- readLines(con)
Warning message:
In readLines(con) :
  incomplete final line found on 'http://www.albertoaj.com'
> head(x)
[1] ""                                                                         
[2] ""                                                                         
[3] "<!doctype html>"                                                          
[4] "<html>"                                                                   
[5] "<head>"                                                                   
[6] "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />"
