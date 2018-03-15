

TOC:
  - [PDF with lab content](lab2.pdf)


Solutions:
3. Download data
```
> download.file("http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/car-speeds.csv.zip", "car-speeds.csv.zip")
próbowanie adresu URL 'http://home.agh.edu.pl/~mmd/_media/dydaktyka/as-is/car-speeds.csv.zip'
Content type 'application/zip' length 971 bytes
==================================================
downloaded 971 bytes

> unzip("./car-speeds.csv.zip")

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

5. 
```
> carSpeeds <- read.csv(file='./car-speeds.csv', stringsAsFactors=FALSE)
> head(carSpeeds)
  Color Speed     State
1  Blue    32 NewMexico
2   Red    45   Arizona
3  Blue    35  Colorado
4 White    34   Arizona
5   Red    25   Arizona
6  Blue    41   Arizona
```
6. Use the as.is argument to import colors of cars as strings and names of states as factors
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
> carSpeeds$Color <- ifelse(carSpeeds$State=='Arizona', 'Ohio', carSpeeds$State)
> carSpeeds$State
  [1] NewMexico Arizona   Colorado  Arizona   Arizona   Arizona   NewMexico
  [8] Colorado  Arizona   Colorado  Utah      Utah      Utah      Utah
 [15] Utah      NewMexico Arizona   NewMexico Arizona   Utah      Utah
 [22] Utah      NewMexico Colorado  Colorado  NewMexico Colorado  Utah
 [29] Colorado  Utah      NewMexico Colorado  Colorado  Utah      Colorado
 [36] Colorado  NewMexico Arizona   Utah      Colorado  Colorado  NewMexico
 [43] Arizona   Utah      Arizona   Colorado  NewMexico NewMexico NewMexico
 [50] Colorado  Arizona   Utah      Utah      Arizona   NewMexico Colorado
 [57] Utah      Colorado  Utah      Utah      Utah      Colorado  NewMexico
 [64] Colorado  NewMexico Colorado  NewMexico Arizona   NewMexico Utah
 [71] Utah      Colorado  Arizona   Utah      Colorado  Colorado  Colorado
 [78] Arizona   NewMexico Arizona   Utah      Colorado  Colorado  Arizona
 [85] Arizona   Arizona   Utah      Arizona   Utah      Utah      Utah
 [92] Arizona   Arizona   NewMexico Colorado  Colorado  Utah      NewMexico
 [99] Arizona   Utah
Levels: Arizona Colorado NewMexico Utah
```
7. wtf?
```
> unique(carSpeeds$Color)
[1] "3"    "Ohio" "2"    "4"
```

8. 
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
```

9.
```
write.csv(carSpeeds, file=``)
```


