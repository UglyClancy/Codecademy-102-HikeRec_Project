from Hike import hikes
from Locations import h_locations
from Locations import h_directions
from MyQueue import Queue

# hike_string = ""
# for location, hikes in h_locations.items(): 
#     for hike in hikes.values():
#         hike_string += "{0} - {1}\n".format(location, hike)
# print(hike_string)

def reccomendation_queue_direction():
    print("Which area of Arizona would you like to hike today?")
    direction_choice = input()
    if direction_choice == "north":
        pass
    

reccomendation_queue_direction()