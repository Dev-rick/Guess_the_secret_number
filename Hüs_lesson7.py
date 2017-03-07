
secret = 25



play = str(raw_input("press ENTER to play or type 'x' to Exit:\n>> "))
if play=='x':

    print "Bye, Bye"
    exit()

while True:
    try:
        guess = int(raw_input("Guess a secret number between 1 and 30:\n>> " ))
        if guess == secret:
            print "You have won!!"
            print "Thank you for playing"
            break
        else:
            print "Sorry you have lost, try again!"
            play = str(raw_input("press ENTER to play or type 'x' to Exit:\n>> "))
            if play == 'x':
                print "Bye, Bye!"
                exit()
            continue
    except ValueError:
        print "Oops that is not a number! Try again!"
        continue






