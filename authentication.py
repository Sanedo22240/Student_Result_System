
def admin_login():
    ADMIN_PASSWORD = "admin123"  # hardcoded for simplicity
    print("=== Admin Login ===")
    for _ in range(3):
        pwd = input("Enter admin password: ")
        if pwd == ADMIN_PASSWORD:
            print("Login successful!\n")
            return True
        else:
            print("Incorrect password.")
    print("Too many failed attempts. Exiting.")
    return False
