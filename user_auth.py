import argparse
import hashlib

users = {}

def register(username, email, password):
    users[email] = {"username": username, "password": hashlib.sha256(password.encode()).hexdigest()}
    print("User registered successfully!")

def login(email, password):
    if email in users and users[email]["password"] == hashlib.sha256(password.encode()).hexdigest():
        print("Login successful!")
    else:
        print("Invalid email or password!")

def main():
    parser = argparse.ArgumentParser(description="User Registration and Login System")
    parser.add_argument('action', choices=['register', 'login'], help="Action to perform")
    parser.add_argument('username', nargs='?', help="Username (required for registration)")
    parser.add_argument('email', help="Email address")
    parser.add_argument('password', help="Password")
    
    args = parser.parse_args()

    if args.action == 'register':
        if not args.username:
            print("Username is required for registration!")
        else:
            register(args.username, args.email, args.password)
    elif args.action == 'login':
        login(args.email, args.password)

if __name__ == '__main__':
    main()
