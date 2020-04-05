import os.path
import tempfile
import random


class File:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.counter = 0
        if not os.path.exists(path_to_file):
            with open(path_to_file, 'w') as w:
                w.write('')

 
    def read(self):
        with open(self.path_to_file, 'r') as f:
            text = f.read()
        return text


    def write(self, text):
        with open(self.path_to_file, 'w') as f:
            f.write(text)
        return len(text)

 
    def __add__(self, obj):
        storage_path = os.path.join(tempfile.gettempdir(),  f'{str(random.random())[2:]}.data')
        sum_file = self.read() + obj.read()

        if not os.path.exists(storage_path):
            with open(storage_path, 'w') as w:
                w.write('') 
        self.path_to_file = storage_path
        
        if os.path.exists(self.path_to_file):
            with open(self.path_to_file, 'w') as writer:
                writer.write(sum_file)
                
        new_obj = File(self.path_to_file)
        return new_obj


    def __iter__(self):
        return self


    def __next__(self):
        with open(self.path_to_file) as f:
            line = f.readlines()
            if self.counter >= len(line):
                raise StopIteration
         
            result = line[self.counter]
            self.counter += 1
            return result


    def __str__(self):
        return os.path.abspath(self.path_to_file)  
        
        

def main_test():
    path_to_file = "some_filename"
    print(os.path.exists(path_to_file))    
    file_obj = File(path_to_file)
    print(os.path.exists(path_to_file))
    print(file_obj.read())
    print(file_obj.write('some text'))
    print(file_obj.read())
    print(file_obj.write('other text'))
    print(file_obj.read())
    file_ob_1 = File(path_to_file + "_1")
    print(file_ob_1.write('line 1\n'))
    file_ob_2 = File(path_to_file + "_2")
    print(file_ob_2.write('line 2\n'))
    new_file_obj = file_ob_1 + file_ob_2
    print(isinstance(new_file_obj, File))
    print(new_file_obj)
    print(new_file_obj.read())  
    for line in new_file_obj:
        print(ascii(line))

# main_test()
