
# try-except lesson example

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))

        print(x/y)

    except Exception as e:
        print('Invalid input')
        print(e)
    else:
        break;
    finally:
        print('try-except is over!')