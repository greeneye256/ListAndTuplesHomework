import random

# Hobby Shop

items = [[article, size] for article in ["shirt", "scarf", "glove", "hat"] for size in
         ["S", "M", "L", "XL", "XXL"]] * 20

# sell the latest article that was added to the shop
removed_item_1 = items.pop()
print("You removed " + str(removed_item_1))
print("Stock = " + str(len(items)))

# sell any item that is in the shop
items.remove(["shirt", "XL"])
print("Stock = " + str(len(items)))

# restock shop
new_items = [["jeans", "S"], ["socks", "M"]]
items.append(new_items)


# 1 Write a python code to remove an element from a tuple.

def remove_element_from_tuple(tup, index):
    if index < 0 & index > len(tup) - 1:
        print("Wrong index")
        return tup
    else:
        return tup[:index] + tup[index + 1:]


# Example
tuple_length = random.randint(3, 10)
my_tuple = tuple([random.randint(0, 100) for x in range(tuple_length)])
print("Original tuple")
print(my_tuple)
random_index = random.randint(0, tuple_length - 1)
print(random_index)
print("Element to be removed: " + str(my_tuple[random_index]))
print("Tuple after removing the element")
print(remove_element_from_tuple(my_tuple, random_index))

# 2 Replace the last element in the list with the string 'last' using list comprehension and tuples

my_list_of_tuples = [(x, y) for x in range(5) for y in range(5)]
my_list_of_tuples = ['last' if i == len(my_list_of_tuples) - 1 else my_list_of_tuples[i] for i in
                     range(len(my_list_of_tuples))]
print(my_list_of_tuples)

# 3 Extract only the strings from the following list using list comprehension :

string_list = ['I', 'am', 1, 'list', 'of', 5, 'strings']
string_list = [s for s in string_list if isinstance(s, str)]
print(string_list)

# 4 Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.

matrix = [[[['X' if x == y & y == z else '_'] for x in range(3)] for y in range(3)] for z in range(3)]
print(matrix)

# 5 dictionary

data_set = [('France', 2017, 'M', 78), ('France', 2017, 'F', 70), ('France', 2018, 'M', 79), ('France', 2018, 'F', 69),
            ('Romania', 2017, 'M', 67), ('Romania', 2017, 'F', 66), ('Romania', 2018, 'M', 83),
            ('Romania', 2018, 'F', 25), ('Germany', 2017, 'M', 99), ('Germany', 2017, 'F', 93),
            ('Germany', 2018, 'M', 76), ('Germany', 2018, 'F', 47), ('Italy', 2017, 'M', 52), ('Italy', 2017, 'F', 72),
            ('Italy', 2018, 'M', 52), ('Italy', 2018, 'F', 74), ('Belarus', 2017, 'M', 15), ('Belarus', 2017, 'F', 64),
            ('Belarus', 2018, 'M', 35), ('Belarus', 2018, 'F', 18), ('Portugal', 2017, 'M', 55),
            ('Portugal', 2017, 'F', 44),
            ('Portugal', 2018, 'M', 33), ('Portugal', 2018, 'F', 22), ('China', 2017, 'M', 92),
            ('China', 2017, 'F', 93),
            ('China', 2018, 'M', 96), ('China', 2018, 'F', 100), ('USA', 2017, 'M', 64), ('USA', 2017, 'F', 75),
            ('USA', 2018, 'M', 86), ('USA', 2018, 'F', 47)]
health_index_2017 = {country: [year, gender, life_expectancy] for country, year, gender, life_expectancy in data_set if
                     year == 2017}
health_index_2018 = {country: [year, gender, life_expectancy] for country, year, gender, life_expectancy in data_set if
                     year == 2018}
germany = {year: [gender, life_expectancy] for country, year, gender, life_expectancy in data_set if
           country == 'Germany'}
print(germany)
health_index = {country + '_' + str(year): [year, gender, life_expectancy] for country, year, gender, life_expectancy in
                data_set}
print(health_index)
print({country: data for (country, data) in health_index.items() if data[2] > 50})
print({country: data for (country, data) in health_index.items() if data[2] > 50 and data[1] == 'F'})
print([data[2] for (country, data) in health_index.items()])
