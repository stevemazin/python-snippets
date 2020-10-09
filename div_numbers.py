for number in range(1, 100 + 1):
    if number%3 == 0 and number%5 == 0:
        print(number, 'CRACKLE POP')
    elif number%3 == 0:
        print(number, 'CRACKLE')
    elif number%5 == 0:
        print(number, 'POP')
    elif number%3 != 0 and number%5 != 0:
        print(number)
