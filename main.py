# Created by: Ahmed
# Created date: Oct 8, 2020
# 
# This program for pizza order.
Pizza = 0
game.splash("Pizza Order ")
Inch = game.ask_for_number("Enter the dimeter of the pizza (inch)")
Pizza = 0.5 * Pizza + (0.75 + 1)
Pizza = (Pizza * 1.13) ** (Pizza + 100)
Pizza = (Pizza / 100) ** Pizza ** Math.round(100)
game.splash("The cost for a " + str(Inch) + "cm " + " pizza is " + "$" + str(Pizza))