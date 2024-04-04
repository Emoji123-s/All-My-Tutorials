"""
Union : 
                set1 = {1, 2, 3, 4, 5}
                set2 = {4, 5, 6, 10, 11}

                set1 U set2 = {1, 2, 3, 4, 5, 6, 10, 11}
Union merges a set together, and if the sets contain duplicates, only one of them would be written

Intersection : 
                set1 = {1, 2, 3, 4, 5}
                set2 = {4, 5, 6, 10, 11}
                     
                set1 (upside-down U) set2 = {4, 5}
Intersection picks out the common items of a set only


"""

set1 = {"Divine", "Damien", "Dracula", "Jenny"}
set2 = {"Jenny", "Jiya", "Aakash"}
set3 = {"Wisdom", "Hilda", "Prosper", "Providence"}
set4 = {"Kelly", "Judith", "Wale", "Providence"}
set5 = {"Samantha", "Erwin", "Martha", "Agatha", "Kelly", "Judith"}

# Union
print(set1.union(set2)) # This invokes the union method on one set, and the second will be passed as an argument
print(set1.union(set2, set3)) # Works on multiple sets. With this method, any argument can be passed to it, whether or not it is a set, but a set has to be called first i.e
print(set1.union(("Devi", "Bridget")))

# Or with an operator
print(set1 | set2)
print(set1 | set2 | set3) # Works on multiple set. With this, only sets can be used. Any other thing returns a typeerror.

# Union Update
(set1.update(set2)) # This adds the elements of set2 to set1, but not with the same elements present in both of them. 
print(set1) # Because we are updating set1

# Also
set1 |= set2
print(set1)


# Intersection
print(set3.intersection(set4))
print(set3.intersection(set4, set5))

# With an operator
print(set3 & set4)

# Intersection update
set3.intersection_update(set4)
print(set3)

# With an operator
set3 &= set4
print(set3)

"""
Difference : 
                set1 = {1, 2, 3, 4, 5}
                set2 = {4, 5, 6, 10, 11}

                set1 - set2 = {1, 2, 3}
Difference picks out items present in set1 that are not present in set2

Symmetric Difference : 
                set1 = {1, 2, 3, 4, 5}
                set2 = {4, 5, 6, 10, 11}

                (set1 U set2) - (set1 (upside-down U) set2) = {1, 2, 3, 6, 10, 11} 
Symmetric Difference picks out elements which are present in set1 and set2 but not in both
"""
set6 = {"Divine", "Damien", "Dracula", "Jenny"}
set7 = {"Jenny", "Jiya", "Aakash"}
set8 = {"Wisdom", "Hilda", "Prosper", "Providence"}
set9 = {"Kelly", "Judith", "Wale", "Providence"}
set10 = {"Samantha", "Erwin", "Martha", "Agatha", "Kelly", "Judith"}

# Difference
print(set6.difference(set7))

# With an operator
print(set6 - set7)

# Difference Update
set6.difference_update(set7)
print(set6)

# Symmetric Difference
print(set8.symmetric_difference(set9)) # You can't perform symmetric difference on multiple sets

# With an operator
print(set8 ^ set9) # Here, you can apply it to multiple sets
print(set8 ^ set9 ^ set10)

# Symmetric Difference Update
set8.symmetric_difference_update(set9)
print(set8)

"""
Disjoint Set : They are sets that have nothing in common.Basically if their intersection has nothing in common
                    set1 = {1, 2, 3, 4, 5}
                    set2 = {4, 5, 6, 10, 11}

                    set1.isdisjoint(set2) = Returns True or False
There is no operator for this


Subset : This happens if every element of set1 is in set2
                    set1 = {1, 2, 3, 4, 5}
                    set2 = {4, 5, 6, 10, 11}

                    set1.issubset(set2) = Returns True or False
                    set1 <= set2 = Returns True or False

Superset : It is the reverse of set2. It happens if set1 contains every element of set2.
                    set1 = {1, 2, 3, 4, 5}
                    set2 = {4, 5, 6, 10, 11}

                    set1.issuperset(set2) = Returns True or False
                    set1 >= set2 = Returns True or False
"""

set11 = {"Divine", "Damien", "Dracula", "Jenny"}
set12 = {"Jenny", "Jiya", "Aakash"}
set13 = {"Wisdom", "Hilda", "Prosper", "Providence"}
set14 = {"Kelly", "Judith", "Wale", "Providence"}
set15 = {"Samantha", "Erwin", "Martha", "Agatha", "Kelly", "Judith"}

# Disjoint
print(set11.isdisjoint(set12))

# Subset
print(set13.issubset(set14))

# With an operator
print(set13 <= set14)

# Superset
print(set14.issuperset(set15))
print(set14 >= set14)