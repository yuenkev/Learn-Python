print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 1

# Write an if statement below:

if planet == 1:
  print("Planet: Venus & Relative Gravity: 0.91")
  print("Your Weight on Venus is: " + str(weight * 0.91))
elif planet == 2:
  print("Planet: Mars & Relative Gravity: 0.38")
  print("Your Weight on Mars is: " + str(weight * 0.38))
elif planet == 3:
  print("Planet: Jupiter & Relative Gravity: 2.34")
  print("Your Weight on Jupiter is: " + str(weight * 2.34))
elif planet == 4:
  print("Planet: Saturn & Relative Gravity: 1.06")
  print("Your Weight on Saturn is: " + str(weight * 1.06))
elif planet == 5:
  print("Planet: Uranus & Relative Gravity: 0.92")
  print("Your Weight on Uranus is: " + str(weight * 0.92))
elif planet == 6:
  print("Planet: Neptune & Relative Gravity: 1.19")
  print("Your Weight on Neptune is: " + str(weight * 1.19))
else:
  print("Planet does not exist.")
