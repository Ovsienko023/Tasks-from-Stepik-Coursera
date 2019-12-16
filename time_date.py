from datetime import timedelta, date

year_in, month_in, day_in = (int(i) for i in input().split(' '))
data_now = date(year_in, month_in, day_in)

days_letter = timedelta(int(input()))
new_data = data_now + days_letter 

print(new_data.year, new_data.month, new_data.day)


# Вывод можно было сделать используя: inp = datetime.datetime.strptime(input(), "%Y %m %d")