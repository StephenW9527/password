

pwd = 'a123456'
# test = input('請輸入密碼：')
times = 3

# while True:      #  while times > 0  is much better
#     if test == pwd:
#         print('登入成功')
#         break
#     else:
#         times = times - 1
#         if times == 0:
#             print("已鎖卡 請洽發卡銀行")
#             break
#         else:
#             print('密碼錯誤! 還有', times, '次機會')
#             print('請重新輸入：')
#             test = input()
#             continue


# 老師寫法:
while times > 0:
    times = times - 1
    test = input('請輸入密碼：')
    if test == pwd:
        print('登入成功')
        break
    else:
        print('密碼錯誤!')
        if times > 0:
            print('密碼錯誤! 還有', times, '次機會')
        else:
            print("已鎖卡 請洽發卡銀行")
