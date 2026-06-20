# Ask user for their name
name = input("What's your name? ").strip().title()

#say hello to user
print("Hello,", name, sep = " ")

def main():
    name = input("What's your name? ")
    hello(name)


def hello(to = "world"):
    print("Hello,", to)


main()
