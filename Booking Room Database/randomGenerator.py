#random-generator for database
import random

room_types = {"Meeting Room": 10, 
            "Conference Room": 50, 
            "Study Room": 8, 
            "Recreation room": 10,
            }

for counter in range(1, 41):
    #price range
    # print(random.randrange(10, 30))

    #capacity
    # print(random.randrange(5, 20, 5))

    #discount 
    print(random.randrange(5, 20, 5))



