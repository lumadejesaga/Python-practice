import random


def password_generator():
    UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    NUMBER = ["1","2","3","4","5","6","7","8","9","0"]
    SYMBOL = ["!","#","$","&","/","(",")"]

    CHAR = UPPER + LOWER + NUMBER + SYMBOL

    password = []

    for i in range(15):
        random_char = random.choice(CHAR)
        password.append(random_char)
    
    password = "".join(password)
    return password


def app():
    password = password_generator()
    print("Your new password is: " + password)


if __name__ == "__main__":
    app()