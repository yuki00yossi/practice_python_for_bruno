# 数字を入力
while True:
 try:
  number1 = int(input('一つ目の数字を入力してください‐‐≫'))
  number2 = int(input('二つ目の数字を入力してください‐‐≫'))
  number3 = int(input('三つ目の数字を入力してください‐‐≫'))
 except ValueError:
    print('数字以外が入力されました。数字のみを入力してください')
    continue
 if number1 or number2 or number3 < 2:
     print('入力値が不正です。再度入力してください')
     continue
 elif number1 == number2 :
     print('入力値が不正です。再度入力してください')
     continue
 elif number1 or number2 > number3:
     print('入力値が不正です。再度入力してください')
     continue
 else:
    # 出力する数字のデフォルト
    i = 1
    # 数字を判定して、数字の倍数ごとに「buzz」「fizz」「buzzfizz」を表示する
    while i in range(1,number3 + 1):

    # 出力された数字がnumber1かnumber2のいずれかもしくは両方の倍数だった場合は「buzz」「fizz」を表示する
        if number1 and number2:
            if i % number1 == 0 and i % number2 == 0:
                print('fizzbuzz!')

            elif i % number1 == 0:
                print('Fizz!')
            
            elif i % number2 == 0:
                print('Buzz!')

            else:
                print(i)
            i += 1

        else:
            print(number3)
            break


# while i in range(1,number3 + 1):
#  if  number1 % i == 0:
#   print('Fizz!')
#   i += 1
#  elif number2 % i == 0:
#   print('Buzz!')
#   i += 1
#  elif number1 % i and number2 % i != 0:  
#   print('fizzbuzz!')
#   i += 1
#  elif number1 % i != 0:
#   print(i)
#   i += 1
#  elif number2 % i != 0:
#   print(i)
#   i += 1
#  else:
#   print(number3)
#   break