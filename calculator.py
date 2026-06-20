x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)
print(z)
# or
a = x / y
print(f"{a:.2f}")

# Or
print(f"{round(int(input("What's x? ")) / int(input("What's y? ")), 2):,}")

# Or

def main():
    x = int(input("What's x? "))
    print("x square is", square(x))

def square(n):
    return n * n # n ** 2 # pow(n, 2)


main()
