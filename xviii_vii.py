#print("I apologise; I need to be better")

arr_naruto_heroes = ['Naruto', 'Sasuke', 'Raikage', 'Hokage', 'Gai']
arr_onepiece_heroes = ['Luffy', 'Blackbeard', 'Red Shanks', 'Garp', 'Oden']
arr_bleach_heroes = ['Ichigo', 'Iruka', 'Gin', 'Chad', 'Inoue']
arr_deathnote_heroes = ['Light', 'Ryokuza', 'Near', 'Mello', 'Ryuk'] 
arr_fma_heroes = ['Edward', 'Alphonse', 'Mustang', 'Homonculus', 'Armstrong']

#Running a single for loop an on array and also using the index location information: my way
print(" ")
for hero in arr_naruto_heroes:
    print(f"{arr_naruto_heroes.index(hero) + 1}. {hero}")
print(" ")

#Running a single for loop on an array and also using the index location information: enumerate() 
print(" ")
for i, hero in enumerate(arr_onepiece_heroes, 1):
    print(f"{i}. {hero}")
print(" ")

#Running a single for loop on an array and also using the index location information: range(len(arr))
print(" ")
for i in range(len(arr_bleach_heroes)):
    print(f"{i+1}. {arr_bleach_heroes[i]}")
print(" ")

#Running a single for loop on an array and also using the index location information: loop counter with counter outside of for loop and the increment at the base of the for loop 
i = 0 
print(" ")
for hero in arr_deathnote_heroes:
    print(f"{i+1}. {arr_deathnote_heroes[i]}")
    i += 1 
print(" ")

i = 1 
print(" ")
for hero in arr_fma_heroes:
    print(f"{i}. {hero}")
    i += 1
print(" ")


