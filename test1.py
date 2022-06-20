num1=int(input('數字'))
op=input('符號')
num2=int(input('數字'))


if op=='+':
    sum=num1+num2
    print(sum)
elif op=='-':
    sum=num1+num2
    print(sum) 
elif op=='*':
    sum=num1+num2
    print(sum)
elif op=='/':
    sum=num1+num2 
    print(sum)
else:
    print('輸入錯誤') 

while True:
    op=input('符號')
    num=int(input('數字'))
    if op=='+':
        sum=sum+num
        print(sum)
    elif op=='-':
        sum=sum-num
        print(sum) 
    elif op=='*':
        sum=sum*num
        print(sum) 
    elif op=='/':
        sum=sum/num
        print(sum)
    else:
        print('輸入錯誤')
        break 
print (sum)        
       
  



                

# a =input(':')
# ope = input(':')
# b = input(':')

# sum = str(eval(a+ope+b))
# print(sum)
# Flag = True

# while Flag:
  
#   ope = input(':')
#   b = input(':')
#   sum = str(eval(sum+ope+b))
#   print(sum)

# #   if ope == 0:
# #     Flag = False