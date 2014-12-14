################################# VECTORS ######################################

# A range on integers
> 1:10
[1]  1  2  3  4  5  6  7  8  9 10

# Containing specific values
> c(0.5, 0.6)
[1] 0.5 0.6
> c(TRUE, FALSE)
[1]  TRUE FALSE
> c(T, F)
[1]  TRUE FALSE
> c("a", "b", "c")
[1] "a" "b" "c"

# Using the vector function
> vector("numeric", length = 10)  # 1st arg is elemnts type
[1] 0 0 0 0 0 0 0 0 0 0

# Mixing objects: coercion
> c(1.4, "hi")
[1] "1.4" "hi"
> c(TRUE, 5)
[1] 1 5
> c("b", FALSE)
[1] "b" "FALSE"



################################# COERCION #####################################

> x <- 1:10
> class(x)
[1] "integer"
> as.numeric(x)
[1]  1  2  3  4  5  6  7  8  9 10
> as.character(x)
[1] "1"  "2"  "3"  "4"  "5"  "6"  "7"  "8"  "9"  "10"

> x <- c("a", "b", "c")
> as.numeric(x)
[1] NA NA NA
Warning message:
NAs introduced by coercion
> as.logical(x)
[1] NA NA NA
> as.complex(x)
[1] NA NA NA
Warning message:
NAs introduced by coercion



################################## MATRICES ####################################

# Specifying only the dimensions, leaving it with no data
> m <- matrix(nrow = 2, ncol = 5)
> m
     [,1] [,2] [,3] [,4] [,5]
[1,]   NA   NA   NA   NA   NA
[2,]   NA   NA   NA   NA   NA
> dim(m)
[1] 2 5
> attributes(m)
$dim
[1] 2 5

# Specifying the dimensions along with the data
> m <- matrix(1:10, nrow = 2, ncol = 5)
> m
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    3    5    7    9
[2,]    2    4    6    8   10

# Using a vector
> m <- 1:10
> m
 [1]  1  2  3  4  5  6  7  8  9 10
> dim(m) <- c(2, 5)  # Set the attribute "dim" in the vector
> m
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    3    5    7    9
[2,]    2    4    6    8   10

# Binding columns or rows
> x <- 4:6
> y <- 7:9
> cbind(x, y)
     x y
[1,] 4 7
[2,] 5 8
[3,] 6 9
> rbind(x, y)
  [,1] [,2] [,3]
x    4    5    6
y    7    8    9



################################## LISTS #######################################

> list(5, FALSE, "c", 3+1i)
[[1]]
[1] 5

[[2]]
[1] FALSE

[[3]]
[1] "c"

[[4]]
[1] 3+1i


################################## FACTORS #####################################

> x <- factor(c("blue", "red", "red", "blue", "red"))
> x
[1] blue red  red  blue red 
Levels: blue red
> table(x)
x
blue  red 
   2    3 
> unclass(x)
[1] 1 2 2 1 2
attr(,"levels")
[1] "blue" "red" 

# Specifying the order of the levels
> x <- factor(c("blue", "red", "red", "blue", "red"), levels = c("red", "blue"))
> x
[1] blue red  red  blue red 
Levels: red blue
> table(x)
x
 red blue 
   3    2 
> unclass(x)
[1] 2 1 1 2 1
attr(,"levels")
[1] "red"  "blue"


################################ MISSING VALUES ###############################

> x <- c(TRUE, NA, 5, FALSE, NaN)
> is.nan(x)
[1] FALSE FALSE FALSE FALSE  TRUE
> is.na(x)
[1] FALSE  TRUE FALSE FALSE  TRUE


################################ DATA FRAMES ##################################

> x <- data.frame(foo = 1:4, bar = c(T, T, F, F))
> x
  foo   bar
1   1  TRUE
2   2  TRUE
3   3 FALSE
4   4 FALSE
> nrow(x)
[1] 4
> ncol(x)
[1] 2


################################## NAMES ######################################

# In a vector
> x <- 1:3
> names(x)
NULL
> names(x) = c("foo", "bar", "blah")
> x
 foo  bar blah 
   1    2    3 
> names(x)
[1] "foo"  "bar"  "blah"

# In a list
> x <- list(a = 1, b = 2, c = 3)
> x
$a
[1] 1

$b
[1] 2

$c
[1] 3

# In a matrix
> m <- matrix(1:4, nrow = 2, ncol = 2)
> dimnames(m) <- list(c("a", "b"), c("c", "d"))
> m
  c d
a 1 3
b 2 4
