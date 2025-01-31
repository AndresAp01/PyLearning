# Logical Operators = evaluate multiple conditions
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is ok.")

temp2 = 20
is_sunny = False

if temp2 >= 28 and is_sunny:
    print("It is hot outside!!")
    print("It is SUNNY.")
elif temp2 <= 0 and is_sunny:
    print("it is cold outside!!")
    print("It is SUNNY.")
elif 28 > temp2 > 0 and is_sunny:
    print("It is warm outside!!")
    print("It is SUNNY.")
elif temp2 >= 28 and not is_sunny:
    print("It is hot outside!!")
    print("It is CLOUDY.")
elif temp2 <= 0 and not is_sunny:
    print("it is cold outside!!")
    print("It is CLOUDY.")
elif 28 > temp2 > 0 and not is_sunny:
    print("It is warm outside!!")
    print("It is CLOUDY.")






