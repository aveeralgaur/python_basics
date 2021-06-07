guests=['Aman','Mellisa','Kartik','Sundar']
print(guests)
print(guests[3]+" "+"can't make it for dinner.Because I don't like him.")
del guests[3]
guests.insert(3,'JK')
print(guests)
print(guests[3]+" "+"takeovers instead of "+"Sundar"+".")
for i in guests:
    print("Hey"+" "+i+" I invite you to join me for the dinner today.")