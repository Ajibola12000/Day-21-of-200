# 1️⃣ Fixed "Usual Suspects" bug: Typo in variable name
def calculate_age(birth_year, current_year):
    age = current_year - birth_year  # Fixed: 'current_yeer' -> 'current_year'
    return age

# 2️⃣ Fixed "Ask Why" bug: Loop logic clarified
def sum_favorite_numbers(numbers):
    total = 0
    for num in numbers:  # Fixed: Avoids index confusion
        total += num
    return total

# 3️⃣ Fixed "Bug Isn't Where You Think": Added validation
def validate_profile(username, password, email):
    if len(username) >= 3 and len(password) >= 8 and "@" in email:  # Fixed: Added checks
        return True
    return False

# 4️⃣ Fixed "Rubber Duck" bug: Removed extra parenthesis
def is_premium_user(user_status):
    return user_status == "premium"  # Fixed: No more syntax error

# 5️⃣ Fixed "Don't Trust Docs" bug: Corrected operation
def add_user_points(current_points, bonus):
    """Adds bonus to current_points."""
    return current_points + bonus  # Fixed: Now actually adds (not multiplies)

# 6️⃣ Fixed "Write Docs" bug: Handled edge case
def divide_points(points, divisor):
    if divisor == 0:  # Fixed: Added check
        raise ValueError("Divisor cannot be zero")
    return points / divisor

# 7️⃣ Fixed "Walk Away" bug: Added base case
def factorial(n):
    if n == 0:  # Fixed: Base case stops recursion
        return 1
    return n * factorial(n - 1)

# --- Test Cases ---
print("Age:", calculate_age(1990, 2025))  # ✅ Correct: 35
print("Sum:", sum_favorite_numbers([10, 20, 30]))  # ✅ Correct: 60
print("Valid Profile:", validate_profile("Amy", "password123", "amy@example.com"))  # ✅ True
print("Premium User:", is_premium_user("premium"))  # ✅ True
print("Points Added:", add_user_points(100, 5))  # ✅ Correct: 105
print("Points Divided:", divide_points(100, 5))  # ✅ Correct: 20.0
print("Factorial:", factorial(3))  # ✅ Correct: 6

# Uncomment to test error cases:
# print(divide_points(100, 0))  # Raises ValueError (handled)
# print(factorial(-1))  # Would recurse infinitely (exercise: add another guard!)