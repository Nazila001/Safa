import shlex

# این متغییر همان دیتابیس ماست
DATA = {}


def checking_input(x):
    if type(int(x)) is not int:
        raise TypeError('Work with Numbers Only')


def cntr_arg():
    ...


while True:
    try:
        cmd, *args = shlex.split(input('# '))
        if cmd == 'set':
            if args[0] not in DATA and len(args) < 3:
                print("Please enter the type of value!")
                break
            if args[0] not in DATA:
                checking_input(args[2])
                args[1] = args[2]
                del args[2]
            checking_input(args[1])

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
