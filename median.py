"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def median(x):
    x.sort()
    length = len(x)
    if length % 2 == 0:
        print(    ((  (x[int(length/2 -1)])   + (x[int(length/2 )]) )/2) )
    else:
        print(x[int(length/2 -0.5)])
        
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
median(numbers)