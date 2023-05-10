# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Вариант 1
print('Первый трек:', my_favorite_songs[0:14])
print('Последний трек:', my_favorite_songs[-13:-1])
print('Второй трек:', my_favorite_songs[16:30])
print('Второй с конца трек:', my_favorite_songs[-26:-14])

# Вариант 2
songs_list = my_favorite_songs.split(', ')  # получаем список песен
print('Первый трек:', songs_list[0])
print('Последний трек:', songs_list[-1])
print('Второй трек:', songs_list[1])
print('Второй с конца трек:', songs_list[-2])
