date = input("Enter a date in dd/mm/yyyy format")
date = date.split("/")


## Day
while int(date[0]) <= 0 or int(date[0]) >= 32 or len(date[0]) > 2:
    date = input("Enter a date in dd/mm/yyyy format") 
    date = date.split("/")


## Month
while int(date[1]) <= 0 or int(date[1]) >= 13 or len(date[1]) > 2:
    date = input("Enter a date in dd/mm/yyyy format") 
    date = date.split("/")


monthName = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print("The date is %s %s, %s " % (monthName[int(date[1])-1], date[0], date[2]))
