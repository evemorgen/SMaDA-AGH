# Advanced Statistics lab1

## There were 2 things to be done on this lab:
  - [Basic guide to R language by Dr. Mirka](as-lab1-rbasics.pdf)
  - [More stuff by Dr. Krystian](lab1_more_stuff.pdf)


## First part is done in here.

1. Create a directory on the disk (the first letter of the name + surname). It will be your Working Directory.  
   - no point for doing that
2. Run RStudio
   - nope, terminal is fine
3. Display the informations about setwd() function
   - ?setwd
```
> ?setwd
    getwd                   package:base                   R Documentation

Get or Set Working Directory

Description:

     ‘getwd’ returns an absolute filepath representing the current
     working directory of the R process; ‘setwd(dir)’ is used to set
     the working directory to ‘dir’.

Usage:

     getwd()
     setwd(dir)

Arguments:

     dir: A character string: tilde expansion will be done.
```
4. Set your Working Directory using the command setwd()
   - nope, I'm fine with my current dir ;)
5. Make sure that the Working Directory is set correctly (use the command getwd()).
   - sure thing
6. Enter an expression that assigns a value of "36.6"temp.
```
> temp <- "36.6"
> temp
[1] "36.6"
```
7. Show temp variable by typing its name.
```
> temp
[1] "36.6"
```
8. Try to add 0.1 to created variable. Is it possible? Why?
```
> temp + 0.1
Błąd w poleceniu 'temp + 0.1':
  argument nieliczbowy przekazany do operatora dwuargumentowego
```
   - It is not possible. Why? Cause R does not want to implicitly cast 0.1 to "character" (unlike java or Python)
9. Check the type of variable temp
```
> class(temp)
[1] "character"
```
10. Convert the variable “temp” to the numeric type and then check its value.
```
> as.numeric(temp)
[1] 36.6
```
   - But explicit cast is o-kay I guess
11. Convert the variable “temp” to the integer and then check its value.
```
> as.integer(temp)
[1] 36
```
   - It drops decimal part as expected
12. Check the types of the following values:
   - class("36") -> `[1] "character"`
   - class(36) -> `[1] "numeric"`
   - class(36L) -> `[1] "integer"` - L suffix sucks imo
   - class(36+0i) -> `[1] "complex"`
   - class(TRUE) -> `[1] "logical"`
13. Create a vector using the following sequence, then print a value of this vector. `v1 <- 3:0`
```
> v1
[1] 3 2 1 0
```
14. Check how to display the selected elements of the vector by typing the following expressions:
   - v1[1] -> `[1] 3`
   - v1[length(v1)] -> `[1] 0`
   -  v1[c(T,T,T,F)] -> `[1] 3 2 1`
   - v1[3:1] -> `[1] 1 2 3`
   - v1[-2] -> `[1] 3 1 0` - I was hoping for Python-ish behavior BUT apparently `-` sign stands for _"except that element"_
15.  Create the following vectors using the function c(), and then check their type and values.
   - v2 <- c(0/0, 1/0, 1/Inf, TRUE, as.numeric("abc"))
```
> v2 <- c(0/0, 1/0, 1/Inf, TRUE, as.numeric("abc"))
Komunikat ostrzegawczy:
pojawiły się wartości NA na skutek przekształcenia
> v2
[1] NaN Inf   0   1  NA
> class(v2)
[1] "numeric"
```
   - v3 <- as.logical(c("T", "False", "abc"))
```
> v3 <- as.logical(c("T", "False", "abc"))
> v3
[1]  TRUE FALSE    NA
> class(v3)
[1] "logical" <- which makes sense, lol
```
16.  Pay particular attention to the NA and NaN values. What is.na() function return if it accept the argument NaN? What is.nan() function return if it accept the argument NA?
  - NA is a logical constant of length 1 which contains a missing value indicator.
  - NaN is short for Not a Number
  - `is.na(NA)` -> TRUE
  - `is.na(NaN)` -> TRUE
  - `is.nan(NA)` -> FALSE
  - `is.nan(NaN)` -> TRUE
17.  Create an empty vector using the function vector(). Assign to it values: 1,2,3,4, "null", 5,6,7,8,9. What type of data contain this vector after assigning? Convert the vector to a vector of numeric values, and then delete the NA of the vector.
```
> v4 <- vector("numeric", length=9)
> v4[1:4] <- 1:4
> v4[5] <- "null"
> v4[6:9] <- 6:9
> v4
[1] "1"    "2"    "3"    "4"    "null" "6"    "7"    "8"    "9"
> class(v4)
[1] "character"
> as.numeric(v4)
[1]  1  2  3  4 NA  6  7  8  9
> BAD = is.na(as.numeric(v4))
> BAD
[1] FALSE FALSE FALSE FALSE  TRUE FALSE FALSE FALSE FALSE
> v4[!BAD]
[1] "1" "2" "3" "4" "6" "7" "8" "9"
```
18. Create vector v5 and v6. Then check the results of the following expressions:
```
> v5 <- 1:5
> v6 <- 6:10
> v5 + v6
[1]  7  9 11 13 15
>      v5 - v6
[1] -5 -5 -5 -5 -5
>      v5 * v6
[1]  6 14 24 36 50
>      v5 / v6
[1] 0.1666667 0.2857143 0.3750000 0.4444444 0.5000000
>      v5 == v6
[1] FALSE FALSE FALSE FALSE FALSE
>      v5 >= 3
[1] FALSE FALSE  TRUE  TRUE  TRUE
# so arithmetic operations and compares are done on every corresponding element, nice
```
19. Create a matrix using the functions cbind and rbind.
```
> m1 <- cbind(v5,v6) # binds elements to columns
> m2 <- rbind(v5,v6) # binds elements to rows (makes sense)
> m1
     v5 v6
[1,]  1  6
[2,]  2  7
[3,]  3  8
[4,]  4  9
[5,]  5 10
> m2
   [,1] [,2] [,3] [,4] [,5]
v5    1    2    3    4    5
v6    6    7    8    9   10
```
20. Display m1 matrix, then display the item on the 1,2 position in the matrix. Is the first value determines the row or column? How the parameter drop = FALSE affects the outcome?
```
> m1
     v5 v6
[1,]  1  6
[2,]  2  7
[3,]  3  8
[4,]  4  9
[5,]  5 10
>      m1[1,2]
v6
 6
>      m1[1,2, drop=FALSE]
     v6
[1,]  6
# no clue what drop does
```
21. Display rows 2 and 3 of the matrix.
```
> m1[2:3,] # colon operator defines range
     v5 v6
[1,]  2  7
[2,]  3  8
```
22. Create a matrix m3 with 2 rows and 5 columns. Complete m3 with values from 1 to 10. Note how the values have been entered into the matrix. Compare the result with the matrix m1.
```
> m3 <- matrix(1:10, nrow=2, ncol=5)
> m3
     [,1] [,2] [,3] [,4] [,5]
[1,]    1    3    5    7    9
[2,]    2    4    6    8   10
```
23. Create a 10-element vector, and then use it to create a matrix m4 of 5 rows and 2 columns. Note how the values have been entered into the matrix. Check the attributes of the matrix m4. Compare the result with the matrix m2.
```
> m4 <- 1:10
> dim(m4)
NULL
> dim(m4) <- c(5,2) # o-okay, so matrices are treated like objects?
> attributes(m4)
$dim
[1] 5 2
```
24. Create two matrices of size 2x2, then multiply them to each other.
```
> m5
     [,1] [,2]
[1,]    1    1
[2,]    1    1
> m6
     [,1] [,2]
[1,]    2    2
[2,]    2    2
> m5 * m6  # element-wise multiplication
     [,1] [,2]
[1,]    2    2
[2,]    2    2
> m5 %*% m6  # matrix multiplication?
     [,1] [,2]
[1,]    4    4
[2,]    4    4
```
25. Create a list using the list function. Check the types of the variable and its individual elements. Notice that list may have elements of different types.
```
> l1 <- list(id=1L, name="Kowalski", temp=36.6) # so list here is more like dict or named tuple?
> class(l1)
[1] "list"
> class(l1[[1]])
[1] "integer"
```
26. Check the different ways to access the items in the list. Are all these expressions give you access to the data?
   - `l1$name` -> `[1] "Kowalski"` - yeah
   - `l1["temp"]` -> `[1] 36.6` -yeah
   - `arg <- "id"` -> here magic happens
   - `l1$arg` -> `NULL`
   - `l1[arg]` -> `$id [1] 1`
   - `l1["arg"]` -> `NA NULL`
   - `l1$i` -> `[1] 1` - so it assumed that we wanted `id` I guess
   - `l1[["i"]]` -> `NULL`
   - `l1[["i", exact=FALSE]]` -> `[1] 1` - regex matching?
27. Create a dataframe, then check its attributes and the number of rows and columns.
```
> df <- data.frame(id=1:5, temp=c(36.6, NA, 37.2, 37.1, 36.8))
> attributes(df)
$names
[1] "id"   "temp"
$row.names
[1] 1 2 3 4 5
$class
[1] "data.frame"
> nrow(df)
[1] 5
> ncol(df)
[1] 2
```
28. Delete all rows in which there is NA:
```
> good <- complete.cases(df)
> df <- df[good,]
> df
  id temp
1  1 36.6
3  3 37.2
4  4 37.1
5  5 36.8
```
29. Convert dataframe into a matrix:
```
>  m <- data.matrix(df)
> m
  id temp
1  1 36.6
3  3 37.2
4  4 37.1
5  5 36.8
# looks the same?
```
30. Create a factor. Print the tabular summary and convert factor into the vector.
```
>  f <- factor(c("male","female","female","male"), level=c("male","female"))
>  table(f)
f # so its like Counter in Python?
  male female
     2      2
>      v <- unclass(f)
> v
[1] 1 2 2 1
attr(,"levels")
[1] "male"   "female"
```
