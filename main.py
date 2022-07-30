# передадим в программу данные
print('Напишите про ветер:')
beaufort = int(input())
print('Напишите про дождь:')
is_raining = str(input())
print('Напишите про температуру:')
temperature = int(input())

if (is_raining == "нет" or is_raining == "Нет" and beaufort <= 4) and temperature > 16:
    print('Идём гулять, на улице хорошо')
else:
    print('Сидим дома, читаем книги')

input()