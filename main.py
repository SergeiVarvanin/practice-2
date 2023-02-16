





import csv

print(f'Hello.I was created for the individual selection of games from Steam according to the users preferences.'
f'And now I propose to take a small survey: ')
#открываем ксв файл
with open('steam.csv', newline='',encoding='utf-8-sig') as csvfile:
      # отображаем информацию о столбцах в словарь
      reader = csv.DictReader(csvfile)
      # достаем заголовки
      headers = reader.fieldnames
      # создаем пустой словарь, для внесения информации
      filters = dict()
      # создаем список, для внесения информации
      tm_reader = list()
      for i in headers:
            """цикл для вля порядкового внесения значений для сортировки"""
            if not i in []:
                  print(f"What kind of {i}"
                  f" you prefer: ", end='')
                  filters[i] = input()
                  tm_reader.append(filters[i])
      for row in reader:
            """цикл котрый сравнивает введеную информацию с исходной. 
            В случае совпадения выводит информацию в resalt
            В случае несоответствия заставляет вводить нужную информацию
            Можно было для каждого запроса вводить свои параметры, но в задании это не уточнялось"""
            for data in filters.keys():
                  # lower() преобразует все символы верхнего регистра в строке в символы нижнего регистра
                  if (filters[data].lower() in row[data].lower()):
                        with open('result.csv', mode='a', encoding='utf-8-sig', newline='') as of:
                              writer = csv.DictWriter(of, fieldnames=filters)
                              writer.writerow(row)
                        print('You can look at this:')
                  else:
                        print(f'The following games are suitable. We continue')
                        break
                  print(f' Your wait has come to an end.  Wrirting to "result.csv" => game: "{row[filters[0]]}"')


print('According to your preferences, the following games are suitable. Games has been written to "result.csv"')
