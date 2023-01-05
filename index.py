import shlex

# این متغییر همان دیتابیس ماست
DATA = {}


def checking(x):
    if type(int(x)) is not int:
        raise TypeError('Work with Numbers Only!')

        
while True:
    try:
        cmd, *args = shlex.split(input('# '))
        if cmd == 'set':
            checking(args[1])
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")
    except KeyboardInterrupt as e:
        print('Bye!')
        break
    
    if cmd.upper() == 'SET':
        DATA[args[0]] = args[1]
    elif cmd.upper() == 'GET':
        print(DATA[args[0]])
   if cmd.upper() == 'DEL':
        DATA[args[0]] = None
        
