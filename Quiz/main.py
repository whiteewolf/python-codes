from time import sleep


print("Welcome to the PC Quiz")

play = input("Wanna play? (y / n) : ")
if play == 'y':
    ram_q = input("What does RAM stands for? : ")
    if ram_q == 'random access memory':
        print("Great! You guessed my 1st question! On to the next one")
        invention = input('When was the first computer invented? :')
        if invention == '1943':
            print("YES! Next Question:")
            company = input("Which popular company designed the first CPU? : ")
            if company == 'Intel':
                print("Yes! You win our quiz! You get a reward! Here is a cookie: 🍪")
                sleep(1)
elif play != 'y':
    print("Okay, byee")
    sleep(0.8)