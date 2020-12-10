import psutil
import time
from datetime import datetime
import os
import sys
import csv

log_file_path = "data/log/log.csv"

def get_info():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    return plugged, percent

def notify():
    # notification bar
    command = "osascript -e 'display notification \"Battery is now full charged. Unplugg the charger\" with title \"Battery Manager\"'"
    os.system(command)
    # sound notify
    command = "afplay data/sound/sound.mp3"
    os.system(command)


def logger(msg,percent,plugged,notify): 
    datetime_info = datetime.now()
    script_name = sys.argv[0]
    log_data = [datetime_info,script_name,percent, plugged,notify]
    with open(log_file_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow(log_data)
    print('[{}] : runing {} : {} : {}%'.format(str(datetime.now()), sys.argv[0],msg,percent))

def main():
    while True:
        time.sleep(10)
        plugged, percent = get_info() 
        if percent == 100 and plugged:
            notify()
            logger('sent notify',percent,plugged,True)
        else:
            logger('found no problem',percent,plugged,False)

if __name__ == '__main__':
    main()
