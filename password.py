

pwd = 'a123456'
print('請輸入密碼：')
test = input()
times = 3

while True:
    if test == pwd:
        print('登入成功')
        break
    else:
        times = times - 1
        if times == 0:
            print("已鎖卡 請洽發卡銀行")
            break
        else:
            print('密碼錯誤! 還有', times, '次機會')
            print('請重新輸入：')
            test = input()
            continue
