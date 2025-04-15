import math
import time
import matplotlip.pylot as plt

def cube_root_by_bisection(n, epsion=0.0001, max_iterations = 100):

 steps = 0
 low = 0
high = max(1, abs(n))  # Handle cases where n is 0 or between -1 and 1
guess = (low + high) / 2.0

while steps < max_iterations and abs(guess**3 - abs(n)) > epsilon:
    if guess**3 < abs(n):
        low = guess
    else:
        high = guess
        guess = (low + high) / 2.0
        steps += 1
    if n < 0:
        return -guess, steps
    else:
        return guess, steps

def test_cube_root_bisection():
    
    print("Testing cube root using bisection:")
    test_numbers = [-8, -1, 0, 1, 8, 27, 64, 125]
    for num in test_numbers:
        root, steps = cube_root_bisection(num)
        print(f"Cube root of {num}: {root:.4f} (steps: {steps})")
