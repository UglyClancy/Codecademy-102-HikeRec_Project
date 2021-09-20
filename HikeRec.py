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
    if direction_input in h_directions.keys():
        towns = h_directions[direction_input]
        print("Your hike choices include: ")
        for town in towns:
            d_queue.enqueue(town)
    else:
        print("Your choice must be North, South, East, or West.")
        return reccomendation_queue_direction()

t_queue = Queue()

def rec_queue_town():
    print("Which town would you like to hike near?")
    town_input = input()
    if town_input in h_locations.keys():
        towns = h_locations[town_input]
        print("Your hike choices include: ")
        for hike in towns:
            t_queue.enqueue(hike)
    else:
        print("Your choice must be one of the previously displayed locations.")
        return rec_queue_town()

def rec_queue_hike_diff():
    print("What kind of hike are you looking for: easy, moderate, or hard?")
    diff_input = input()
    h_queue = Queue()
    if not t_queue:
        print("No hikes found in the are that are " + diff_input)
    while t_queue:
        if hikes.keys() in t_queue:
            pass

    # if diff_input not in hikes.values():
    #     return True
        # t_queue.pop()
    # else:
    #     return False
        # print("Your choice must be one of the previously displayed locations.")
        # return rec_queue_hike_diff()


print(reccomendation_queue_direction())
print(rec_queue_town())
print(rec_queue_hike_diff())