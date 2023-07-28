#print("I apologise; I need to be better")

arr_naruto_heroes = ['Naruto', 'Sasuke', 'Raikage', 'Hokage', 'Gai']
arr_onepiece_heroes = ['Luffy', 'Blackbeard', 'Red Shanks', 'Garp', 'Oden']
arr_bleach_heroes = ['Ichigo', 'Iruka', 'Gin', 'Chad', 'Inoue']
arr_deathnote_heroes = ['Light', 'Ryokuza', 'Near', 'Mello', 'Ryuk'] 

print(" ")
for hero in arr_naruto_heroes:
    print(f"{arr_naruto_heroes.index(hero) + 1}. {hero}")

print(" ")

(" ")
for i, hero in enumerate(arr_onepiece_heroes, 1):
    print(f"{i}. {hero}")

print(" ")

print(" ")
for i in range(len(arr_bleach_heroes)):
    print(f"{i+1}. {arr_bleach_heroes[i]}")

print(" ")

i = 0 
print(" ")
for hero in arr_deathnote_heroes:
    print(f"{i+1}. {arr_deathnote_heroes[i]}")
    i += 1 

print(" ")



