#Random numbers

import random
#def get_code():
code=""
for i in range(5) :
    num=str(random.randrange(10))
    big_str=chr(random.randrange(97, 123))
    small_str=chr(random.randrange(65,91))
    codes=random.choice([num,big_str,small_str])
    code+=codes
    #ret = get_code()
print (code)

