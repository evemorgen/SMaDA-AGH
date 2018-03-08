var int: fruit;
var int: fries;
var int: salad;
var int: wings;
var int: sticks;
var int: sampler;

constraint fruit >= 0;
constraint fries >= 0;
constraint salad >= 0;
constraint wings >= 0;
constraint sticks >= 0;
constraint sampler >= 0;

constraint fruit*215 + fries*275 + salad*335 + wings*355 + sticks*420 + sampler*580 == 1505;

solve satisfy;

output ["fruit:", show(fruit), "\t fries:", show(fries), 
        "\t salad:", show(salad), "\t wings:", show(wings),
        "\t sticks:", show(sticks), "\t sampler:", show(sampler)];