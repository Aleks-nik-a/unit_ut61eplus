import logging
import csv
import datetime
import keyboard
from ut61eplus import UT61EPLUS

CP2110_VID_PID = [[0x1A86, 0xE429], [0x10C4, 0xEA80]]

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

for vid, pid in CP2110_VID_PID:
    try:
        dmm = UT61EPLUS(vid, pid)
    except:
        log.error('Cant open device' + str(f'VID={vid:X} PID= {pid:X}'))

# dmm = UT61EPLUS(VID, PID)

log.info('name=%s', dmm.getName())
dmm.sendCommand('lamp')

measurement_counter = 1

with open('measurements.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Дата', 'Порядковый номер', 'display', 'display_unit', 'Введенное значение'])

while True:
    value = input("Введите значение: ")
    if value == "":
        break

    m = dmm.takeMeasurement()
    log.info('measurement=%s', m)

    # Запись данных в CSV файл
    with open('measurements.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), measurement_counter, m.display, m.display_unit, value])

    measurement_counter += 1


