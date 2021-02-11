# numbers is a list.
#numbers.append()
#numbers.insert(place, number)
#numbers.remove(number)
#numbers.clear()
#numbers.pop()
#numbers.index():: The index of the number is printed.
#numbers.count():: Counts the number every particular time it arrives.
#numbers.sort()
#numbers.reverse()
#numbers.copy()
#Write a program to remove the duplicates in a list.
numbers=[2,3,2,5,6,5,3,7,8,0,1,1,8]
numbers.sort()
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

