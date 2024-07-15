import time

def start():
    global start_watch
    start_watch = time.time()
    print("Started")

def stop():
    if not start_watch:
        print("Stopwatch was not start yet !")
    stop_watch = time.time()
    elapsed = stop_watch - start_watch
    print(f"The Elapsed Time is : {elapsed:.2f}")

while True: 
    print('\n1. 1 for Start stopwatch \n2. 2 for stop stopwatch \n3. 3 for terminate')
    choice = int(input())
    if choice == 1:
        start()
        
    elif choice == 2:
        stop()    

    elif choice == 3:
        quit()

    else:
        print("Invalid choice is selected")
