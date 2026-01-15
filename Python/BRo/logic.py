# logical operaotrs = eval multiple condition
# or = at least 1 condition must be true
# and = both must be true
# not = inverts the condition


# OR OPERATOR 
temp = 25

is_raining = False
#            ▼ or operator
if temp > 35 or temp < 0 or is_raining:
    print("Event is cancel")

else:
    print("not cancel")

# AND OPERATOR

temperature = -10

is_snowing = True

if temperature < 0 and is_snowing:
    print("It is Winter")

else:
    print("it is Summer")


#    NOT OPERATOR

temp1 = 156

is_burining = True

if temp1 <= 15 and not is_burining:
    print("it is cold")

else:
    print("it is hot")