for num in range(1, 101):
    string = ''

    # ここから記述
    # 15の倍数かどうか判断
    if(num%15 == 0):
        string = 'FizzBuzz'
    # 5の倍数かどうか判断
    elif(num%5 == 0):
        string = 'Buzz'
    # 3の倍数かどうか判断
    elif(num%3 == 0):
        string = 'Fizz'
    # その他
    else:
        string = num
    # ここまで記述

    print(string)
