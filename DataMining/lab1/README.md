# Lab 1

Lab 1 is about getting familiar (again) with R data types/structures with following exercises:


```
> factor(c('black', 'just-black', 'not-pink', 'black-ish'))
[1] black      just-black not-pink   black-ish
Levels: black black-ish just-black not-pink
> as.list(factor(c('black', 'just-black', 'not-pink', 'black-ish')))
[[1]]
[1] black
Levels: black black-ish just-black not-pink

[[2]]
[1] just-black
Levels: black black-ish just-black not-pink

[[3]]
[1] not-pink
Levels: black black-ish just-black not-pink

[[4]]
[1] black-ish
Levels: black black-ish just-black not-pink
```
