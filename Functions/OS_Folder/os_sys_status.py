import subprocess
import psutil

# Main function is get_wifi_info() -> no input required #
# Returns a list of statuses, each status is a list of strings # X 4

# Main function is gget_battery_info() -> no input required #
# Return a string of battery status #

def get_wifi_info():
    wifi_result = []
    proc = subprocess.check_output('netsh wlan show interfaces')
    proc = proc.decode('utf-8')
    proc = proc.split('\n')
    for line in proc:
        if 'State' in line:
            result =  line.split(':')[1].strip()
            result = result[0].upper() + result[1:]
            result = "Wifi Status: {}".format(result)
            wifi_result.append(result)
        if 'SSID' in line and 'B' not in line:
            result = "Wifi Name: {}".format(line.split(':')[1].strip())
            wifi_result.append(result)
        if 'Signal' in line:
            result = "Wifi Signal: {}".format(line.split(':')[1].strip())
            wifi_result.append(result)
        if 'Band' in line:
            result = "Wifi Band: {}".format(line.split(':')[1].strip())
            wifi_result.append(result)
    return wifi_result

def get_battery_info():
    # Get battery information
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Charging"
    else:
        status = "Not Charging"

    return "Battery status: {} ({}%)".format(status, percent)


# # Run systeminfo command
# result = subprocess.run('systeminfo', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# # Extract the line containing Bluetooth status and device name
# bluetooth_info = [line for line in result.stdout.split('\n') if 'Bluetooth' in line]

# print(bluetooth_info)

# # Parse the Bluetooth status and device name
# if bluetooth_info:
#     status = bluetooth_info[0].split(':')[1].strip()
#     device_name = bluetooth_info[1].split(':')[1].strip()
#     print(f"Bluetooth status: {status}\nDevice name: {device_name}")
# else:
#     print("Bluetooth is not available on this system.")
