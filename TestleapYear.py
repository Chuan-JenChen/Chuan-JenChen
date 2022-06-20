leapYear = int(input("西元年"))           # 使用變數 year 紀錄使用者輸入的年份
if (leapYear%4 == 0):                    # 如果除以 4 能整除
    if (leapYear%100 == 0):              # 如果除以 100 能整除
        if (leapYear%400 == 0):          # 如果除以 400 能整除，就是閏年
            print(f'{leapYear} 是閏年')
        else:
            print(f'{leapYear} 是平年')
    else:
      print(f'{leapYear} 是閏年')
else:
    print(f'{leapYear} 是平年')