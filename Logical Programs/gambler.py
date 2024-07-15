import random
stake = int(input('Enter the Available Stakes : '))
goal = int(input('Enter the Goal of the Gambler : '))
N = int(input('Enter the Number of Times he played : '))
passed = 0
failed = 0

for i in range(N):
    if(stake != goal and stake > 1):
        rand1 = random.randint(1,stake)
        rand2 = random.randint(1,stake)
        if(rand1 > rand2):
            stake += rand2
            passed += 1
        elif(rand1 < rand2):
            stake -= rand1
            failed += 1
        else:
            print('Match Draw')
    
    
print("The Number of time gambler win is : ",passed)
print("The Winning percentage is : ",((passed/N)*100))