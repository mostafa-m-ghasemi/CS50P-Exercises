# print_column

def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")
main()

# print_row

def main():
    print_row(4)


def print_row(width):
    print("?" * width)
main()

# print_square

def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()