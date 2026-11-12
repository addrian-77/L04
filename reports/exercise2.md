# Bug reports for exercise2.py

Line: 3  
Problem: The function claims to return True if the grade is 5 or more, but the condition uses `grade > 5`, which excludes 5. It should include 5.  
Example: is_passing(5) returns False, expected True.  
Fix: return grade >= 5

Line: 8  
Problem: The description says "At least 8 characters and at least one digit", which means the length should be 8 or more, not strictly greater than 8. The condition `len(password) > 8` fails for passwords of length 8.  
Example: is_valid_password("password123") returns False, expected True.  
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 12  
Problem: The function `clamp(x, low, high)` has a logical error in the implementation. It says "x, limited to the range from low to high", but the code returns `max(low, min(x, low))`, which simplifies to `low` regardless of x. This is incorrect.  
Example: clamp(10, 5, 15) returns 5, expected 10.  
Fix: return max(low, min(x, high))
