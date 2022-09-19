import pickle


class Stadium:
    def __init__(self, stadium_name="Астана Арена", opening_date="2009 год", country="Казахстан",
                 city="Астана", capacity="30 200", get=""):
        self.text = None
        self.stadium_name = stadium_name  # название стадиона
        self.opening_date = opening_date  # дату открытия
        self.country = country  # страну
        self.city = city  # город
        self.capacity = capacity  # вместимость
        self.get = get

    def brief_information(self):
        self.text = (
            "Название стадиона: ", self.stadium_name, "Дата открытия: ", self.opening_date, "Страна: ", self.country, "Город: ",
            self.city)
        return self.text

    def full_information(self):
        self.text = (
            "Название стадиона: ", self.stadium_name, "Дата открытия: ", self.opening_date, "Страна: ", self.country, "Город: ",
            self.city, "Вместимость: ", self.capacity)
        return self.text

    def get_ser_info(self, get):
        '''
                    Аргументы подаются через пробел
                    Аргументы которые можно подать:
                        stadium_name \n
                        opening_date \n
                        country \n
                        city \n
                        capacity \n
        '''
        self.get = get.split(" ")

        self.giv_text_info = ""
        for i in self.get:
            # print(i)
            if i == "stadium_name":
                self.giv_text_info += f"Название стадиона: {self.stadium_name} \n"
            elif i == "opening_date":
                self.giv_text_info += f"Дата открытия: {self.opening_date} \n"
            elif i == "country":
                self.giv_text_info += f"Страна: {self.country} \n"
            elif i == "city":
                self.giv_text_info += f"Город: {self.city} \n"
            elif i == "capacity":
                self.giv_text_info += f"Вместимость: {self.capacity} \n"
        return self.giv_text_info

stadium = Stadium()
print(stadium.capacity)

stadium = Stadium(capacity="30 200")
print(stadium.capacity) 

print(stadium.brief_information())
print(stadium.full_information())

print(stadium.get_ser_info("stadium_name opening_date country"))
