import logging
import csv
import time
from ut61eplus import UT61EPLUS

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

dmm = UT61EPLUS()

# Open a CSV file for writing
csv_file_path = 'data_02.csv'
csv_file = open(csv_file_path, 'w', newline='')
csv_writer = csv.writer(csv_file)

# Write header to the CSV file
csv_writer.writerow(['Time', 'Value', 'Unit'])

try:
    while True:
        # Take measurement
        measurement = dmm.takeMeasurement()

        # Get current time
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        # Extract relevant information from the measurement
        value = measurement.value
        unit = measurement.unit

        # Log the measurement
        log.info('Measurement at %s: %s %s', current_time, value, unit)

        # Write the measurement to the CSV file
        csv_writer.writerow([current_time, value, unit])

        # Wait for 0.5 seconds before taking the next measurement
        time.sleep(0.5)

except KeyboardInterrupt:
    # Close the CSV file when the script is interrupted (e.g., by pressing Ctrl+C)
    csv_file.close()
    log.info('Script interrupted. CSV file closed.') 
