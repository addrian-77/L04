# Bug reports for exercise3.py

Line: 3  
Problem: The function averages a list, but if the list is empty, it will cause a division by zero error. The description states that an empty list has an average of 0, but the current code calls `len(numbers)` which would be 0 for an empty list, leading to division by zero.  
Example: average([]) raises ZeroDivisionError, expected 0.  
Fix: return sum(numbers) / len(numbers) if numbers else 0

Line: 8  
Problem: The function returns the first word of the text, but if the text is empty or has no words (e.g., "   "), `split()` returns an empty list, and `split()[0]` will raise an IndexError. The description says it should return "" if the text is empty.  
Example: first_word("") returns IndexError, expected "".  
Fix: return text.split()[0] if text.strip() else ""

Line: 13  
Problem: The function calculates part as a percentage of total, but if total is 0, it will cause division by zero. The description explicitly states that if total is 0, the result is 0.  
Example: percent(5, 0) raises ZeroDivisionError, expected 0.  
Fix: return part / total * 100 if total != 0 else 0
