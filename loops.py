for i in range(6):
    print(i)

names = ["Harry", "Ron", "Hermione"]

for i in names:
    print(i)

# print('meow\n' * 3, end="")

# while True:
#     n = int(input("What's n?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
