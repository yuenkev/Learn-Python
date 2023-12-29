hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

#Add the sum of the prices
for p in prices:
  total_price += p

print(total_price)

#Find the average price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

#Cut prices by $5
new_prices = [p - 5 for p in prices]

print(new_prices)

#get total revenue 
total_revenue = 0

#Add the total revenue to the variable
for i in range(0,len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])

print("Total Revenue: " + str(total_revenue))

#average daily revenue 
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

#new list comprehension list for cuts under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)

