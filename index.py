import shlex

# این متغییر همان دیتابیس ماست
DATA = {}


while True:
    try:
        cmd, *args = shlex.split(input('# '))
    except ValueError as e:
        continue
    except KeyboardInterrupt as e:
        print('Bye!')
        break
    
    if cmd.upper() == 'SET':
        DATA[args[0]] = args[1]
    elif cmd.upper() == 'GET':
        print(DATA[args[0]])
     
   if cmd.upper() == 'DEL':
        DATA[args[0]] = None
        
