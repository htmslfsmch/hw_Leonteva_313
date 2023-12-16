class Book:
    def __init__(self, name: str, author: str, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def print_info(self):
        print(
            f"О книге {self.name}:\t Автор: {self.author}, Год издания: {self.year}, Количество страниц: {self.pages}")

    def set_pages(self, new_pages: int):
        self.pages = new_pages

    def __str__(self):
        return f"{self.name}, {self.author}, {self.year}, {self.pages}"


book1 = Book("Бойцовский клуб", "Чак Паланик", 1996, 256)
book2 = Book("Яма", "Александр Куприн", 1915, 416)

book1.print_info()
book2.print_info()

book1.set_pages(100)
book2.set_pages(100)

print("\nУстановили новые значения для pages")

book1.print_info()
book2.print_info()

print("\n", book1, book2, sep="\n")
