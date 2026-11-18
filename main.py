import data



temperatures = [12, 18, 30, 48, 72]

print(temperatures)
print(len(temperatures))

cities = ["Gothenburg", "Los Angeles", "Madrid", "London", "Berlin"] 
print(cities)
print(len(cities))



my_interests = ["Technology", "Cars", "Football", "Food", "Travel"]

print(my_interests)
print(len(my_interests))



print(my_interests[0])
print(my_interests[2])
print(my_interests[-1])


temperatures = data.get_temperatures()
print(temperatures)

cities = data.get_cities()
print(cities)

games = data.get_games()
print(games)
print(len(games))


shopping_list = data.get_shopping_list()
print(shopping_list)