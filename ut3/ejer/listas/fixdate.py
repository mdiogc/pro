date = '12/31/20'

splitted_date = date.split('/')
day = splitted_date[1]
month = splitted_date[0]
year = '20' + splitted_date[2]

new_date = '-'.join([day, month, year])
print(new_date)
