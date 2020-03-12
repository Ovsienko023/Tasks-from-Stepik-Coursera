import os
import csv


def get_car_list():
    with open('cars.csv') as file_csv:
        data_text = csv.reader(file_csv)

        for car in data_text:
            print(car)
     
get_car_list()





path = r'D:\Programming\Git\Tasks-from-Stepik-Coursera\Coursera\week_2_decorator_to_json.py'
a = os.path.splitext(path)
