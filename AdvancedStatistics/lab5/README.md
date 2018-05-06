

# Lab 5: linear regresion

1. Preparing the data
  - Run RStudio - **YEP**
```
17:34:45 evemorgen@Patryks-MacBook-Pro-2.local ~ R

R version 3.4.3 (2017-11-30) -- "Kite-Eating Tree"
Copyright (C) 2017 The R Foundation for Statistical Computing
Platform: x86_64-apple-darwin17.3.0 (64-bit)
```
  - Set your Working Directory using the setwd() command. - **YEP**
```
> setwd(dir="~/Dropbox/studia/1yearSMADA/AdvancedStatistics/lab5/")
```

  - Download, extract and then load the data from the file krakow-kurdwanow.zip. The data comes from the monthly reports from 2015 from the Kraków-Kurdwanów station (source: http://monitoring.krakow.pios.gov.pl/).
```
> download.file("http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/krakow-kurdwanow.zip", "krakow-kurdwanow.zip")
próbowanie adresu URL 'http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/krakow-kurdwanow.zip'
Content type 'application/zip' length 5525 bytes
==================================================
downloaded 5525 bytes

> unzip("krakow-kurdwanow.zip")
> data <- dget("./krakow-kurdwanow")
> data
     SO2 NO2 NOx  NO O3 O38h PM10  PM25       date
1   15.5  23  33   7 23   35   73  15.5 2015-01-01
2   12.3  27  55  18 22   38   57  12.3 2015-01-02
```

2. Linear regression
  - Create y and x vectors. Assign corresponding data from columns: data$PM25 and data$PM10.
  - Create y and x vectors. Assign corresponding data from columns: data$PM25 and data$PM10.
```
y <- data$PM25
x <- data$P
> y <- data$PM25
BŁĄD: nieoczekiwane ';' in ";"
> x <- data$PM10
> y
  [1]  15.5  12.3   5.8   5.2   9.3   8.5  21.5  18.1   6.2   5.0   4.5   5.2
 [13]   6.4  10.0   9.5  12.8   6.7   4.6   2.8   4.5   7.5   3.7   5.1   4.2
> x
  [1]  73  57  22  16  32  42 120  70  14  12  16  15  40  61  74 145  58  36
 [19]  35  43  73  40  33  32  47  79  72  44  38  35  24  82 166  68  87  58
```
  - Delete missing data from vectors. If there is no data in the vector y, also delete the corresponding data from the vector x. Similarly, if the vector x is missing data, also delete the corresponding data from the vector y.
```
> good <- complete.cases(x,y)
> y <- y[good]
> x <- x[good]
> good
  [1]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
 [13]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
```
  - Calculate correlation - find out how variables depend on each other linearly.
```
> n <- length(x)
> l <- (n*sum(x*y)-sum(x)*sum(y))
> m <- sqrt((n*sum(x^2) - sum(x)^2) * (n*sum(y^2) - sum(y)^2))
> 1/m
[1] 8.405464e-09
```
  - Use the cor() function to calculate correlations.
```
> cor(x,y)
[1] 0.913628
```

  - Centralize the random variable.
```
> ymean <- mean(y)
> xmean <- mean(x)
> y <- y - ymean
> x <- x - xmean
> x
  [1]  27.6391185  11.6391185 -23.3608815 -29.3608815 -13.3608815  -3.3608815
  [7]  74.6391185  24.6391185 -31.3608815 -33.3608815 -29.3608815 -30.3608815
```

  - Make sure the centralization is done correctly.
```
> mean(y)
[1] 9.478185e-16
> mean(x)
[1] 1.49278e-15
```
  - Create a function that would count the sum of the squares "vertical"distances between the points of the straight line y = ax for a given “a” argument. The function should have the following arguments:
    - y-coordinate of the data (vector)
    - x-coordinate of the data (vector)
    - Parameter a of straight line y = ax, for which the sum of squares is calculated.
```
```

  - Create a function that will select “a” parameter from the given vector of “a” parameters (a_vector) for which the sum of squares is the smallest. The function should have the following arguments:
    - y-coordinate of the data (vector)
    - x-coordinate of the data (vector)
    - Vector a parameters (a_vector).
