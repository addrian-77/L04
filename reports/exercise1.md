# Bug reports for exercise1.py

Line: 3  
Problem: The function is_even(n) should return True for even numbers, but it returns True when n % 2 == 1, which is true for odd numbers.  
Example: is_even(4) returns False, expected True.  
Fix: return n % 2 == 0

Line: 8  
Problem: The function rectangle_area(width, height) calculates the sum of width and height, but the description states it should return the area of a rectangle.  
Example: rectangle_area(5, 3) returns 8, expected 15.  
Fix: return width * height

Line: 13  
Problem: The function double(n) is described as "twice the number n", but it returns n + 2, which is not twice the number.  
Example: double(5) returns 7, expected 10.  
Fix: return n * 2
