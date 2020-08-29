import pandas as pd
import numpy
import copy
import csv
import os


name_file_exel = r'Приложение к ПИВ Н135_БЦВМ.xls'  # need to add to config
name_file_csv = r'Приложение к ПИВ Н135_БЦВМ.csv'


def exel_to_csv(name_file):
    """"Функция читает файл формата 'exel', который необходимо парсить и
    создает на его основе файл формата 'csv'.
    """
    read_file = pd.read_excel(name_file_exel, sheet_name='Лист1')
    read_file.to_csv(name_file_csv, index=None, header=True)


class DivisionTable:
    """Класс для грубого парсинга и обработки таблиц."""
    def __init__(self):
        self.lst_of_csv = []
        self.all_tables = []

    def create_all_tables(self):
        """Метод читает ранее созданный файл формата 'csv' и
        наполняет на его основе лист - 'self.lst_of_csv'
        для его дальнейшей обработки.
        """
        with open(name_file_csv, 'r', encoding='utf-8') as csv_obj:
            reader = csv.reader(csv_obj)
            for one_str in reader:
                self.lst_of_csv.append(one_str)

    def dirty_divis_table(self):
        """Метод осуществляет 'грязное' разделение таблиц."""
        one_table = []
        for one_str in self.lst_of_csv:
            one_table.append(one_str)
            firsr_char = one_str[0]

            if firsr_char == 'Источник':
                if one_table:
                    one_table.pop()
                    new_one_table = copy.deepcopy(one_table)
                    self.all_tables.append(new_one_table)
                    one_table.clear()
                    one_table.append(one_str)
        self.all_tables.append(one_table)

    def remove_csv(self):
        """Метод удаляет, ранее созданный, файл формата 'csv' и
        очищает список наполненый данными файла 'csv',
        так как они в дальнейшем не понадобятся.
        """
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            name_file_csv)
        os.remove(path)
        self.lst_of_csv.clear()

    def remove_empt_first_tabl(self):
        """Метод проверяет является ли первая таблица ожидаемой таблицой,
        если же это не валидные данные(не то что нам необходимо парсить),
        то они удаляются.
        """
        lst_del_index = [self.all_tables.index(one_table) for one_table in self.all_tables 
                                                            if one_table[0][0] != 'Источник']
        for val_index in lst_del_index:
            del self.all_tables[val_index]

    def remove_empt_str_tabl(self):
        """Метод осуществляет проверку наличия пустых строк в
        каждой имеющейся таблице, если такие имеются, они удаляются.
        """
        for one_table in self.all_tables:
            for one_str in reversed(one_table):
                first_char, sekond_char, third_char = one_str[:3]

                if first_char == '' and sekond_char == '' and third_char == '':
                    del one_table[one_table.index(one_str)]
    
    def remove_empt_last_tabl(self):
        """Метод удаляет лишние строки из последней таблицы."""
        flag_del = False
        lst_for_del = []
        last_table = self.all_tables[-1]

        for one_str in last_table:
            if 'Таблица  ГО1' in one_str:
                flag_del = True
            if flag_del:
                lst_for_del.append(last_table.index(one_str))

        for i in reversed(lst_for_del):
            del last_table[i]

    def give_tables(self) -> list:
        """Метод возвращает список таблиц."""
        return self.all_tables


class ParsTable:
    def __init__(self, tables: list):
        self.all_tables = tables
        self.a = self.pars_words_all_tabl(self.all_tables)

    def pars_words_all_tabl(self, all_tabl):
        """ """
        word = 0
        for tabl in range(len(all_tabl)):
            for words in range(5, len(all_tabl[tabl])):
                if all_tabl[tabl][words][0].isdigit():
                    word = all_tabl[tabl][words][0]
                else:
                    all_tabl[tabl][words][0] = word
        self.all_tables = copy.deepcopy(all_tabl)

    def show_table(self):
        for i in self.all_tables:
            for j in i:
                print(j)
            print()


def main():
    exel_to_csv(name_file_exel)
    b = DivisionTable()
    b.create_all_tables()
    b.dirty_divis_table()
    b.remove_csv()
    b.remove_empt_first_tabl()
    b.remove_empt_str_tabl()
    b.remove_empt_last_tabl()
    c = ParsTable(b.give_tables())
    c.show_table()


if __name__ == '__main__':
    main()
