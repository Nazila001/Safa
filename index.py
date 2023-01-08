import shlex

# این متغییر همان دیتابیس ماست
DATA = {}
num_test = 0


def checking_input(x):
    if len(args) > 2:
        if args[1] == 'int':
            if type(int(args[2])) != type(num_test):
                print("Error")
            else:
                args[1] = args[2]
                del args[2]
        elif args[1] == 'str':
            print('Error')
        elif args[1] != 'int' or 'str':
            print('Error')
    else:
        if type(int(1)) is not int:
            raise TypeError('Error')


while True:
    try:
        cmd, *args = shlex.split(input('# '))
        if cmd == 'set':
            if args[0] not in DATA and len(args) < 3:
                print("Error")

            if args[0] not in DATA:
                checking_input(args)
            else:
                checking_input(args)

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    except KeyboardInterrupt as e:
        print('Bye!')
        break

    if cmd.upper() == 'SET':
        DATA[args[0]] = args[1]
    elif cmd.upper() == 'GET':
        print(DATA[args[0]])
    elif cmd.upper() == 'DEL':
        DATA[args[0]] = None
