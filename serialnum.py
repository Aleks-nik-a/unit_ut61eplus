import hid

CP2110_VID = 0x10c4
CP2110_PID = 0xEA80

def get_serial_number():
    found_devices = hid.enumerate(CP2110_VID, CP2110_PID)
    if found_devices:
        device_info = found_devices[0]
        device = hid.device()
        device.open_path(device_info['path'])
        device.write([0x00, 0x01])  # Send the command to get the serial number
        response = device.read(64)  # Read the response data
        serial_number = response[2:].tostring()  # Extract and decode the serial number
        device.close()
        return serial_number.decode('utf-8')
    else:
        return None

serial_number = get_serial_number()
if serial_number:
    print('Serial number:', serial_number)
else:
    print('Device not found')
