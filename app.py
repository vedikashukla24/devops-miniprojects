# Mini Project 02 - Git Workflow Simulator

def login():
    username = input("Enter Username: ")
    return username

def dashboard():
    print("\nDashboard")
    print("1. View Profile")
    print("2. Settings")
    print("3. Logout")

def profile(username):
    print("\nUser Profile")
    print(f"Username : {username}")

def main():
    print("Git Workflow Simulator")

    username = login()
    dashboard()
    profile(username)

if __name__ == "__main__":
    main()
