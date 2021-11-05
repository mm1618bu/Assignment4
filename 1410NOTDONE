#! /usr/bin/python3

# I am importing the random function to help pick states. I am also making a dictionary with states as the key and the capitol as the value.
import random
states = {
    "Alabama" : "Montgomery",
    "Alaska" : "Juneau",
    "Arizona":"Phoenix",
    "Arkansas":"Little Rock",
    "California":"Sacramento",
    "Colorado":"Denver",
    "Conneticut":"Hartford",
    "Delaware":"Dover",
    "Florida":"Talahassee",
    "Georgia":"Atlanta",
    "Hawaii":"Honolulu",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Indiana":"Indianapolis",
    "Iowa":"Des Moines",
    "Kansas":"Topeka",
    "Kentucky":"Frankfort",
    "Louisiana":"Baton Rouge",
    "Maine":"Augusta",
    "Maryland":"Annapolis",
    "Massachusetts":"Boston",
    "Michigan":"Lansing",
    "Minnesota":"Saint Paul",
    "Mississippi":"Jackson",
    "Missouri":"Jefferson City",
    "Montana":"Helena",
    "Nebraska":"Lincoln",
    "Nevada":"Carson City",
    "New Hampshire":"Concord",
    "New Jersey":"Trenton",
    "New Mexico":"Santa Fe",
    "New York":"Albany",
    "North Carolina":"Raleigh",
    "North Dakota":"Bismarck",
    "Ohio":"Columbus",
    "Oklahoma":"Oklahoma City",
    "Oregon":"Salem",
    "Pennsylvania":"Harrisburg",
    "Rhode Island":"Providence",
    "South Carolina":"Columbia",
    "South Dakota":"Pierre",
    "Tennessee":"Nashville",
    "Texas":"Austin",
    "Utah":"Salt Lake City",
    "Vermont":"Montpelier",
    "Virginia":"Richmond",
    "Washington":"Olympia",
    "West Virginia":"Charleston",
    "Wisconsin":"Madison",
    "Wyoming":"Cheyenne"
}

States=list(states.keys()) # I am storing all of the captiols in a list

point=0 # Setting the score to zero
for i in range(50):
    state=random.choice(States) # selecting all states at random
    capital = states[state]
    user_guess = input('what is the capital of %s?'%state )
    if user_guess.lower() == 'exit':  #if a user type in exit, the game exits
        break
    elif user_guess.title() == capital:
        point+=1
        print('Right! Your score is %d' %point)
    else:
        print('Wrong. The capital of {} is {}.'.format(state,capital))
print('Your final score is %d.' %point)

