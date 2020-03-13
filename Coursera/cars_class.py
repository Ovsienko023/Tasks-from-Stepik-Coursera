import os


class CarBase:
    def __init__(self, brand=None, photo_file_name=None, carrying=None):
        self.brand = brand 
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_car_file_ext(self):
        authorized = ['.jpg', '.jpeg', '.png', '.gif']
        resoult = os.path.splitext(self.photo_file_name)

        if resoult[1] in authorized:
            return resoult[1]
        else:
            return None
        

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=None):
        super().__init__(brand, photo_file_name, carrying)
        self.photo_file_name = photo_file_name


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        print(body_whl, '!')
        if self.body_whl:
            l, w ,h = self.body_whl.split('x')
        
            
        self.body_length = float(l) or 0
        self.body_width = float(w) or 0
        self.body_height = float(h) or 0

    def get_body_volume(self):
        volume = self.body_length * self.body_width * self.body_height
        return volume
        


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        


def get_car_list(csv_filename):
    car_list = []
    return car_list




new_truck = Truck('Man', 'f2.png', '20', '')
#new_car = Car('Nissan xTtrail', 'f1.jpeg', '2.5','4')
print(new_truck.get_body_volume())


# print(new_car.__dict__)
print(new_truck.__dict__)




# def get_car_list(neme_file):
#     lst_car = list()
#     with open(neme_file) as file_csv:
#         name_data = file_csv.readline().rstrip().split(';')
#         data_text = csv.reader(file_csv, delimiter=';')
        
#         for car in data_text:
#             if not car or not car[0]:
#                 continue     
#             lst_car.append({name_data[0]: car[0], name_data[1]: car[1], 
#                             name_data[2]: car[2], name_data[3]: car[3], 
#                             name_data[4]: car[4], name_data[5]: car[5], 
#                             name_data[6]: car[6],})

#         lst_object = list()       
#         for car in lst_car:
#             if car['car_type'] == 'car':
#                 obj_car = Car(**car)
#                 lst_object.append(obj_car)
#             elif car['car_type'] == 'truck':
#                 obj_car = Truck(**car)
#                 lst_object.append(obj_car)
#             elif car['car_type'] == 'spec_machine':
#                 obj_car = SpecMachine(**car)
#                 lst_object.append(obj_car)
#         print(lst_car[0])
#         for i in lst_car[0].values:
#             print(i, end="")
#         return lst_object
        

  
        
# def main():         
#     get_car_list('cars.csv')