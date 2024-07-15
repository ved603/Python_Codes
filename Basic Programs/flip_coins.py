import random
num = int(input('Enter the Number of times the Coin is flipped : '))
heads = 0
tails = 0
for i in range(num):
    a = random.randint(0,1)
    if a == 0:
        tails += 1
    else:
        heads += 1
print('Total number of head is ', heads)
print('Total number of Tails is : ', tails)
res = (heads/num) * 100
print('The Percentage of heads over tails is : ' , res)