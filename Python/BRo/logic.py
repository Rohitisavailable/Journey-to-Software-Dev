# logical operaotrs = eval multiple condition
# or = at least 1 condition must be true
# and = both must be true
# not = inverts the condition

temp = 45

is_raining = False
#            ▼ or operator
if temp > 35 or temp < 0 or is_raining:
    print("Event is cancel")

else:
    print("not cancel")