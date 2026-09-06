from .base_book import BaseBook


class PrintedBook(BaseBook):
    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)
        self.__pages = pages

    def get_details(self):
        return (
            f"[일반 도서] "
            f"도서명: {self.get_title()}, "
            f"저자: {self.get_author()}, "
            f"ISBN: {self.get_isbn()}, "
            f"페이지: {self.__pages}, "
            f"상태: {self.get_status()}"
        )


class EBook(BaseBook):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.__file_format = file_format

    def get_details(self):
        return (
            f"[전자 도서] "
            f"도서명: {self.get_title()}, "
            f"저자: {self.get_author()}, "
            f"ISBN: {self.get_isbn()}, "
            f"파일 형식: {self.__file_format}, "
            f"상태: {self.get_status()}"
        )