from Hike import hikes
from Locations import h_locations
from Locations import h_directions
from MyGraphSearch import bfs
from MyGraphSearch import dfs

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

def get_location():
    location_input = input("What town or city will you travel to?")
    hike_matches = []
    if h_locations[location_input]:
        location_choice = h_locations[location_input]
        for hike in location_choice:
            print(hike + "\n")
            for hike2 in hikes.keys():
                if hike == hike2:
                    hike_matches.append(hike)
        return hike_matches
    else:
        print("Sorry, that's not a location provided, please choose from the listed options: " + town_string)
        get_location()

# Getting Hike Recommendation (minus miles and diff choice)
# def get_hike(direction_choice, location_choice):
    


print(hike_rec())
print(get_direction())
print(get_location())
