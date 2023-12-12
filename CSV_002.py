import logging
import csv
import datetime
import keyboard
from ut61eplus import UT61EPLUS

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

# Получение списка всех подключенных устройств
devices = UT61EPLUS.getAvailableDevices()

log.info('Найдено устройств: %s', len(devices))

# Создание списка объектов UT61EPLUS для каждого устройства
dmm_list = []
for device in devices:
    dmm = UT61EPLUS(device)
    dmm_list.append(dmm)
    log.info('Устройство %s - name=%s', device.serial_number, dmm.getName())
    dmm.sendCommand('lamp')

measurement_counter = 1
while True:
    input("Нажмите Enter для выполнения следующего измерения...")
    
    for i, dmm in enumerate(dmm_list):
        m = dmm.takeMeasurement()
        log.info('Устройство %s - measurement=%s', devices[i].serial_number, m)

        # Запись данных в CSV файл
        with open(f'measurements_{devices[i].serial_number}.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now(), measurement_counter, m.display, m.display_unit])
    
    measurement_counter += 1 
