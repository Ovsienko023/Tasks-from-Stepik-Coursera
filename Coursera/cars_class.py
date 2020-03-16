import os
import csv


class CarBase:
    def __init__(self, car_type=None, brand=None, photo_file_name=None, carrying=None):
        self.car_type = car_type
        self.brand = brand 
        self.photo_file_name = photo_file_name
        self.carring = carrying 


    def get_photo_file_ext(self):
        authorized = ['.jpg', '.jpeg', '.png', '.gif']
        resoult = os.path.splitext(self.photo_file_name)

        if resoult[1] in authorized:
            return resoult[1]
        else:
            return None
        

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=None, body_whl=None, extra=None):
        super().__init__(brand, carrying, photo_file_name)
        self.passenger_seats_count = passenger_seats_count
        
        print(self.carrying)
a = Car('f4','qw.png','2.5')

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl=None, passenger_seats_count=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl or 0
        if body_whl:
            whl = self.body_whl.split('x')
            #print(whl)
        else:
            whl = [0,0,0]          
        self.body_length = whl[0] or 0
        self.body_width = whl[1] or 0
        self.body_height = whl[2] or 0
      

    def get_body_volume(self):
        volume = float(self.body_length) * float(self.body_width) * float(self.body_height)
        return volume
        


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=None, body_whl=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        


def get_car_list(neme_file):
    lst_car = list()
    with open(neme_file) as file_csv:
        name_data = file_csv.readline().rstrip().split(';')
        data_text = csv.reader(file_csv, delimiter=';')
        
        for car in data_text:
            if not car or not car[0]:
                continue     
            lst_car.append({name_data[0]: car[0], name_data[1]: car[1], 
                            name_data[2]: car[2], name_data[3]: car[3], 
                            name_data[4]: car[4], name_data[5]: car[5], 
                            name_data[6]: car[6],})

        lst_object = list()
        # for i in lst_car:
        #     print(i)       
        for car in lst_car:
        
            if car['car_type'] == 'car':
                del car['car_type']
                obj_car = Car(**car)
                lst_object.append(obj_car)
            elif car['car_type'] == 'truck':
                del car['car_type']
                obj_car = Truck(**car)
                lst_object.append(obj_car)
            elif car['car_type'] == 'spec_machine':
                del car['car_type']
                obj_car = SpecMachine(**car)
                lst_object.append(obj_car)
        
        
        return lst_object

# new_car = Car('car', 'Nissan xTtrail', 'f1.jpeg', '2.5','4')
# #print(new_car.carrying)

d = {'brand': 'f3.jpeg', 'photo_file_name': None, 'carring': '2.5', 'passenger_seats_count': '4'}
car = Car(**d)
# def main():
#     # lst_obj = get_car_list('cars.csv')
#     # print(lst_obj)


#     cars = get_car_list('cars.csv')
#     len(cars)

#     for car in cars:
#         print(car)
#         print(car.__dict__)
# main()   
#     print(cars[1].get_body_volume())
#     print(cars[0].passenger_seats_count)
# #     # new_truck = Truck('Man', 'f2.png', '20', '8x9x7')
#     # new_car = Car('Nissan xTtrail', 'f1.jpeg', '2.5','4')
#     # print(new_car.passenger_seats_count)
# #     # print(new_truck.get_body_volume())
# #     # print(new_truck.__dict__)

# #     # print(new_car.__dict__)
# #     # print(new_truck.__dict__)

# main()


  