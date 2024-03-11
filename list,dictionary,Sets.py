# Creating a list of fruits
fruits_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Creating a dictionary for fruits from A to H
fruits_dict = {'A': 'apple', 'B': 'banana', 'C': 'cherry', 'D': 'date', 'E': 'elderberry', 'F': 'fig', 'G': 'grape', 'H': 'honeydew'}

# Creating a set with colors
colors_set = {"red", "yellow", "purple", "green"}

# Adding elements to the list
fruits_list.append("kiwi")
print("List after adding element:", fruits_list)

# Removing elements from the list
fruits_list.remove("date")
print("List after removing element:", fruits_list)

# Modifying elements in the list
fruits_list[0] = "apricot"
print("List after modifying element:", fruits_list)

# Adding elements to the dictionary
fruits_dict['I'] = 'kiwi'
print("Dictionary after adding element:", fruits_dict)

# Removing elements from the dictionary
del fruits_dict['D']
print("Dictionary after removing element:", fruits_dict)

# Modifying elements in the dictionary
fruits_dict['A'] = 'apricot'
print("Dictionary after modifying element:", fruits_dict)

# Adding elements to the set
colors_set.add("blue")
print("Set after adding element:", colors_set)

# Removing elements from the set
colors_set.remove("purple")
print("Set after removing element:", colors_set)