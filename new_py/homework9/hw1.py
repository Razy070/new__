import json

import openpyexcel

import requests

url = "https://jsonplaceholder.typicode.com/todos/"


class My_json(object):
    def __init__(self):
        self.url = "https://jsonplaceholder.typicode.com/todos/"
        self.json_list = []

    def method_get(self, url_id):
        for idd in range(1, url_id + 1):
            req = requests.get(f"{self.url}{idd}").json()
            self.json_list.append(req)
        return self.json_list

    def method_save(self, data):
        with open("data_file.json", "w") as write_file:
            json.dump(data, write_file)

    def method_save_separately(self, data):
        print(data[0])
        for i in data:
            with open(f"data_file{data.index(i) + 1}.json", "w") as write_file:
                json.dump(i, write_file)

    def method_load_json_from_file(self, urls: list):
        list_json = []
        for i in urls:
            with open(f"{i}", "r") as read_file:
                data = json.load(read_file)
                list_json.append(data)
        return list_json

    def method_save_in_exel(self, data:list):
        workbook = openpyexcel.load_workbook("data.xlsx")
        worksheet = workbook.active
        max_row = worksheet.max_row
        worksheet.cell(row=1, column=1, value=str(data))
        for i in data:
            worksheet.cell(row=2, column=data.index(i)+1, value=str(i))
        workbook.save("data.xlsx")
        workbook.close()
