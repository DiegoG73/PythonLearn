set1 = {"Hola", 56, False}
print("This is the set 1:", set1)
#---------------------------------------------------------------
set2 = {"Hola", 25, 15.856}
print("This is the set 2:", set2)

#Union: it print all values including the repeated (but just 1)
setUnion = set1 | set2
print("This is Union:", setUnion)

#Intersection: it print only the common value
setIntersection = set1 & set2
print("This is intersection:", setIntersection)

#Difference: It takes onece and delete all the other values
setDifference1 = set1 - set2
print("This is difference 1-2:", setDifference1)
setDifference2 = set2 - set1
print("This is difference 2-1:", setDifference2)

#Symmetrical difference: 
setSd = set1 ^ set2
print("This is the symmetrical difference:", setSd)