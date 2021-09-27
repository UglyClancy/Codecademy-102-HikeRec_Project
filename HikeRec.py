from Hike import hikes
from Locations import h_locations
from Locations import h_directions
from MyGraphSearch import bfs
from MyGraphSearch import dfs
import math

# Greeting / Options start
direction_string = ""
for directions in h_directions.keys():
    direction_string += "{0}\n".format(directions)

def greeting():
    print("Welcome to Hiking Arizona!")
    print("We'll recommend some of our favorite places and trails for you today.")
    print("First let's start with a direction: \n" + direction_string)

def hike_rec():
    greeting()

# Search helper functions
def get_direction(): 
    direction_input = input("What area of Arizona would you like to hike in?")
    if h_directions[direction_input]:
        direction_choice = h_directions[direction_input]
        return direction_choice
    elif direction_input == "Weast":
        print("Mayonnaise is not an instrument.")
        get_direction()
    else:
        print("Unfortunately, that's not a direction, please choose from North, South, East, or West.")
        get_direction()
        # else and elif returning KeyError

town_string = ""
for towns in h_locations.keys():
    town_string += "{0}\n".format(towns)

hike_matches = []

def get_location():
    location_input = input("What town or city will you travel to?")
    if h_locations[location_input]:
        location_choice = h_locations[location_input]
        for hike in location_choice:
            print(hike + "\n")
            for hike2 in hikes.keys():
                if hike == hike2:
                    hike_matches.append(hike)
        # return hike_matches
    else:
        print("Sorry, that's not a location provided, please choose from the listed options: " + town_string)
        get_location()

hikes_with_values = []

def difficulty_list():
    for hike_item in hikes.items():
        if hike_item[0] in hike_matches:
            hikes_with_values.append(hike_item)

result_hikes = []

def get_difficulty():
    difficulty_input = input("How hard would you like to push yourself today?")
    for hike_diff in hikes_with_values:
        if difficulty_input == hike_diff[1][1]:
            result_hikes.append(hike_diff)
    # return result_hikes


        
def get_length():
    miles_input = int(input("How far would you like to hike? Enter 1-5, 5-10, 10-20, 21+"))
    chosen_hikes = []
    range_1 = range(6)
    range_2 = range(6, 11)
    range_3 = range(10, 21)
    range_4 = range(21, 101)
    if miles_input in range_1:
        for hike_m in result_hikes:
            if math.floor(hike_m[1][0]) in range_1:
                chosen_hikes.append(hike_m)
    elif miles_input in range_2:
        for hike_m in result_hikes:
            if math.floor(hike_m[1][0]) in range_2:
                chosen_hikes.append(hike_m)
    elif miles_input in range_3:
        for hike_m in result_hikes:
            if math.floor(hike_m[1][0]) in range_3:
                chosen_hikes.append(hike_m)
    elif miles_input in range_4:
        for hike_m in result_hikes:
            if math.floor(hike_m[1][0]) in range_4:
                chosen_hikes.append(hike_m)
    return chosen_hikes
            
    


print(hike_rec())
print(get_direction())
print(get_location())
difficulty_list()
print(hikes_with_values)
print(get_difficulty())
print(result_hikes)
print(get_length())



