import random
def main():
    guess = random.randint(1,10)
    while 1:
        answer = int(input('please enter your guess:'))
        if answer == guess :
            print('you are right.\n')
            break
        elif answer > guess:
            print('you are too big.\n')
        elif answer < guess:
            print('you are too small.\n')

if __name__ == "__main__":
    main()