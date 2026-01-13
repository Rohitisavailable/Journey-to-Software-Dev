unit = input("Is this temp in Celsius or Fareneit(C ot F): ")

temp = float(input("Enter Your Temperature: "))


if unit == "C":
    temp = round(((9 * temp) / 5 + 32), 1)
    print(f"Your Temperature in Farenheit is:{temp}°F")
elif unit == "F":
    pass
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Your Temperature in Celsius is:{temp}°C")
else:
    print(f"{unit} is invaid unit of measurement")