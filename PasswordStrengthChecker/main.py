import zxcvbn

def crack_time(password):
    result = zxcvbn.zxcvbn(password)
    return result['crack_times_display']['offline_slow_hashing_1e4_per_second']

if __name__ == "__main__":
    password = input("Enter your password: ")
    if not password:
        print("Password cannot be empty!")
        exit(1)
    print(f"Estimated time to crack password: {crack_time(password)}")
