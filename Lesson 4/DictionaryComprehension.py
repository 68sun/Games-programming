my_dict = {"item1" : 4, "item3" : 5, "item2" : 6}
new_dict = {i : my_dict[i]*2 for i in my_dict}
print(new_dict)
