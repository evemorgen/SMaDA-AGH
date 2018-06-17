

1. Preparing the data
  - Run RStudio **YEP**
  - Set your Working Directory using the setwd() command. **YEP**

2. Calculating frequencies
  - Load dataset (this data is the number of hits (in millions) for each word on Google).
```
groups <- c(rep("blue", 17250),rep("red", 13570),rep("orange", 8820),rep("green", 15700),rep("purple", 4790))
```
  - Create the frequency table.
```
 >  groups.t1 <- table(groups)
> groups.t1
groups
  blue  green orange purple    red
 17250  15700   8820   4790  13570
```
  - Modify the frequency table by sorting the data by frequency.
```
> groups.t2 <- sort(groups.t1, decreasing = TRUE)
> groups.t2
groups
  blue  green    red orange purple
 17250  15700  13570   8820   4790
```

  - Modify the frequency table to give the proportions of total, proportions with two decimal places and percentages.
```
> prop.table(groups.t2)
groups
      blue      green        red     orange     purple
0.28687843 0.26110095 0.22567770 0.14668219 0.07966074
> round(prop.table(groups.t2), 2)
groups
  blue  green    red orange purple
  0.29   0.26   0.23   0.15   0.08
> round(prop.table(groups.t2), 2)*100
groups
  blue  green    red orange purple
    29     26     23     15      8
```

3. Calculating descriptives
  - Load dataset “cars”, but first read the description about this dataset.
```
> require("datasets")
> ?cars
> cars
   speed dist
1      4    2
2      4   10
3      7    4
4      7   22
```

  - Display the structure of the dataset.
```
> str(cars)
'data.frame':	50 obs. of  2 variables:
 $ speed: num  4 4 7 7 8 9 10 10 10 11 ...
 $ dist : num  2 10 4 22 16 10 18 26 34 17 ...
```

  - Load the data to the workspace.
```
> data(cars)
```

  - Use the summary function to calculate the summary for one variable: speed. Then use the same function to calculate the summary for entire table. Notice which descriptive statistics are automatically calculated by using this function.
```
> summary(cars$speed)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
    4.0    12.0    15.0    15.4    19.0    25.0
> summary(cars)
     speed           dist
 Min.   : 4.0   Min.   :  2.00
 1st Qu.:12.0   1st Qu.: 26.00
 Median :15.0   Median : 36.00
 Mean   :15.4   Mean   : 42.98
 3rd Qu.:19.0   3rd Qu.: 56.00
 Max.   :25.0   Max.   :120.00
```

  - Calculate the basic descriptives by using the fivenum function. What kind of descriptives are calculated now?
```
> fivenum(cars$speed)
[1]  4 12 15 19 25
```

  - Analyze how the boxplot stats works in R.
```
> boxplot.stats(cars$speed)
$stats
[1]  4 12 15 19 25

$n
[1] 50

$conf
[1] 13.43588 16.56412

$out
numeric(0)
```

  - Read about and then install the package “psych” to calculate the alternative de- scriptives. Analyze the results of using describe function. **IT REQUIRES SUDO, HOW DARE YOU R**
```
> install.packages("psych")
Instalowanie pakietu w ‘/usr/local/lib/R/3.4/site-library’
(ponieważ ‘lib’ nie jest określony)
```
