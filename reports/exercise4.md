# Bug reports for exercise4.py

Line: 8  
Problem: The function returns `True` if the password is the admin password, but the condition `ADMIN_PASSWORD != ""` is always true since `ADMIN_PASSWORD` is defined as "admin123", which is not empty. However, the logic is flawed because it checks if the password equals the admin password only when the admin password is non-empty, which is redundant and incorrect. The function should simply check if `password == ADMIN_PASSWORD`.  
Example: check_admin("wrong") returns True, expected False.  
Fix: return password == ADMIN_PASSWORD

Line: 14  
Problem: The function uses string formatting directly in SQL without escaping, which makes it vulnerable to SQL injection. Additionally, the function returns the first row of the query result, but the description says "The user's row, or None if the username does not exist". The current implementation may return a row even if no user exists (e.g., if the query returns no rows, `fetchone()` returns `None`, which is correct), so the logic is mostly sound, but the SQL injection risk is a critical security bug.  
Example: If an attacker passes `username = "'; DROP TABLE users; --"`, the query could be corrupted.  
Fix: Use parameterized queries instead of string formatting. Replace line 14 with: `return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()`
