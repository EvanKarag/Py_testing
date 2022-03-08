import math

user_input = float(input("Give one number to learn its square root, or type 'quit' to exit:"))

while (user_input != 4):
    root = float(user_input)
    root = math.sqrt(root)
    print("the square root of" + user_input +" is equal to:" + root)
    user_input = input("Give one number, or type 'quit' to exit:")
