letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#1 - Building a dict of the combined lists
letter_to_points = {k:v for k, v in zip(letters, points)}

print(letter_to_points)

#2 - Add in blank title key - " "
letter_to_points[" "] = 0

print(letter_to_points)

#3/4 - Function that will tkae in a word and return ho wmany points

def score_word(word):
  print_total = 0

  #5 - loop that goes throught letters and adds at the total points for each letter
  for w in word.upper():
    print_total += letter_to_points.get(w, 0)

  return print_total

#7 - Testing if the funciton words
brownie_points = score_word("BROWNIE")

print(brownie_points)


#9 - Create a dictionary that maps a list of words they have played
player_to_words = {"player1" : ["BLUE", "TENNIS", "EXIT"], "wordNerd" : ["EARTH", "EYES", "MACHINE"], "Lexi Con" : ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

#10 - empty dict
player_to_points = {}

#11 - Add to the new dict the player and their total points
for player, words in player_to_words.items():
  player_points = 0
  for w in words:
      player_points += score_word(w)
  player_to_points[player] = player_points

print(player_to_points)