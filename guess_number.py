from pickle import TRUE


real_number=88
guess=[]
guess_count=1
guess_limit=3
#out_of_limit = False

while guess!= real_number :
    if guess_count<=guess_limit:
        
        guess=int(input('你要猜的數字'))
        if  guess > real_number:
            print('小一點')
        elif guess < real_number:
            print('大一點') 
        guess_count += 1
    else:
       print ('LOSE')
       break
# if out_of_limit:
#     print('lose')
else:
    print('YAAA~~~~')
