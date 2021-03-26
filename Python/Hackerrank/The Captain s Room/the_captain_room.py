# Basic approach removed the those which are repeated or shared.

size_of_group = int(input())
room_number_list = input().split()

# It contains only shared rooms
shared_rooms = set()

# it contains both shared and single room
unique_rooms=set()
for room in room_number_list:
    if room not in unique_rooms:
        # add only if its unique
        unique_rooms.add(room)
    else:
        # repeated or shared room 
        shared_rooms.add(room)

# Used Set property a difference b or a-b
print((unique_rooms-shared_rooms).pop())