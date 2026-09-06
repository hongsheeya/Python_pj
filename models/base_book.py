class BaseBook:

    def __init__(self, title, author, isbn):
        if not title.strip():
            raise ValueError("도서명은 비어 있을 수 없습니다.")

        if not author.strip():
            raise ValueError("저자명은 비어 있을 수 없습니다.")

        if not isbn.strip():
            raise ValueError("ISBN은 비어 있을 수 없습니다.")

        self.__title = title.strip()
        self.__author = author.strip()
        self.__isbn = isbn.strip()
        self.__is_borrowed = False

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        if self.__is_borrowed:
            raise ValueError("이미 대여 중인 도서입니다.")

        self.__is_borrowed = True

    def return_book(self):
        if not self.__is_borrowed:
            raise ValueError("현재 대여 중인 도서가 아닙니다.")

        self.__is_borrowed = False

    def get_status(self):
        if self.__is_borrowed:
            return "대여 중"

        return "대여 가능"

    def get_details(self):
        return (
            f"도서명: {self.__title} | "
            f"저자: {self.__author} | "
            f"ISBN: {self.__isbn} | "
            f"상태: {self.get_status()}"
        )

    def __str__(self):
        return self.get_details()