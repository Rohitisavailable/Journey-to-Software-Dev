def solve_eqn(a: float, b : float, c:float) -> float:
    return(float(c) - float(b)) / float(a)

print("ax + b = c linear eqn")

a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

x = solve_eqn(a, b, c)
print(f"x is {x}")