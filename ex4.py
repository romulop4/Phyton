for number in range(1, 100):
    if number >= 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, 'falso')
                break
        else:
            print(number, 'verdadeiro')
