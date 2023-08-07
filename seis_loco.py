#6 loco

number_of_players = input("How many partners do you have? ")
number_of_players = int(number_of_players)

while number_of_players % 4 != 0:
    number_of_players = number_of_players - 1

