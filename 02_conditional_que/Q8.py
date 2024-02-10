# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "jemqwwdf"
pass_len = len(password)

if pass_len < 6:
    strength = "Weak"
elif pass_len <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is",strength)