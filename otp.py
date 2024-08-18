import random

def generate_otp():
    # Generate a random 6-digit number
    otp = random.randint(100000, 999999)
    return otp

# Example usage
otp = generate_otp()
print(f"Your OTP is: {otp}")
