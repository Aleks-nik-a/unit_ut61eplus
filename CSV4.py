import logging
import csv
import datetime
from ut61eplus import UT61EPLUS

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

dmm = UT61EPLUS()

log.info('name=%s', dmm.getName())
dmm.sendCommand('lamp')

# Открытие CSV файла для записи
csv_file = open('data.csv', mode='w', newline='')
fieldnames = ['Дата', 'Порядковый номер', 'Display', 'Display unit', 'Ввод с клавиатуры']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

count = 1

while True:
    m = dmm.takeMeasurement()
    log.info('measurement=%s', m)

    # Получение значения ввода с клавиатуры
    user_input = input("Введите значение: ")

    # Получение текущей даты
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Запись данных в CSV файл
    writer.writerow({
        'Дата': current_date,
        'Порядковый номер': count,
        'Display': m.display,
        'Display unit': m.display_unit,
        'Ввод с клавиатуры': user_input
    })

    # Делаем следующее измерение

    count += 1

    # Проверка нажатия на пробел
    if input("Нажмите Пробел для продолжения или любую другую клавишу для выхода: ") != " ":
        break

# Закрытие CSV файла
csv_file.close()
