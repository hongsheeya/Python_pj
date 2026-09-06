from datetime import datetime


def get_non_empty_input(message):
    """
    공백 입력을 방지하는 함수입니다.
    값이 정상적으로 입력될 때까지 반복해서 입력받습니다.
    """

    while True:
        value = input(message).strip()

        if value:
            return value

        print("잘못된 입력입니다. 값을 입력해주세요.")


def get_positive_integer(message):
    """
    양의 정수만 입력받는 함수입니다.

    숫자가 아닌 값을 입력했을 때 발생하는 ValueError를
    try-except로 처리합니다.
    """

    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("1 이상의 숫자를 입력해주세요.")
                continue

            return value

        except ValueError:
            print("숫자만 입력해주세요.")


def get_menu_choice(message, valid_choices):
    """
    메뉴 번호 입력을 검증하는 함수입니다.
    valid_choices에 포함된 숫자만 입력받습니다.
    """

    while True:
        try:
            choice = int(input(message))

            if choice not in valid_choices:
                print("메뉴에 있는 번호를 입력해주세요.")
                continue

            return choice

        except ValueError:
            print("숫자를 입력해주세요.")


def format_datetime():
    """
    현재 시간을 문자열 형태로 반환합니다.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_error(error_message):
    """
    프로그램 실행 중 발생한 오류를 error.log 파일에 기록합니다.
    """

    current_time = format_datetime()

    try:
        with open("error.log", "a", encoding="utf-8") as file:
            file.write(f"[{current_time}] {error_message}\n")

    except OSError:
        print("오류 로그 파일을 작성할 수 없습니다.")