/****************************************************************************************************************/
/* In-Class Exercises                                                                                           */
/****************************************************************************************************************/
/* 1. create an array called "fruits" and assign the values "Strawberry", "Raspberry", and "Apple" to it         */
// add code here
let fruits = [];
fruits  = ["Strawberry", "Raspberry", "Apple"];

console.log(fruits);
/* 2. add two more fruits to the "fruits" array using the correct array method                                   */
// add code here
fruits.push("Banana");
fruits.push("Watermelon");
/* 3. sort the fruits array alphabetically using the correct array method                                        */
// add code here
console.log(fruits.sort());
/* 4. create a function called printFruit that prints each item in the fruits array to the console              */
/*    and call the printFruit function                                                                          */
// add code here
function printFruits() {
    for (let i = 0; i < fruits.length; i++) { 
        console.log(fruits[i]);
    }
}
printFruits();
/* 5. create a fruit class that has three properties: name, color, and season and one method: printFruit()      */
/*    that prints all three properties of the fruit to the console. Then, create 3 fruit objects and print      */
/*    them using the printFruit() method             
// add code here
/****************************************************************************************************************/

class Fruit {
    constructor(name, color, season) {
        this.name = name,
        this.color = color,
        this.season = season
    }
    printFruits() {
        console.log("Name: " + this.name + ", Color: " + this.color + ", Season: " + this.season);
    }
 }

 const apple = new Fruit("Apple", "Red", "Fall");
 const mango = new Fruit("Mango", "Yellow", "Summer");
 const kiwi = new Fruit("Kiwi", "Green", "Spring");

 apple.printFruits();
 mango.printFruits();
 kiwi.printFruits();

/* In-Class Lab                                                                                                 */
/****************************************************************************************************************/
/* 1. Write a function that asks the user if they want to say hi. If the user selects "Okay" (true), then       */
/*    display a welcome message. If the user selects "Cancel" (false), then display a different message         */
function areYouSure() {
    let text = "Do you want to say hi?";
    if (confirm(text) === true) {
        text = "Welcome to Lab 8!";
    } else {
        text = "Rude!";
    }
    document.getElementById("welcome").innerHTML = text;
}

/* 2. Write a function to change 3 styles on the webpage                                                        */
function changeStyle() {
    document.getElementById("welcome").style.color = "red";
    document.getElementById("button1").style.backgroundColor = "green";
    document.getElementById("button2").style.width = "500px";
    document.getElementById("welcome").innerHTML = "8 Lab to Welcome!";
}
