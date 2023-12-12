import logging
import csv
from datetime import datetime, timedelta
from ut61eplus import UT61EPLUS

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

csv_filename = 'data.csv'  # Имя файла CSV

dmm = UT61EPLUS()

log.info('name=%s', dmm.getName())
dmm.sendCommand('lamp')

# Создаем объект CSV файла
csv_file = open(csv_filename, 'w', newline='')
csv_writer = csv.writer(csv_file)

# Записываем заголовки столбцов
csv_writer.writerow(['Дата', 'Значение', 'Единицы'])

# Задаем интервал в 1 секунду
interval = timedelta(seconds=1)
next_record_time = datetime.now() + interval

while True:
    if datetime.now() >= next_record_time:
        m = dmm.takeMeasurement()
        
        # Записываем данные в CSV файл
        csv_writer.writerow([datetime.now(), m.display, m.display_unit])
        csv_file.flush()  # Сбрасываем буфер CSV файла
        
        next_record_time = datetime.now() + interval
        
    # Дополнительный код
    # ...

csv_file.close()
