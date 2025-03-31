#!/usr/bin/env python3
# Example code with common issues for demonstration

import os
import sys
import time
import sqlite3
import requests
import json

# Hardcoded credentials - security issue
DB_USER = "admin"
DB_PASS = "password123"  # This should not be hardcoded

# Global variable - can lead to unexpected behavior
counter = 0

def connect_to_db():
    """Connect to the SQLite database."""
    return sqlite3.connect('example.db')

# Function with multiple responsibilities - violates single responsibility principle
def process_user_data(user_id, data):
    global counter
    counter += 1
    
    # SQL Injection vulnerability - using string formatting for SQL
    conn = connect_to_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE user_id = '{user_id}'"  # Vulnerable to SQL injection
    cursor.execute(query)
    
    # Inefficient data processing - O(n²) complexity
    result = []
    for item in data:
        found = False
        for existing in result:
            if existing['id'] == item['id']:
                found = True
                break
        if not found:
            result.append(item)
    
    # Resource leak - connection not properly closed in all cases
    if len(result) > 0:
        print(f"Found {len(result)} items")
        return result
    
    # Uncaught exception possibility
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()

# Duplicate code - should be refactored
def get_user_by_id(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE user_id = '{user_id}'"  # Same vulnerability as above
    cursor.execute(query)
    return cursor.fetchone()

# Unclear naming - function name doesn't describe what it does
def do_stuff(x, y):
    # Magic numbers with no explanation
    if x > 1000:
        return y * 1.05
    else:
        return y * 0.95

# No error handling
def fetch_external_data(url):
    response = requests.get(url)
    return response.json()  # Will fail if response is not JSON

# Main execution - with unnecessary complexity
if __name__ == "__main__":
    # Debug code left in production
    print("DEBUG: Starting application")
    
    # Inefficient loop that could be simplified
    data = []
    for i in range(10):
        for j in range(10):
            if i == j:
                data.append({"id": i, "value": i*j})
    
    # Commented out code
    # Old implementation that's no longer used
    # for item in data:
    #     process_item(item)
    
    result = process_user_data("user123", data)
    print(result)
    
    # Pointless code that does nothing useful
    time.sleep(1)  # Arbitrary delay with no purpose
    print("Application finished")