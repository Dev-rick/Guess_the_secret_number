
secret = 25



play = str(raw_input("press ENTER to play or type 'x' to Exit:\n>> "))
if play=='x':

    print "Bye, Bye"
    exit()

while True: #used for creating a loop(where you come back by 'continue' to this point!
    try: #used to implement the except for a ValueError
        guess = int(raw_input("Guess a secret number between 1 and 30:\n>> " ))
        if guess == secret:
            print "You have won!!"
            print "Thank you for playing"
            exit()
        else:
            print "Sorry you have lost, try again!"
            play = str(raw_input("press ENTER to play or type 'x' to Exit:\n>> "))
            if play == 'x':
                print "Bye, Bye!"
                exit()
            continue #start again by while True:
    except ValueError: #if there is a ValueError, which means when User entered a str and not an int.
        print "Oops that is not a number! Try again!"
        continue






