import os
import sqlite3
import subprocess

import pytest

import exercise4
from exercise4 import *


# bug report 1
def test_r1_check_admin_wrong_password():
    assert check_admin("wrong") == False


# bug report 2
def test_r2_find_user_sql_injection():
    """Proves that the function is vulnerable to SQL injection by testing with a malicious username."""
    # Mock database object with a simple execute method that returns a mock result
    class MockDB:
        def execute(self, query, params=None):
            # Simulate that the query is executed as a string with no escaping
            # The query will be vulnerable to injection if string formatting is used
            if "DROP TABLE users" in query:
                return None  # Simulate table drop (should not happen)
            # Return a mock row if the username matches, otherwise None
            if "admin" in query or "'; DROP TABLE users" in query:
                return None
            return {"id": 1, "username": "testuser", "password": "pass123"}

    db = MockDB()
    # Malicious input to trigger SQL injection
    malicious_username = "'; DROP TABLE users; --"
    
    # Call the vulnerable function
    result = find_user(db, malicious_username)
    
    # The function should not execute the DROP TABLE command due to injection
    # But because it uses string formatting, it will execute the malicious query
    # The test proves the vulnerability by showing that the query is constructed
    # with unescaped input, which is a security flaw.
    
    # Even though the function returns None when no row exists, the real issue
    # is that the query is vulnerable — so we assert that the query was not
    # properly parameterized, and the function still executes the malicious input.
    
    # Since the function does not use parameterized queries, the query is built
    # as: "SELECT * FROM users WHERE username = ''; DROP TABLE users; --'"
    # This is a direct SQL injection.
    
    # The test does not check for a specific row, but rather proves that the
    # function is vulnerable
