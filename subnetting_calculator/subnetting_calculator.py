import sys

prefix_input=input("Write your prefix CIDR: ").strip().lower()
if prefix_input == "exit":
        sys.exit(0)
        
if not prefix_input.isdigit():
    print("Error: Prefix CIDR must be a number (0-32)")
    sys.exit(1)

prefix = int(prefix_input)

if prefix > 32 or prefix < 0:
    print("ERROR: This mask is not valid (must be 0-32).")
elif prefix >= 31:
    print(f"A /{prefix} network has 0 usable hosts for standard devices.")
else:
    calculation = 2**(32 - prefix) - 2
    print(f"The number of available hosts is {calculation}")
    