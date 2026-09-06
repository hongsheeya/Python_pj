from collections import Counter
from datetime import datetime

from models import PrintedBook, EBook
from utils import (
    get_non_empty_input,
    get_positive_integer,
    get_menu_choice,
    format_datetime,
    log_error,
)


# 도서를 ISBN 기준으로 빠르게 조회하기 위해 딕셔너리를 사용합니다.
books = {}


# ISBN은 중복되면 안 되기 때문에 집합(set)을 사용합니다.
isbn_set = set()


# 대여/반납 이력을 순서대로 저장하기 위해 리스트를 사용합니다.
# 각 이력은 수정할 필요가 없으므로 튜플 형태로 저장합니다.
# 형식: (처리종류, ISBN, 도서명, 처리시간)
rental_history = []


def show_menu():
    print()
    print("=" * 50)
    print("              도서 관리 시스템")
    print("=" * 50)
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 검색")
    print("4. 대여 / 반납 처리")
    print("5. 통계 조회")
    print("6. 종료")
    print("=" * 50)


def register_book():
    print()
    print("[도서 등록]")
    print("1. 일반 도서")
    print("2. 전자 도서")

    book_type = get_menu_choice(
        "도서 종류를 선택하세요: ",
        {1, 2},
    )

    title = get_non_empty_input("도서명: ")
    author = get_non_empty_input("저자: ")
    isbn = get_non_empty_input("ISBN: ")

    if isbn in isbn_set:
        print("이미 등록된 ISBN입니다.")
        return

    try:
        if book_type == 1:
            pages = get_positive_integer("페이지 수: ")

            book = PrintedBook(
                title,
                author,
                isbn,
                pages,
            )

        else:
            file_format = get_non_empty_input(
                "전자도서 파일 형식(PDF, EPUB 등): "
            )

            book = EBook(
                title,
                author,
                isbn,
                file_format,
            )

        books[isbn] = book
        isbn_set.add(isbn)

        print()
        print("도서가 정상적으로 등록되었습니다.")
        print(book.get_details())

    except ValueError as error:
        print(f"도서 등록 실패: {error}")
        log_error(f"도서 등록 오류: {error}")

    except Exception as error:
        print("예상하지 못한 오류가 발생했습니다.")
        log_error(f"예상하지 못한 도서 등록 오류: {error}")


def show_all_books():
    print()
    print("[전체 도서 조회]")

    if not books:
        print("등록된 도서가 없습니다.")
        return

    for index, book in enumerate(books.values(), start=1):
        print(f"{index}. {book.get_details()}")

    print()
    print(f"총 {len(books)}권의 도서가 등록되어 있습니다.")


def search_books():
    print()
    print("[도서 검색]")
    print("1. 도서명 검색")
    print("2. 저자 검색")
    print("3. ISBN 검색")

    search_type = get_menu_choice(
        "검색 방법을 선택하세요: ",
        {1, 2, 3},
    )

    keyword = get_non_empty_input(
        "검색어를 입력하세요: "
    ).lower()

    results = []

    for book in books.values():

        if search_type == 1:
            if keyword in book.title.lower():
                results.append(book)

        elif search_type == 2:
            if keyword in book.author.lower():
                results.append(book)

        elif search_type == 3:
            if keyword in book.isbn.lower():
                results.append(book)

    print()
    print("[검색 결과]")

    if not results:
        print("검색 결과가 없습니다.")
        return

    for index, book in enumerate(results, start=1):
        print(f"{index}. {book.get_details()}")

    print(f"총 {len(results)}개의 도서를 찾았습니다.")


def borrow_book():
    print()
    print("[도서 대여]")

    isbn = get_non_empty_input(
        "대여할 도서의 ISBN: "
    )

    if isbn not in books:
        print("존재하지 않는 도서입니다.")
        log_error(
            f"존재하지 않는 도서 대여 시도 - ISBN: {isbn}"
        )
        return

    book = books[isbn]

    try:
        book.borrow()

        history = (
            "대여",
            book.isbn,
            book.title,
            format_datetime(),
        )

        rental_history.append(history)

        print(
            f"'{book.title}' 도서가 대여되었습니다."
        )

    except ValueError as error:
        print(f"대여 실패: {error}")
        log_error(
            f"도서 대여 실패 - ISBN: {isbn}, 오류: {error}"
        )


def return_book():
    print()
    print("[도서 반납]")

    isbn = get_non_empty_input(
        "반납할 도서의 ISBN: "
    )

    if isbn not in books:
        print("존재하지 않는 도서입니다.")
        log_error(
            f"존재하지 않는 도서 반납 시도 - ISBN: {isbn}"
        )
        return

    book = books[isbn]

    try:
        book.return_book()

        history = (
            "반납",
            book.isbn,
            book.title,
            format_datetime(),
        )

        rental_history.append(history)

        print(
            f"'{book.title}' 도서가 반납되었습니다."
        )

    except ValueError as error:
        print(f"반납 실패: {error}")
        log_error(
            f"도서 반납 실패 - ISBN: {isbn}, 오류: {error}"
        )


def rental_return_menu():
    print()
    print("[대여 / 반납]")
    print("1. 도서 대여")
    print("2. 도서 반납")
    print("3. 이전 메뉴")

    choice = get_menu_choice(
        "메뉴를 선택하세요: ",
        {1, 2, 3},
    )

    if choice == 1:
        borrow_book()

    elif choice == 2:
        return_book()


def show_rental_history():
    print()
    print("[대여 / 반납 이력]")

    if not rental_history:
        print("대여 또는 반납 이력이 없습니다.")
        return

    for index, history in enumerate(
        rental_history,
        start=1,
    ):
        action, isbn, title, processed_at = history

        print(
            f"{index}. "
            f"[{action}] "
            f"{title} | "
            f"ISBN: {isbn} | "
            f"{processed_at}"
        )


def show_most_borrowed_books():
    borrow_records = [
        history
        for history in rental_history
        if history[0] == "대여"
    ]

    print()
    print("[도서별 대여 횟수]")

    if not borrow_records:
        print("대여 기록이 없습니다.")
        return

    title_counter = Counter(
        history[2]
        for history in borrow_records
    )

    ranking = title_counter.most_common()

    for rank, (title, count) in enumerate(
        ranking,
        start=1,
    ):
        print(
            f"{rank}위. "
            f"{title} - "
            f"{count}회"
        )


def show_monthly_statistics():
    print()
    print("[월별 대여 통계]")

    monthly_count = {}

    for history in rental_history:

        action, isbn, title, processed_at = history

        if action != "대여":
            continue

        try:
            date = datetime.strptime(
                processed_at,
                "%Y-%m-%d %H:%M:%S",
            )

            month = date.strftime("%Y-%m")

            monthly_count[month] = (
                monthly_count.get(month, 0) + 1
            )

        except ValueError as error:
            log_error(
                f"대여 이력 날짜 변환 오류: {error}"
            )

    if not monthly_count:
        print("대여 기록이 없습니다.")
        return

    for month in sorted(monthly_count):
        print(
            f"{month}: "
            f"{monthly_count[month]}회 대여"
        )


def show_current_status():
    total = len(books)

    borrowed = sum(
        1
        for book in books.values()
        if book.is_borrowed
    )

    available = total - borrowed

    print()
    print("[현재 도서 현황]")
    print(f"전체 도서: {total}권")
    print(f"대여 가능: {available}권")
    print(f"대여 중: {borrowed}권")


def statistics_menu():
    while True:
        print()
        print("[통계 조회]")
        print("1. 전체 대여 / 반납 이력")
        print("2. 도서별 대여 순위")
        print("3. 월별 대여 통계")
        print("4. 현재 도서 현황")
        print("5. 이전 메뉴")

        choice = get_menu_choice(
            "메뉴를 선택하세요: ",
            {1, 2, 3, 4, 5},
        )

        if choice == 1:
            show_rental_history()

        elif choice == 2:
            show_most_borrowed_books()

        elif choice == 3:
            show_monthly_statistics()

        elif choice == 4:
            show_current_status()

        elif choice == 5:
            break


def main():
    print("=" * 50)
    print("도서 관리 시스템을 시작합니다.")
    print("=" * 50)

    while True:

        try:
            show_menu()

            choice = get_menu_choice(
                "메뉴를 선택하세요: ",
                {1, 2, 3, 4, 5, 6},
            )

            if choice == 1:
                register_book()

            elif choice == 2:
                show_all_books()

            elif choice == 3:
                search_books()

            elif choice == 4:
                rental_return_menu()

            elif choice == 5:
                statistics_menu()

            elif choice == 6:
                print()
                print("도서 관리 시스템을 종료합니다.")
                break

        except KeyboardInterrupt:
            print()
            print()
            print("사용자에 의해 프로그램이 종료되었습니다.")
            break

        except Exception as error:
            print()
            print("프로그램 실행 중 오류가 발생했습니다.")
            print("다시 시도해주세요.")

            log_error(
                f"메인 프로그램 오류: "
                f"{type(error).__name__} - {error}"
            )


if __name__ == "__main__":
    main()