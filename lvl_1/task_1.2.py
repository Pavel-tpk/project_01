import random
from datetime import timedelta

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

random_songs = random.choices(my_favorite_songs, k=3)
print('Случайные песни:', random_songs)

# Если в условии длительность песен задана десятичной дробью в минутах, то выполняем этот код:

total_time = 0
for i in range(len(random_songs)):
    total_time += random_songs[i][1]

print('Если в условии длительность песен задана десятичной дробью в минутах, то:')
print(f'Три песни звучат {round(total_time, 2)} минут')


# Если в условии длительность песен задана в формате "минуты.секунды", то выполняем этот код:
total_time = timedelta(minutes=0, seconds=0)
for i in range(len(random_songs)):
    duration = str(random_songs[i][1])
    minutes = int(duration.split('.')[0])
    seconds_str = duration.split('.')[1]
    if len(seconds_str) < 2:
        seconds_str = seconds_str + '0'
    seconds = int(seconds_str)
    
    total_time += timedelta(minutes=minutes, seconds=seconds)
    
total_minutes = total_time.seconds // 60
total_seconds = total_time.seconds - total_minutes * 60
total_minutes_str = str(total_minutes)
total_seconds_str = str(total_seconds)

if len(total_seconds_str) < 2:
    total_seconds_str = '0' + total_seconds_str

print('Если в условии длительность песен задана в формате "минуты.секунды", то:')
print(f'Три песни звучат {total_minutes_str}.{total_seconds_str} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

songs_list = list(my_favorite_songs_dict.items())

total_time = 0
for i in range(0, 3):
    name, duration = songs_list[random.randint(0, len(songs_list)-1)]
    print(name, duration)
    total_time += duration

print(f'Три песни звучат {round(total_time, 2)} минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 