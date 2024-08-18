import random

def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

otp = generate_otp()
print(f"Your OTP is: {otp}")
