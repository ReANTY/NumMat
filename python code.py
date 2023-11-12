def trap(h, f0, f1):
    return h * (f0 + f1) / 2

def trapm(h, n, f):
    summation = f[0]

    for i in range(1, n - 1):
        summation += 2 * f[i]

    summation += f[n - 1]
    result = h * summation / 2

    return result

def simp13(h, f0, f1, f2):
    return 2 * h * (f0 + 4 * f1 + f2) / 6

def simp38(h, f0, f1, f2, f3):
    return 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8

def simp13m(h, n, f):
    summation = f[0]

    for i in range(1, n - 1, 2):
        summation += 4 * f[i] + 2 * f[i + 1]

    summation += 4 * f[n - 1 - 1] + f[n - 1]
    result = h * summation / 3

    return result

def simpInt(a, b, n, f):
    h = (b - a) / n
    result = 0

    if n == 1:
        result = trap(h, f(a), f(b))
    else:
        m = n
        odd = n / 2 - int(n / 2)

        if odd > 0 and n > 1:
            result += simp38(h, f(b - 3 * h), f(b - 2 * h), f(b - h), f(b))
            m = n - 3

        if m > 1:
            result += simp13m(h, m, f)

    return result

def trapun(x, y, n):
    result = 0

    for i in range(1, n):
        result += (x[i] - x[i - 1]) * (y[i - 1] + y[i]) / 2

    return result

def uneven(n, x, f):
    h = x[1] - x[0]
    k = 1
    result = 0.0

    for j in range(1, n):
        hf = x[j + 1] - x[j]

        if abs(h - hf) < 0.000001:
            if k == 3:
                result += simp13(h, f[j - 3], f[j - 2], f[j - 1])
                k -= 1
            else:
                k += 1
        else:
            if k == 1:
                result += trap(h, f[j - 1], f[j])
            else:
                if k == 2:
                    result += simp13(h, f[j - 2], f[j - 1], f[j])
                else:
                    result += simp38(h, f[j - 3], f[j - 2], f[j - 1], f[j])
                k = 1

        h = hf

    return result

import math

def integrand(t, g, m, c):
    return g * m / c * (1 - math.exp(-c / m * t))

def simulate_parachute_drop(a, b, n, g, m, c):
    h = (b - a) / n
    t_values = [a + i * h for i in range(n + 1)]
    y_values = [integrand(t, g, m, c) for t in t_values]

    result_trapezoidal = trapm(h, n+1, y_values)

    return result_trapezoidal

# Example usage:
a = 0  # initial time
b = 10  # final time
n = 5000  # number of segments

g = 9.8  # acceleration due to gravity (m/s^2)
m = 68.1  # mass of the parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

result = simulate_parachute_drop(a, b, n, g, m, c)
print(f"The calculated distance using the trapezoidal rule is: {result} meters.")
