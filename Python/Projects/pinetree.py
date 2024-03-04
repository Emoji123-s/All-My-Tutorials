"""
Create a pine tree with the hash symbol(#) based on user's input on the number of rows.
Ask the user for the number of rows
Output: 
    #
   ###
  #####
 #######
#########
    #

Use 1 while loop, and 3 for loops

# 4 spaces, 1 hash
# 3 spaces, 3 hashes
# 2 spaces, 5 hashes
# 1 space, 7 hashes
# 0 spaces, 9 hashes
# Since the first row is equal to the last, we would need to save the number

# Decrement spaces by 1 each time through the loop
# Increment the hashes by 2 each time through the loop
# save spaces to the stump by calculating tree height -1
# Decrement from tree height until it equals 0
# print spaces and hashes for each row
# Print stump spaces and one hash
"""