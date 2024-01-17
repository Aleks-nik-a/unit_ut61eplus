import logging
import csv
import datetime
import keyboard
import sys
from ut61eplus import UT61EPLUS


UNIT1_VID_PID = [0x1A86, 0xE429]
UNIT2_VID_PID = [0x10C4, 0xEA80]

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)


if len(sys.argv) >= 2:
    outFileName = sys.argv[1]
    log.info(f'Имя файла: {outFileName} ')
else:
    outFileName = 'measurement.csv'
    log.info(f'Имя файла не указано. Данные записываются в {outFileName}')


dmmVolts = UT61EPLUS(UNIT1_VID_PID[0], UNIT1_VID_PID[1] )
dmmAmpers = UT61EPLUS(UNIT2_VID_PID[0], UNIT2_VID_PID[1])

log.info('name=%s', dmmVolts.getName())
dmmVolts.sendCommand('lamp')
dmmAmpers.sendCommand('lamp')

measurement_counter = 1

with open(outFileName, mode='a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Дата', 'Порядковый номер', 'disp1', 'disp1_unit', 'disp2', 'disp2_unit',  'Введенное значение'])

    while True:
        value = input("Введите значение: ")
        measV = dmmVolts.takeMeasurement()
        measA = dmmAmpers.takeMeasurement()
        log.info('measurement Volts = {measV}, measurement Current = {measA}')

        # Запись данных в CSV файл
        writer.writerow([datetime.datetime.now(), measurement_counter, measV.display, measV.display_unit, measA.display, measA.display_unit, value])

        measurement_counter += 1


