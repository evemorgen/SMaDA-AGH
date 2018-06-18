var int: fruit;
var int: fries;
var int: salad;
var int: wings;
var int: sticks;
var int: plate;

constraint fruit >= 0;
constraint fries >= 0;
constraint salad >= 0;
constraint wings >= 0;
constraint sticks >= 0;
constraint plate >= 0;

constraint fruit  * 215 +
           fries  * 275 +
           salad  * 335 +
           wings  * 355 +
           sticks * 420 +
           plate  * 580 =
           1515;
           
solve satisfy;
           
output ["Solution:\n", 
        "fruit: ", show(fruit), "\n",
        "fries: ", show(fries), "\n",
        "salad: ", show(salad), "\n",
        "wings: ", show(wings), "\n",
        "sticks: ", show(sticks), "\n",
        "plate: ", show(plate), "\n",
];

            
