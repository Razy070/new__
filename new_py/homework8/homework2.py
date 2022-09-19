import pickle


class Book:
    def __init__(self, book_title="Серия романов о Гарри Поттере", year_of_issue="1997 год",
                 publisher="Первоначально главными издателями книг являлись Bloomsbury в Великобритании и Scholastic Press[en] в США.",
                 genre="серия романов, написанная британской писательницей Дж. К. Роулинг", author="Дж. К. Роулинг",
                 price="30 000 тг", get=""):
        self.text = None
        self.book_title = book_title  # название книги
        self.year_of_issue = year_of_issue  # год выпуска
        self.publisher = publisher  # издателя
        self.genre = genre  # жанр
        self.author = author  # автора
        self.price = price  # цена
        self.get = get

    def information_on_the_plate(self):
        self.text = (
            "Название книги: ", self.book_title, "Год выпуска: ", self.year_of_issue, "Издатели: ", self.publisher,
            "Цена: ",
            self.price)
        return self.text

    def detailed_information_on_the_website(self):
        self.text = (
            "Название книги: ", self.book_title, "Год выпуска: ", self.year_of_issue, "Издатели: ", self.publisher,
            "Цена: ",
            self.price, "Жанр: ", self.genre, "Авторы: ", self.author)
        return self.text

    def get_ser_info(self, get):
        '''
                    Аргументы подаются через пробел
                    Аргументы которые можно подать:
                        book_title \n
                        year_of_issue \n
                        publisher \n
                        genre \n
                        author \n
                        price \n
        '''
        self.get = get.split(" ")

        self.giv_text_info = ""
        for i in self.get:
            # print(i)
            if i == "book_title":
                self.giv_text_info += f"Название книги: {self.book_title} \n"
            elif i == "year_of_issue":
                self.giv_text_info += f"Год выпуска: {self.year_of_issue} \n"
            elif i == "publisher":
                self.giv_text_info += f"Издатели: {self.publisher} \n"
            elif i == "genre":
                self.giv_text_info += f"Жанр: {self.genre} \n"
            elif i == "author":
                self.giv_text_info += f"Авторы: {self.author} \n"
            elif i == "price":
                self.giv_text_info += f"Цена: {self.price} \n"
        return self.giv_text_info

    def get_ser_info_book_price(self):
        info_price = pickle.dumps(book.price)
        info_price_object = pickle.loads(info_price)
        return info_price_object


# exec
book = Book()
print(book.price)

book = Book(price="30 000 тг")  # ввод (замена)
print(book.price)  # Вывод

print(book.information_on_the_plate())
print(book.detailed_information_on_the_website())

print(book.get_ser_info("book_title year_of_issue publisher"))

print(book.get_ser_info_book_price())
