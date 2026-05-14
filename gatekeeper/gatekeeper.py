import sys
BLOCK_USERS=("root","admin","guest")
user=input("Please, write your username: ").strip().lower()

if user in BLOCK_USERS:
    print("Access denied by security policy")
    sys.exit(1)
else:
    privilege_input=input("Please, write your privilege level: ")
    if not privilege_input.isdigit():
        print("Error: Privilege level must be a number (1-3)")
        sys.exit(1)
    privilege=int(privilege_input)
    match privilege:
        case 1:
            print("Read-only access")
        case 2:
            print("Edit access")
        case 3:
            print("Admin access")
        case _:
            print("This privilege doesn't exists")


