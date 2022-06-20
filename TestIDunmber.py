ID= input("請輸入身份證字號:").upper()
if(len(ID) != 10):
 print("錯誤，身份證字號須為 10 碼")
elif(not ID[0].isalpha()):
 print("錯誤，第一碼須為英文字母")
elif(not ID[1:].isdigit()):
 print("錯誤，後九碼須為數字")
elif(ID[1]<'1' or ID[1]>'2'):
 print("錯誤，第一個數字須為 1 或 2")
else:
 X= {'A':10, 'B':11, 'C':12, 'D':13, 'E':14,
 'F':15, 'G':16, 'H':17, 'I':34, 'J':18,
 'K':19, 'L':20, 'M':21, 'N':22, 'O':35,
 'P':23, 'Q':24, 'R':25, 'S':26, 'T':27,
 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31,
 'Z':33 }
 num= X[ID[0]]//10 + (X[ID[0]]%10)*9
 for i in range(2,10):
    num += int(ID[-i])*(i-1)
 ans= 10 - num % 10
 if(ans==int(ID[-1])):
    print(ID + " 是正確的身分證字號")
 else:
    print(ID + " 不是正確的身分證字號")