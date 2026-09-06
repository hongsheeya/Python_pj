def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("값을 입력해주세요.")


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value
            else:
                print("1 이상의 숫자를 입력해주세요.")

        except ValueError:
            print("숫자를 입력해주세요.")


def get_menu_choice(message, choices):
    while True:
        try:
            choice = int(input(message))

            if choice in choices:
                return choice
            else:
                print("올바른 메뉴 번호를 입력해주세요.")

        except ValueError:
            print("숫자를 입력해주세요.")