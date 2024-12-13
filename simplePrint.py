for _ in range(2):  # if you don't need to use a variable you can switch to _
    print("Hello world")

name = input("What is your name?")
name = name.strip().title()

print(f"Hello {name}")
