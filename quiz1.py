# Author CCG 10/19/21

year = input("Enter the year of the date: ")
m = input("Enter the month of the date: ")
q = input("Enter the day of the date: ")

if int(m) < 3:
    year = int(year) - 1
    m = int(m) + 12

j = int(year) // 100
k = int(year) % 100

h = (int(q) + (26 * (int(m) + 1)) // 10 + int(k) + int(k) // 4 + int(j) // 4 + 5 * j) % 7

if int(h) == 0:
    day = "Saturday"
elif int(h) == 1:
    day = "Sunday"
elif int(h) == 2:
    day = "Monday"
elif int(h) == 3:
    day = "Tuesday"
elif int(h) == 4:
    day = "Wednesday"
elif int(h) == 5:
    day = "Thursday"
elif int(h) == 6:
    day = "Friday"

if int(m) > 12:
    year = int(year) + 1
    m = int(m) - 12

print(str(m) + "/" + str(q) + "/" + str(year) + " was a " + str(day) + ".")
