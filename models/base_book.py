class BaseBook:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_status(self):
        if self.__is_borrowed:
            return "대여 중"
        else:
            return "대여 가능"

    def borrow(self):
        if self.__is_borrowed:
            return False

        self.__is_borrowed = True
        return True

    def return_book(self):
        if not self.__is_borrowed:
            return False

        self.__is_borrowed = False
        return True

    def get_details(self):
        return (
            f"도서명: {self.__title}, "
            f"저자: {self.__author}, "
            f"ISBN: {self.__isbn}, "
            f"상태: {self.get_status()}"
        )