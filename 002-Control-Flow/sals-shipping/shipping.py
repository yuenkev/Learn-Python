weight = 41.5

#Ground Shipping
groundShippingCost = 0.0

if weight <= 2:
  groundShippingCost = (weight * 1.5) + 20
elif weight <= 6:
  groundShippingCost = (weight * 3) + 20
elif weight <= 10:
  groundShippingCost = (weight * 4) + 20
elif weight > 10:
 groundShippingCost = (weight * 4.75) + 20

print("Ground Shipping Costs: " + str(groundShippingCost))

#Premium Shipping Cost
premShippingCost = 125.00
print("Ground Shipping Premium Costs: " + str(premShippingCost))

#Drone Shipping
droneShippingCost = 0.0

if weight <= 2:
  droneShippingCost = weight * 4.5
elif weight <= 6:
  droneShippingCost =  weight * 9
elif weight <= 10:
  droneShippingCost = weight * 12
elif weight > 10:
  droneShippingCost = weight * 14.25

print("Drone Shipping Costs: " + str(droneShippingCost))
print("")

#Compare
if (groundShippingCost < droneShippingCost) and (groundShippingCost < premShippingCost):
  print("Ground Shipping is the cheapest at: " + str(groundShippingCost))
elif (droneShippingCost < groundShippingCost) and (droneShippingCost < premShippingCost):
  print("Drone Shipping is the cheapest at: " + str(droneShippingCost))
else:
  print("Premium Ground Shipping is the cheapest at: " + str(premShippingCost))
