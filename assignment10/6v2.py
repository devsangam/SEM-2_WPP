import random
import math
import matplotlib.pyplot as plt

def f(p, func):
    return sum(coef * math.pow(p, power) for coef, power in func)

def find_root(a, b, x_vals, y_vals, func, tol=1e-6):
    c = (a + b) / 2.0
    fc = f(c, func)
    
    x_vals.append(c)
    y_vals.append(fc)
    
    print(f"a: {a}, b: {b}, c: {c}, f(c): {fc}")
    
    if abs(fc) < tol:
        return c
    
    if f(a, func) * fc < 0:
        return find_root(a, c, x_vals, y_vals, func, tol)
    else:
        return find_root(c, b, x_vals, y_vals, func, tol)

n = int(input("Enter number of terms:\t"))

func = []
for i in range(n):
    coef = float(input("Coefficient:\t"))
    power = float(input("Power:\t"))
    func.append((coef, power))

a = random.randint(-100, 100)
b = random.randint(-100, 100)
while f(a, func) * f(b, func) > 0:
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
x_vals = [a, b]
y_vals = [f(a, func), f(b, func)]

root = find_root(a, b, x_vals, y_vals, func)
print("Root found:", root)
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, marker='o', linestyle='-')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method Intermediate Points")
plt.grid(True)
plt.show()
