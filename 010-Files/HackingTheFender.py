import csv
import json

#2 creata new list of comprised users
compromised_users = []

#3 open up the file
with open('passwords.csv') as password_file:
    
    # Step 4: Pass the file object to CSV reader and save as password_csv
    password_csv = csv.DictReader(password_file)
    
    # Step 5: Iterate through each row in password_csv
    for password_row in password_csv:
        # Step #7 - Append compromised users to the list
        compromised_users.append(password_row['Username'])
        # print(password_row['Username'])

# Step 8-10 - Write the username of each compromised_user in compromised_users to compromised_user_file.
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user + '\n')

#Step 13-15 - open a new json, create a dict, and write out boss_message_dict to boss_message using json.dump()
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message":"Mission Success"}
  json.dump(boss_message_dict, boss_message)



