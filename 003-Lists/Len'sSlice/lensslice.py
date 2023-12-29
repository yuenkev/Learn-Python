# Your code below:
#Create two lists
toppings = ["pepperoni", "pineapple", "cheese" ,"sausage", "olives", "anchovies", "mushrooms"]
print(toppings)

prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)

#Print the count of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#find len of toppings 
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) +  " different kinds of pizza!")

#Create a new 2D List with toppings + prices list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

#Sort the 2D list
pizza_and_prices.sort()
print(pizza_and_prices)

#store the pricest pizza in a var 
pricisest_pizza = pizza_and_prices[-1]
print(pricisest_pizza)

#remove pricest
pizza_and_prices.pop()
print(pizza_and_prices)

#add new toppings and insert in sorted order
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

#grab 3 lowest priced pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
