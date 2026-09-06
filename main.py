from models import PrintedBook, EBook
from utils import (
    get_non_empty_input,
    get_positive_integer,
    get_menu_choice,
)


books = {}
isbn_set = set()
rental_history = []


def show_menu():
    print()
    print("===== 도서 관리 시스템 =====")
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 검색")
    print("4. 대여 / 반납 처리")
    print("5. 종료")
    print("6. 통계 조회")


def register_book():
    print()
    print("[도서 등록]")
    print("1. 일반 도서")
    print("2. 전자 도서")

    book_type = get_menu_choice(
        "도서 종류를 선택하세요: ",
        {1, 2}
    )

    title = get_non_empty_input("도서명: ")
    author = get_non_empty_input("저자: ")
    isbn = get_non_empty_input("ISBN: ")

    if isbn in isbn_set:
        print("이미 등록된 ISBN입니다.")
        return

    if book_type == 1:
        pages = get_positive_integer("페이지 수: ")
        book = PrintedBook(title, author, isbn, pages)

    else:
        file_format = get_non_empty_input("파일 형식: ")
        book = EBook(title, author, isbn, file_format)

    books[isbn] = book
    isbn_set.add(isbn)

    print("도서가 등록되었습니다.")


def show_all_books():
    print()
    print("[전체 도서 조회]")

    if len(books) == 0:
        print("등록된 도서가 없습니다.")
        return

    for book in books.values():
        print(book.get_details())


def search_books():
    print()
    print("[도서 검색]")
    print("1. 도서명")
    print("2. 저자")
    print("3. ISBN")

    search_type = get_menu_choice(
        "검색 방법을 선택하세요: ",
        {1, 2, 3}
    )

    keyword = get_non_empty_input("검색어를 입력하세요: ")
    keyword = keyword.lower()

    results = []

    for book in books.values():
        if search_type == 1:
            if keyword in book.get_title().lower():
                results.append(book)

        elif search_type == 2:
            if keyword in book.get_author().lower():
                results.append(book)

        elif search_type == 3:
            if keyword in book.get_isbn().lower():
                results.append(book)

    if len(results) == 0:
        print("검색 결과가 없습니다.")
        return

    print()
    print("[검색 결과]")

    for book in results:
        print(book.get_details())


def borrow_book():
    print()
    print("[도서 대여]")

    isbn = get_non_empty_input("대여할 도서의 ISBN: ")

    if isbn not in books:
        print("존재하지 않는 도서입니다.")
        return

    book = books[isbn]

    if book.borrow():
        print(f"{book.get_title()} 대여 완료")

        history = (
            "대여",
            book.get_isbn(),
            book.get_title()
        )

        rental_history.append(history)

    else:
        print("이미 대여 중인 도서입니다.")


def return_book():
    print()
    print("[도서 반납]")

    isbn = get_non_empty_input("반납할 도서의 ISBN: ")

    if isbn not in books:
        print("존재하지 않는 도서입니다.")
        return

    book = books[isbn]

    if book.return_book():
        print(f"{book.get_title()} 반납 완료")

        history = (
            "반납",
            book.get_isbn(),
            book.get_title()
        )

        rental_history.append(history)

    else:
        print("현재 대여 중인 도서가 아닙니다.")


def rental_menu():
    print()
    print("[대여 / 반납 처리]")
    print("1. 도서 대여")
    print("2. 도서 반납")
    print("3. 이전 메뉴")

    choice = get_menu_choice(
        "메뉴를 선택하세요: ",
        {1, 2, 3}
    )

    if choice == 1:
        borrow_book()

    elif choice == 2:
        return_book()


def show_rental_history():
    print()
    print("[대여 / 반납 이력]")

    if len(rental_history) == 0:
        print("대여 또는 반납 기록이 없습니다.")
        return

    for history in rental_history:
        print(
            f"{history[0]} | "
            f"ISBN: {history[1]} | "
            f"도서명: {history[2]}"
        )


def show_most_borrowed_book():
    print()
    print("[가장 많이 대여된 도서]")

    borrow_count = {}

    for history in rental_history:
        if history[0] == "대여":
            title = history[2]

            if title in borrow_count:
                borrow_count[title] += 1
            else:
                borrow_count[title] = 1

    if len(borrow_count) == 0:
        print("대여 기록이 없습니다.")
        return

    max_count = 0

    for count in borrow_count.values():
        if count > max_count:
            max_count = count

    for title, count in borrow_count.items():
        if count == max_count:
            print(f"{title}: {count}회")


def statistics_menu():
    print()
    print("[통계 조회]")
    print("1. 대여 / 반납 이력")
    print("2. 가장 많이 대여된 도서")
    print("3. 이전 메뉴")

    choice = get_menu_choice(
        "메뉴를 선택하세요: ",
        {1, 2, 3}
    )

    if choice == 1:
        show_rental_history()

    elif choice == 2:
        show_most_borrowed_book()


def main():
    while True:
        show_menu()

        choice = get_menu_choice(
            "메뉴를 선택하세요: ",
            {1, 2, 3, 4, 5, 6}
        )

        if choice == 1:
            register_book()

        elif choice == 2:
            show_all_books()

        elif choice == 3:
            search_books()

        elif choice == 4:
            rental_menu()

        elif choice == 5:
            print("프로그램을 종료합니다.")
            break

        elif choice == 6:
            statistics_menu()


if __name__ == "__main__":
    main()