room_items = { "item1" : {"Name" : "Lamp", "Colour" : "Red"},
"item2": {"Name" : "Table", "Colour" : "Brown", "Type": 0},
"item3": {"Name" : "Lamp", "Colour" : "Red"},
"item4": {"Name" : "Chair", "Colour" : "Green", "Type": 1}}

items = {}
for i in room_items:
    if room_items.get(i) == items.get("item1"):
        continue
    items[i] = room_items.get(i)
print(items)
    
    

