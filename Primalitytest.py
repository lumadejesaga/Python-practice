def is_primal(number):
    a = 0
    for i in range(1,number+1):
        if number % i == 0:
            a += 1
        else:
            continue
    if a == 2:
        return True
    else:
        return False


def run():
    number = int(input("Input a number to know if it's a primal number: "))
    if is_primal(number): 
        print("It's a primal number")
    else: 
        print ("It's not a primal number")


if __name__ == "__main__":
    run()