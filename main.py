import random  # Random Number Generation

print('\nWelcome To Dice Simulator By Zeeshan Khalid !!!\n')


def main(num1, num2):
    """
    The Main Function of The Program
    """
    number = random.randint(num1, num2)
    return number


if __name__ == "__main__":
    while True:
        result = main(1, 6)

        start = input('\nDo You Wanna Roll The Dice (y/n):')

        if start == 'y':
            print('Your Number is :', result)

        if start == 'n':
            exit()

        if result == 6:
            print('\nCongratz You Got A Six\n')
