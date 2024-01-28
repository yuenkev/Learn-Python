class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name +  " menu available from " + str(self.start_time) + " to " + str(self.end_time)

  # Task 9 - Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items.
  def calculate_bill(self, purchased_items):
    total = 0
    
    for items in purchased_items:
      total += self.items[items]
    
    return total
      
# Task 3-6 - Create 4 Menu objects
brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 1100, 1600)

early_bird = Menu("early_bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 1100, 1800)

dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 1700, 2300)

kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1100, 2100)

print(brunch)

#10 - Test out Menu.calculate_bill()
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

#11 
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


#12 - Create Franchise class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #15 - String representation so that we’ll be able to tell them apart
  def __repr__(self):
    return self.address

  # 16 - .available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time.
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

flagship_store = Franchise( "1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store)

print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))


class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#21 - Let’s create our first Business
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#22 
arepas_menu = Menu("arepas", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepa = Business("Take a' Arepa", [arepas_place])

