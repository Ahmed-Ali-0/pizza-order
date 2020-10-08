// Created by: Ahmed
// Created date: Oct 8, 2020
// 
// This program for pizza order.
game.splash("Pizza Order ")
let inch = game.askForNumber("Enter the dimeter of the pizza (inch)")
let pizza = 0.5 * inch + (0.75 + 1)
pizza = pizza * 1.13
pizza = Math.round(pizza * 100) / 100
game.splash("The cost for a " + inch + "cm " + "pizza is " + "$" + pizza)
