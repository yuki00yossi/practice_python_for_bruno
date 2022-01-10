""" FizzBuzzアプリ サンプル"""


def main():
    print_fizzbuzz(input_numbers())


def input_numbers():
    """
    入力値を受け取る

    標準入力から値を３つ受け取って、バリデーションを実行。
    バリデーションに成功するまで繰り返し入力を受け付ける。

    Returns
    -------
    validated_data : list
        バリデーション済みの３つの入力値を格納したリスト
        [fizz_num, buzz_num, max_num]
    """
    while True:
        fizz_num = input("Fizzの値を入力してください。: ")
        buzz_num = input("Buzzの値を入力してください。: ")
        max_num = input("出力する最大値を入力してください。: ")
        # バリデーション呼び出し
        validated_data = valid_data(fizz_num, buzz_num, max_num)
        if not validated_data:
            print("入力された数値が不正です。もう一度入力してください。")
            continue
        break
    return validated_data


def valid_data(fizz_num, buzz_num, max_num):
    """
    入力値をバリデーションする

    Parameters
    ----------
    fizz_num : String
        Fizzと出力する数
    buzz_num : String
        Buzzと出力する数
    max_num : String
        出力する最大値

    Returns
    -------
    validated_data : list or False
        バリデーション済みの３つの入力値を格納したリスト、バリデーション失敗時はFalseを返す
        [fizz_num, buzz_num, max_num]
    """

    values = [fizz_num, buzz_num, max_num]
    try:
        # 整数値か判定
        int_values = [int(i) for i in values]
    except ValueError:
        return False
    # 数字が２以上か判定
    if not all(value >= 2 for value in int_values):
        return False
    if int_values[0] == int_values[1]:
        return False
    if int_values[2] < int_values[0] or int_values[2] < int_values[1]:
        return False
    return int_values


def print_fizzbuzz(list_numbers):
    """
    FizzBuzzの出力を行う

    Parameters
    ----------
    list_numbers : list
        ３つの入力値を格納したリスト
    """
    fizz_number = list_numbers[0]
    buzz_number = list_numbers[1]
    max_num = list_numbers[2]

    for i in range(1, max_num + 1):
        if i % fizz_number == 0 and i % buzz_number == 0:
            print('FizzBuzz!')
        elif i % fizz_number == 0:
            print('Fizz!')
        elif i % buzz_number == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == "__main__":
    main()
