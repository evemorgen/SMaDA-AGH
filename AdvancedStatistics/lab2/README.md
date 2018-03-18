TOC:
  - [PDF with lab content](lab2.pdf)
  - [Part 1 - loading data from csv](#part-1-loading-data)
  - [Part 2 - Operations on vectors](#part-2-vectorized-operations)
  - [Part 3 - Subsetting data](#part-3-subsetting-data)
  - [Part 4 - Control structures](#part-4-control-structures)
  - [Part 5 - Exercises](#part-5-exercises)


#Solutions:

## Part 1 - loading data
1. Run R studio  
`mhm..`
2. Set your working directory using the setwd() command  
`comeon..`
3. Download, extract and open .csv file using ...
```
> download.file("http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/car-speeds.csv.zip", "car-speeds.csv.zip")
próbowanie adresu URL 'http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/car-speeds.csv.zip'
Content type 'application/zip' length 971 bytes
==================================================
downloaded 971 bytes

> unzip("./car-speeds.csv.zip")
> carSpeeds <- read.csv(file='car-speeds.csv')
> head(carSpeeds)
  Color Speed     State
1  Blue    32 NewMexico
2   Red    45   Arizona
3  Blue    35  Colorado
4 White    34   Arizona
5   Red    25   Arizona
6  Blue    41   Arizona
```

4. Replace 'Blue' color with 'Green' in the $Color column using ifelse function.  
before:
```
> carSpeeds$Color
  [1] Blue   Red  Blue  White Red   Blue  Blue  Black White Red   Red   White
 [13] Blue  Blue  Black Red   Blue  Blue  White Blue  Blue  Blue  Red   Blue
 [25] Red   Red   Red   Red   White Blue  Red   White Black Red   Black Black
 [37] Blue  Red   Black Red   Black Black Red   Red   White Black Blue  Red
 [49] Red   Black Black Red   White Red   Blue  Blue  Black Blue  White Black
 [61] Red   Blue  Blue  White Black Red   Red   Black Blue  White Blue  Red
 [73] White White Blue  Blue  Blue  Blue  Blue  White Black Blue  White Black
 [85] Black Red   Red   White White White White Red   Red   Red   White Black
 [97] White Black Black White
Levels:  Red Black Blue Red White
```
`> carSpeeds$Color <- ifelse(carSpeeds$Color=='Blue', 'Green', carSpeeds$Color)`
after:  
```
> carSpeeds$Color
  [1] "Green" "1"     "Green" "5"     "4"     "Green" "Green" "2"     "5"
 [10] "4"     "4"     "5"     "Green" "Green" "2"     "4"     "Green" "Green"
 [19] "5"     "Green" "Green" "Green" "4"     "Green" "4"     "4"     "4"
 [28] "4"     "5"     "Green" "4"     "5"     "2"     "4"     "2"     "2"
 [37] "Green" "4"     "2"     "4"     "2"     "2"     "4"     "4"     "5"
 [46] "2"     "Green" "4"     "4"     "2"     "2"     "4"     "5"     "4"
 [55] "Green" "Green" "2"     "Green" "5"     "2"     "4"     "Green" "Green"
 [64] "5"     "2"     "4"     "4"     "2"     "Green" "5"     "Green" "4"
 [73] "5"     "5"     "Green" "Green" "Green" "Green" "Green" "5"     "2"
 [82] "Green" "5"     "2"     "2"     "4"     "4"     "5"     "5"     "5"
 [91] "5"     "4"     "4"     "4"     "5"     "2"     "5"     "2"     "2"
[100] "5"
```

5. Load same dataset as before but with stringsAsFactors argument set to False. Then use ifelse as before
```
> carSpeeds <- read.csv(file='./car-speeds.csv', stringsAsFactors=FALSE)
> carSpeeds$Color <- ifelse(carSpeeds$Color=='Blue', 'Green', carSpeeds$Color)
> carSpeeds$Color
  [1] "Green" " Red"  "Green" "White" "Red"   "Green" "Green" "Black" "White"
 [10] "Red"   "Red"   "White" "Green" "Green" "Black" "Red"   "Green" "Green"
 [19] "White" "Green" "Green" "Green" "Red"   "Green" "Red"   "Red"   "Red"
 [28] "Red"   "White" "Green" "Red"   "White" "Black" "Red"   "Black" "Black"
 [37] "Green" "Red"   "Black" "Red"   "Black" "Black" "Red"   "Red"   "White"
 [46] "Black" "Green" "Red"   "Red"   "Black" "Black" "Red"   "White" "Red"
 [55] "Green" "Green" "Black" "Green" "White" "Black" "Red"   "Green" "Green"
 [64] "White" "Black" "Red"   "Red"   "Black" "Green" "White" "Green" "Red"
 [73] "White" "White" "Green" "Green" "Green" "Green" "Green" "White" "Black"
 [82] "Green" "White" "Black" "Black" "Red"   "Red"   "White" "White" "White"
 [91] "White" "Red"   "Red"   "Red"   "White" "Black" "White" "Black" "Black"
[100] "White"
# seems a bit nicer
```
6. Use the as.is argument to import colors of cars as strings and names of states as factors.
```
> carSpeeds <- read.csv(file='./car-speeds.csv', as.is=1)
> carSpeeds$Color <- ifelse(carSpeeds$Color=='Blue', 'Green', carSpeeds$Color)
> carSpeeds$Color
  [1] "Green" " Red"  "Green" "White" "Red"   "Green" "Green" "Black" "White"
 [10] "Red"   "Red"   "White" "Green" "Green" "Black" "Red"   "Green" "Green"
 [19] "White" "Green" "Green" "Green" "Red"   "Green" "Red"   "Red"   "Red"
 [28] "Red"   "White" "Green" "Red"   "White" "Black" "Red"   "Black" "Black"
 [37] "Green" "Red"   "Black" "Red"   "Black" "Black" "Red"   "Red"   "White"
 [46] "Black" "Green" "Red"   "Red"   "Black" "Black" "Red"   "White" "Red"
 [55] "Green" "Green" "Black" "Green" "White" "Black" "Red"   "Green" "Green"
 [64] "White" "Black" "Red"   "Red"   "Black" "Green" "White" "Green" "Red"
 [73] "White" "White" "Green" "Green" "Green" "Green" "Green" "White" "Black"
 [82] "Green" "White" "Black" "Black" "Red"   "Red"   "White" "White" "White"
 [91] "White" "Red"   "Red"   "Red"   "White" "Black" "White" "Black" "Black"
[100] "White"
> carSpeeds$State <- ifelse(carSpeeds$State=='Arizona', 'Ohio', carSpeeds$State)
> carSpeeds$State
  [1] "3"    "Ohio" "2"    "Ohio" "Ohio" "Ohio" "3"    "2"    "Ohio" "2"
 [11] "4"    "4"    "4"    "4"    "4"    "3"    "Ohio" "3"    "Ohio" "4"
 [21] "4"    "4"    "3"    "2"    "2"    "3"    "2"    "4"    "2"    "4"
 [31] "3"    "2"    "2"    "4"    "2"    "2"    "3"    "Ohio" "4"    "2"
 [41] "2"    "3"    "Ohio" "4"    "Ohio" "2"    "3"    "3"    "3"    "2"
 [51] "Ohio" "4"    "4"    "Ohio" "3"    "2"    "4"    "2"    "4"    "4"
 [61] "4"    "2"    "3"    "2"    "3"    "2"    "3"    "Ohio" "3"    "4"
 [71] "4"    "2"    "Ohio" "4"    "2"    "2"    "2"    "Ohio" "3"    "Ohio"
 [81] "4"    "2"    "2"    "Ohio" "Ohio" "Ohio" "4"    "Ohio" "4"    "4"
 [91] "4"    "Ohio" "Ohio" "3"    "2"    "2"    "4"    "3"    "Ohio" "4"

> carSpeeds <- read.csv(file='./car-speeds.csv', as.is=1)
> carSpeeds$Color <- ifelse(carSpeeds$Color=='Blue', 'Green', carSpeeds$Color)
> carSpeeds$Color
  [1] "Green" " Red"  "Green" "White" "Red"   "Green" "Green" "Black" "White"
 [10] "Red"   "Red"   "White" "Green" "Green" "Black" "Red"   "Green" "Green"
 [19] "White" "Green" "Green" "Green" "Red"   "Green" "Red"   "Red"   "Red"
 [28] "Red"   "White" "Green" "Red"   "White" "Black" "Red"   "Black" "Black"
 [37] "Green" "Red"   "Black" "Red"   "Black" "Black" "Red"   "Red"   "White"
 [46] "Black" "Green" "Red"   "Red"   "Black" "Black" "Red"   "White" "Red"
 [55] "Green" "Green" "Black" "Green" "White" "Black" "Red"   "Green" "Green"
 [64] "White" "Black" "Red"   "Red"   "Black" "Green" "White" "Green" "Red"
 [73] "White" "White" "Green" "Green" "Green" "Green" "Green" "White" "Black"
 [82] "Green" "White" "Black" "Black" "Red"   "Red"   "White" "White" "White"
 [91] "White" "Red"   "Red"   "Red"   "White" "Black" "White" "Black" "Black"
[100] "White"
```

7. Check for unique values in the $Color column of the dataset to see if there are any whitespaces. Use unique function
```
> unique(carSpeeds$Color)
[1] "Green" " Red"  "White" "Red"   "Black"
```

8. Import dataset using the `strip.white` argument, then check again $Color cloumn for uniqness.
```
> carSpeeds <- read.csv(file='./car-speeds.csv', stringsAsFactors=FALSE, strip.white=TRUE,sep=',')
> head(carSpeeds)
  Color Speed     State
1  Blue    32 NewMexico
2   Red    45   Arizona
3  Blue    35  Colorado
4 White    34   Arizona
5   Red    25   Arizona
6  Blue    41   Arizona
> unique(carSpeeds$Color)
[1] "Blue"  "Red"   "White" "Black"
# no green? huh?
```

9. Export the dataset with replaced 'Blue' and 'Green' in the $Color column by using `write.csv`.
```
> write.csv(carSpeeds, file='./car-speeds-cleared.csv')
>
Save workspace image? [y/n/c]: n
14:44:32 evemorgen@pc67.home ~ head car-speeds-cleared.csv
"","Color","Speed","State"
"1","Green",32,"NewMexico"
"2","Red",45,"Arizona"
"3","Green",35,"Colorado"
"4","White",34,"Arizona"
"5","Red",25,"Arizona"
"6","Green",41,"Arizona"
"7","Green",34,"NewMexico"
"8","Black",29,"Colorado"
"9","White",31,"Arizona"
```

10. Correct the output file by setting row.names argument to false.
```
> write.csv(carSpeeds, file='./car-speeds-cleared.csv', row.names=FALSE)
>
Save workspace image? [y/n/c]: y
14:46:08 evemorgen@pc67.home ~ head car-speeds-cleared.csv
"Color","Speed","State"
"Green",32,"NewMexico"
"Red",45,"Arizona"
"Green",35,"Colorado"
"White",34,"Arizona"
"Red",25,"Arizona"
"Green",41,"Arizona"
"Green",34,"NewMexico"
"Black",29,"Colorado"
"White",31,"Arizona"
```
11. Replace the speed in the 3rd row of CarSpeeds with NA value by using index. Then write new csv file with NA replaced by -9999
```
> carSpeeds$Speed[3] <- NA
> head(carSpeeds)
  Color Speed     State
1 Green    32 NewMexico
2   Red    45   Arizona
3 Green    NA  Colorado
4 White    34   Arizona
5   Red    25   Arizona
6 Green    41   Arizona
> write.csv(carSpeeds, file='./car-speeds-cleared.csv', row.names=FALSE, na='-9999')
>
Save workspace image? [y/n/c]: y
14:48:04 evemorgen@pc67.home ~ head car-speeds-cleared.csv
"Color","Speed","State"
"Green",32,"NewMexico"
"Red",45,"Arizona"
"Green",-9999,"Colorado"
"White",34,"Arizona"
"Red",25,"Arizona"
"Green",41,"Arizona"
"Green",34,"NewMexico"
"Black",29,"Colorado"
"White",31,"Arizona"
```

## Part 2 - vectorized operations
1. Create two vectors: `a` and `b` with values `1:10` and then add pairs of numbers contained in this two vectors
```
> a <- 1:10
> b <- 1:10
> a
 [1]  1  2  3  4  5  6  7  8  9 10
> a+b
 [1]  2  4  6  8 10 12 14 16 18 20
```
2. Create a vector `c` with `1:5` values, then add this vector to vector a.
```
> c <- 1:5
> a + c
 [1]  2  4  6  8 10  7  9 11 13 15
>
# Recycling Rule
# If two vectors are of unequal length, the shorter one will be recycled in order to match the longer vector. For example, the following vectors u and v have different lengths, and their sum is computed by recycling values of the shorter vector u.
```
3. Multiply every element of vector by 5
```
> a * 5
 [1]  5 10 15 20 25 30 35 40 45 50
```
4. Try to add vector a and e. Notice that this time the length of the longer object is not a multiple of the shorter object length.
```
> e < 1:7
> a+e
 [1]  2  4  6  8 10 12 14  9 11 13
# so it just cycles through smaller one
Komunikat ostrzegawczy:
W poleceniu 'a + e':
  długość dłuszego obiektu nie jest wielokrotnością długości krótszego obiektu
```

# Part 3 - Subsetting data
1. Create a vector animal as in the example below. Then subset this vector with first three and then last three characters.
```
> animal <- c('m', 'o', 'n', 'k', 'e', 'y')
> animal[1:3]
[1] "m" "o" "n"
> animal[4:6]
[1] "k" "e" "y"
```
2. Answer the questions:
  - If the first four characters are selected using the slice animal[1:4] how can we obtain the first for characters in reverse order?
```
> animal[4:1]
[1] "k" "n" "o" "m"
```
  - What is `animal[-1]`? What is `animal[-4]`? Given those answers, explain what `animal[-1:-4]` does.
```
> animal[-1]
[1] "o" "n" "k" "e" "y"
# same vector without first element
> animal[-4]
[1] "m" "o" "n" "e" "y"
# same vector without fourth element
> animal[-1:-4]
[1] "e" "y"
# vector without elements from 1 to 4
```
  - Use a slice of animal to create new character vector that spells the word "eon", i.e. `c("e", "o", "n")`.
```
> c(animal[5], animal[2], animal[3])
[1] "e" "o" "n"
```
3. Donwload, extract and then read the .csv file into "dat" variable from file inflammation-01.csv.zip
```
> download.file('http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/inflammation-01.csv.zip', 'inflammation-01.csv.zip')
próbowanie adresu URL 'http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/inflammation-01.csv.zip'
Content type 'application/zip' length 2282 bytes
==================================================
downloaded 2282 bytes

> unzip('inflammation-01.csv.zip')

> dat <- read.csv(file='./inflammation-01.csv', header=FALSE)
> head(dat)
  V1 V2 V3 V4 V5 V6 V7 V8 V9 V10 V11 V12 V13 V14 V15 V16 V17 V18 V19 V20 V21
1  0  0  1  3  1  2  4  7  8   3   3   3  10   5   7   4   7   7  12  18   6
2  0  1  2  1  2  1  3  2  2   6  10  11   5   9   4   4   7  16   8   6  18
3  0  1  1  3  3  2  6  2  5   9   5   7   4   5   4  15   5  11   9  10  19
4  0  0  2  0  4  2  2  1  6   7  10   7   9  13   8   8  15  10  10   7  17
5  0  1  1  3  3  1  3  5  2   4   4   7   6   5   3  10   8  10   6  17   9
6  0  0  1  2  2  4  2  1  6   4   7   6   6   9   9  15   4  16  18  12  12
  V22 V23 V24 V25 V26 V27 V28 V29 V30 V31 V32 V33 V34 V35 V36 V37 V38 V39 V40
1  13  11  11   7   7   4   6   8   8   4   4   5   7   3   4   2   3   0   0
2   4  12   5  12   7  11   5  11   3   3   5   4   4   5   5   1   1   0   1
3  14  12  17   7  12  11   7   4   2  10   5   4   2   2   3   2   2   1   1
4   4   4   7   6  15   6   4   9  11   3   5   6   3   3   4   2   3   2   1
5  14   9   7  13   9  12   6   7   7   9   6   3   2   2   4   2   0   1   1
6   5  18   9   5   3  10   3  12   7   8   4   7   3   5   4   4   3   2   1
```
4. Check what type and shape of thing "dat" is (use `class()` and `dim()` functions).
```
> class(dat)
[1] "data.frame"
> dim(dat)
[1] 60 40
```
5. Pick column 10 and 20 from rows 1, 3, 5.
```
> dat[c(1,3,5), c(10,20)]
  V10 V20
1   3  18
3   9  10
5   4  17
```
6. Select the first 10 columns of values for the first four rows.
```
> dat[1:4, 1:10]
  V1 V2 V3 V4 V5 V6 V7 V8 V9 V10
1  0  0  1  3  1  2  4  7  8   3
2  0  1  2  1  2  1  3  2  2   6
3  0  1  1  3  3  2  6  2  5   9
4  0  0  2  0  4  2  2  1  6   7
```
7. Select the first 10 columns of rows 5 to 10
```
> dat[5:10, 1:10]
   V1 V2 V3 V4 V5 V6 V7 V8 V9 V10
5   0  1  1  3  3  1  3  5  2   4
6   0  0  1  2  2  4  2  1  6   4
7   0  0  2  2  4  2  2  5  5   8
8   0  0  1  2  3  1  2  3  5   3
9   0  0  0  3  1  5  6  5  5   8
10  0  1  1  2  1  3  5  3  5   8
```
8. Select all rows from column 16-18.
```
> dat[, 16:18]
   V16 V17 V18
1    4   7   7
2    4   7  16
3   15   5  11
4    8  15  10
...
```
9. Check the maximum inflammation value for patient 1 and patient 2. Then check the minimum inflammation on day 7.
```
> patient_1 = dat[1, ]
> max(patient_1)
[1] 18
> max(dat[2,])
[1] 18
> min(dat[,7])
[1] 1
```

# Part 4 - Control structures
1. Analyze how this `for loop` works:
2. Analyze how this `while loop` works:
3. Analyze how below repeat loop works. Pay attention to the `if-else`, `next` and `break` structures.

# Part 5 - Exercise
1. Suppose you want to determine the maximum inflammation for patient 5 across days three to seven. To do this you would extract the relevant subset from the data frame and calculate the maximum value. Which of the following lines of R code gives the correct answer?
  - `max(dat[5,])`
  - `max(dat[3:7, 5])`
  - `max(dat[5, 3:7])`
  - `max(dat[5, 3, 7])`
2. Using the inflammation data frame "dat" from above: Let's pretend there was somethig wrong with the instrument on the first five days for every second patient (#2, 4, 6, etc.), which resulted in the measurements being twice as large as they should be.
  - Write a vector containing each affected patient (hint: ? seq)
  - Create a new data frame with in which you halve the first five days' values in only those patients
  - Print out the corrected data frame to check that your code has fixed the problem
