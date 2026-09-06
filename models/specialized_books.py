from .base_book import BaseBook


class PrintedBook(BaseBook):

    def __init__(self, title, author, isbn, pages):
        super().__init__(title, author, isbn)

        if pages <= 0:
            raise ValueError("페이지 수는 1 이상이어야 합니다.")

        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    def get_details(self):

        return (
            f"[일반 도서] "
            f"도서명: {self.title} | "
            f"저자: {self.author} | "
            f"ISBN: {self.isbn} | "
            f"페이지: {self.__pages}쪽 | "
            f"상태: {self.get_status()}"
        )


class EBook(BaseBook):

    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)

        if not file_format.strip():
            raise ValueError("파일 형식은 비어 있을 수 없습니다.")

        self.__file_format = file_format.strip().upper()

    @property
    def file_format(self):
        return self.__file_format

    def get_details(self):
        
        return (
            f"[전자 도서] "
            f"도서명: {self.title} | "
            f"저자: {self.author} | "
            f"ISBN: {self.isbn} | "
            f"파일 형식: {self.__file_format} | "
            f"상태: {self.get_status()}"
        )