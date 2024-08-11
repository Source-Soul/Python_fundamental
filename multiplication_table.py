
user_input = int(input("Enter a number: "))


def multiplication_table(user_input):
    for i in range(1, 11):
        print(f"{user_input} x {i} = {user_input*i}")



multiplication_table(user_input)

