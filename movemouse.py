import mouse, time
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def setTimeout():
    msg = "Welcome to movemouse! This program checks to see if your mouse position has changed over a period of time. This is where you set THAT period of time (in seconds)."
    return int(input(msg))

def moveMouseInSquare():
    mouse.move(0, 150, absolute = False, duration = .5)
    mouse.move(150, 0, absolute = False, duration = .5)
    mouse.move(0,-150, absolute = False, duration = .5)
    mouse.move(-150, 0, absolute = False, duration = .5)

def init():
    timeout = setTimeout()
    # timeout = 5
    real_time = timeout / 60
    clock = 0
    lazy_count = 0
    productive_count = 0
    productive_percentage = 100
    total_interval = productive_count + lazy_count
    productive_minutes = 0
    while True:
        print("Thank you for using movemouse! Close this window to kill the program.")
        print("------STATS------")
        print("Lazy Count: "+str(lazy_count))
        print("Productive Count: "+str(productive_count))
        print("Run Time: "+str(round(clock/60,2))+" Min")
        print("Productive Time: "+str(round(productive_minutes,2))+" Min")
        print("Productive Percentage: "+str(round(productive_percentage,2))+"%")
        x = mouse.get_position()
        y = "Not recorded"
        print("First Position: "+str(x))
        time.sleep(timeout)
        y = mouse.get_position()
        print("Second Position: "+str(y))
        if(x == y):
            print("Moving!")
            moveMouseInSquare()
            lazy_count = lazy_count+1
            clock+=(2/60)
        else:
            productive_count+=1
            productive_minutes+=real_time
        total_interval = productive_count + lazy_count
        productive_percentage = (productive_count / total_interval)*100
        clock+=timeout
        
        clear()

init()