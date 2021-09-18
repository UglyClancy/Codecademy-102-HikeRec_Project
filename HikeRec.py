from Hike import hikes
from Locations import h_locations
from Locations import h_directions
from HikeQueue import Queue

# hike_string = ""
# for location, hikes in h_locations.items(): 
#     for hike in hikes.values():
#         hike_string += "{0} - {1}\n".format(location, hike)
# print(hike_string)

def reccomendation_queue_direction():
    d_queue = Queue()
    print("Which area of Arizona would you like to hike today?")
    direction_input = input()
    # if direction_input == "North":
    if direction_input in h_directions.keys():
        towns = h_directions[direction_input]
        print("Your hike choices include: ")
        for town in towns:
            d_queue.enqueue(town)
    else:
        print("Your choice must be North, South, East, or West.")
        return reccomendation_queue_direction()
    return 
   

    

print(reccomendation_queue_direction())