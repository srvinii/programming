from datetime import datetime
now = datetime.now()
print("Put your birth day, month, and year (separated using '/')")
insert_day = input("--> ")
day = insert_day.replace('/','')
value_day = day[0]
value_day = value_day + day[1]
month = day[2]
month = month + day[3]
year = day[4]
year = year + day[5]
year = year + day[6]
year = year + day[7]
years = now.year
years = int(years) - int(year)
print('Your bith day -> ','\033[0;32m', value_day,'\033[0m')
print('Your birth month -> ','\033[0;32m',month,'\033[0m')
print('Your birth year -> ','\033[0;32m',year,'\033[0m')
print('You have ','\033[0;31m',years,'\033[0m','years :)')