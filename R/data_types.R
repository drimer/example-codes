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
