# bmi module 少被用
def BMI(w,h):
    return w/(h/100)**2

print(__name__)
print(__file__)

# MAIN                    #__name__: '__模組名稱__' 代表該模組(.py)的程式是被import的 EX: import bmi
if __name__=='__main__':  #__name__: '__main__' .py的程式是直接被執行的 EX: python bmi.py
    height=float(input('Height(cm): '))
    weight=float(input('Weight(kg): '))
    print('BMI is ',BMI(weight,height))

