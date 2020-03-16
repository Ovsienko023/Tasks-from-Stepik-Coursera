import os
import csv


class CarBase(object):

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super(Car, self).__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super(Truck, self).__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl or 0
        try:
            self.body_length, self.body_width, self.body_height = \
                map(float, self.body_whl.split('x')) if self.body_whl else [0.0 for _ in range()]
        except (ValueError, TypeError):
            self.body_length, self.body_width, self.body_height = (0.0, 0.0, 0.0)
          


    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list_obj = []
    csv.register_dialect('customcsv', delimiter=';', quoting=csv.QUOTE_NONE, quotechar='', escapechar='\\')
    with open(csv_filename, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, 'customcsv')
        next(reader)
        for row in reader:
            
            try:
                row[0]
            except:
                continue
            if row[0] == '':
                car_list_obj.append([])

            elif len(row) == 7:
                
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if car_type == 'car' and all((brand, photo_file_name)):
                    try:
                        car_list_obj.append(Car(brand, photo_file_name, float(carrying), int(passenger_seats_count)))
                    except ValueError:
                        pass
                elif car_type == 'truck' and all((brand, photo_file_name)):
                    try:
                        car_list_obj.append(Truck(brand, photo_file_name, float(carrying), body_whl))
                    except ValueError:
                        pass
                elif car_type == 'spec_machine' and all((brand, photo_file_name, extra)):
                    try:
                        car_list_obj.append(SpecMachine(brand, photo_file_name, float(carrying), extra))
                    except ValueError:
                        pass
        # print()
        # print(car_list_obj)
        #print(car_list_obj)
        car_list_obj = list(filter(None, car_list_obj))
    return car_list_obj

a = get_car_list("cars.csv")
# # #car = Truck('Toyota', 't2.jpeg', '3.0', '3.7x2x2.6x6')
print(a)

# print(a[0])

# if [] in a:
#     print("!")
#     a = []
#     print(a)


# mylist = [[], ['a'], ['1']]

# c = list(filter(None, mylist))
# print(c)