import random


def app():
    random_number = random.randint(1,100)
    select_number = int(input("Guess the number I'm thinking: "))
    while random_number != select_number:
        if random_number > select_number:
            print("The number I'm thinking is higher than yours ")
        else:
            print("The number I'm thinking is lower than yours ")
        select_number = int(input("Choos another number: "))
    print("You won")


if __name__ == "__main__":
    app()