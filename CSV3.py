import logging
import csv
import datetime
import keyboard
from ut61eplus import UT61EPLUS

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# Открываем CSV файл в режиме добавления
csv_file = open('data.csv', 'a', newline='')
csv_writer = csv.writer(csv_file)

dmm = UT61EPLUS()

log.info('name=%s', dmm.getName())
dmm.sendCommand('lamp')

while True:
    if keyboard.is_pressed(' '):  # Проверяем, была ли нажата клавиша пробела
        d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        m = dmm.takeMeasurement()
        display = m.display
        display_unit = m.display_unit
        
        # Записываем данные в CSV файл
        csv_writer.writerow([d, display, display_unit])
        
        # Сохраняем файл
        csv_file.flush()
        
    else:
        continue

# Закрываем CSV файл
csv_file.close()
