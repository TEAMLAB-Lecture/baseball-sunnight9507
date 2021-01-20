# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    """
    Input:
      - user_input_number : 문자열 값
    Output:
      - user_input_number가 정수로 변환 가능할 경우는 True,
        그렇지 않을 경우는 False
    Examples:
      >>> import baseball_game as bg
      >>> bg.is_digit("551")
      True
      >>> bg.is_digit("103943")
      True
      >>> bg.is_digit("472")
      True
      >>> bg.is_digit("1032.203")
      False
      >>> bg.is_digit("abc")
      False
    """

    result = user_input_number.isdigit()
    return result


def is_between_100_and_999(user_input_number):
    """
    Input:
      - user_input_number : 문자열 값
                            입력된 값은 숫자형태의 문자열 값임이 보장된다.
    Output:
      - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
        그렇지 않을 경우는 False
    Examples:
      >>> import baseball_game as bg
      >>> bg.is_between_100_and_999("551")
      True
      >>> bg.is_between_100_and_999("103943")
      False
      >>> bg.is_between_100_and_999("472")
      True
      >>> bg.is_between_100_and_999("0")
      False
    """

    user_input_number_to_int = int(user_input_number)
    upper_100 = True if user_input_number_to_int >= 100 else False
    under_1000 = True if user_input_number_to_int < 1000 else False
    result = upper_100 and under_1000
    return result


def is_duplicated_number(three_digit):
    """
    Input:
      - three_digit : 문자열로 된 세자리 양의 정수 값
                      문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    Output:
      - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
        그렇지 않을 경우는 False
      ex) 117 - True, 123 - False, 103 - False, 113 - True
    Examples:
      >>> import baseball_game as bg
      >>> bg.is_duplicated_number("551")
      True
      >>> bg.is_duplicated_number("402")
      False
      >>> bg.is_duplicated_number("472")
      False
      >>> bg.is_duplicated_number("100")
      True
    """

    number1, number2, number3 = three_digit
    result = (number1 == number2) or (number1 == number3) or (number2 == number3)
    return result


def is_validated_number(user_input_number):
    """
    Input:
      - user_input_number : 문자열 값
    Output:
      - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
           1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    Examples:
      >>> import baseball_game as bg
      >>> bg.is_validated_number("amvd")
      False
      >>> bg.is_validated_number("402")
      True
      >>> bg.is_validated_number("472")
      True
      >>> bg.is_validated_number("100")
      False
      >>> bg.is_validated_number("1000")
      False
    """

    # 1) 숫자형 문자열
    if not is_digit(user_input_number):
        return False
    # 2) 100이상 1000미만
    if not is_between_100_and_999(user_input_number):
        return False
    # 3) 중복되는 숫자가 없을 경우
    if is_duplicated_number(user_input_number):
        return False
    return True


def get_not_duplicated_three_digit_number():
    """
    Input:
      - None : 입력값이 없음
    Output:
      - 중복되는 숫자가 없는 3자리 정수값을 랜덤하게 생성하여 반환함
        정수값으로 문자열이 아님
    Examples:
      >>> import baseball_game as bg
      >>> bg.get_not_duplicated_three_digit_number()
      125
      >>> bg.get_not_duplicated_three_digit_number()
      634
      >>> bg.get_not_duplicated_three_digit_number()
      583
      >>> bg.get_not_duplicated_three_digit_number()
      381
    """

    check_is_duplicated_number = True
    while check_is_duplicated_number:
        random_number = get_random_number()
        check_is_duplicated_number = is_duplicated_number(str(random_number))
    return random_number


def get_strikes_or_ball(user_input_number, random_number):
    """
    Input:
      - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
      - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    Output:
      - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
      변환 규칙은 아래와 같음
      - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
        한 숫자와 자릿수가 모두 일치하면 1 Strike
      - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
      - 세자리 숫자를 정확히 입력하면 3 Strike
    Examples:
      >>> import baseball_game as bg
      >>> bg.get_strikes_or_ball("123", "472")
      [0, 1]
      >>> bg.get_strikes_or_ball("547", "472")
      [0, 2]
      >>> bg.get_strikes_or_ball("247", "472")
      [0, 3]
      >>> bg.get_strikes_or_ball("742", "472")
      [1, 2]
      >>> bg.get_strikes_or_ball("472", "472")
      [3, 0]
    """

    strikes, ball = 0, 0
    for index, user_number in enumerate(user_input_number):
        if user_number in random_number:
            if user_number == random_number[index]:
              strikes += 1
            else:
              ball += 1
    return [strikes, ball]


def is_yes(one_more_input):
    """
    Input:
      - one_more_input : 문자열값으로 사용자가 입력하는 문자
    Output:
      - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
        그렇지 않을 경우 False를 반환함
    Examples:
      >>> import baseball_game as bg
    >>> bg.is_yes("Y")
    True
    >>> bg.is_yes("y")
    True
    >>> bg.is_yes("Yes")
    True
    >>> bg.is_yes("YES")
    True
    >>> bg.is_yes("abc")
    False
    >>> bg.is_yes("213")
    False
    >>> bg.is_yes("4562")
    False
    """

    yes_set = {"Y", "YES"}
    input_string = one_more_input.upper()
    result = input_string in yes_set
    return result


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    no_set = {"N", "NO"}
    input_string = one_more_input.upper()
    result = input_string in no_set
    return result


def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)

    # ===Modify codes below=============
    do_game = True
    while do_game:
        user_input = input("Input guess number : ")
        # "0" 입력
        if user_input == "0":
            break
        # game 가능한 input
        elif is_validated_number(user_input):
            strikes, balls = get_strikes_or_ball(user_input, random_number)
            print(f"Strikes : {strikes}, Balls : {balls}")
            # 3 strikes
            if strikes == 3:
                input_is_yes, input_is_no = False, False
                while not (input_is_yes or input_is_no):
                    user_input_more_game = input("You win, one more(Y/N)?")
                    input_is_yes = is_yes(user_input_more_game)
                    input_is_no = is_no(user_input_more_game)
                    # game again
                    if input_is_yes:
                        random_number = str(get_not_duplicated_three_digit_number())
                        print("Random Number is : ", random_number)
                    # stop game
                    elif input_is_no:
                        do_game = False
                    else:
                        print("Wrong Input, Input again")
        # game 가능하지 않은 input
        else:
            print("Wrong Input, Input again")

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
