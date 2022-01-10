# 数字を入力
while True:
    try:
        number1 = int(input('一つ目の数字を入力してください‐‐≫'))
        number2 = int(input('二つ目の数字を入力してください‐‐≫'))
        number3 = int(input('三つ目の数字を入力してください‐‐≫'))
    except ValueError:
        print('数字以外が入力されました。数字のみを入力してください')
        continue
    if number1 < 2 or number2 < 2 or number3 < 2:
        print('入力値が不正です。再度入力してください')
        continue
    elif number1 == number2 :
        print('入力値が不正です。再度入力してください')
        continue
    elif number1 > number3 or number2 > number3:
        print('入力値が不正です。再度入力してください')
        continue
    else:
        break


# 数字を判定して、数字の倍数ごとに「buzz」「fizz」「buzzfizz」を表示する
for i in range(1,number3 + 1):

# 出力された数字がnumber1かnumber2のいずれかもしくは両方の倍数だった場合は「buzz」「fizz」を表示する
    
    if i % number1 == 0 and i % number2 == 0:
        print('fizzbuzz!')

    elif i % number1 == 0:
        print('Fizz!')

    elif i % number2 == 0:
        print('Buzz!')

    elif i % number1 != 0 and number2 != 0:
        print(i)
    else:
        print(number3)
        break
    i += 1
