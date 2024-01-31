import subprocess, re
from datetime import datetime
import time
import csv
import public_ip as ip

connected_wifi = subprocess.check_output(
    ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'])
bssid = re.search(r'BSSID: (\S+)', connected_wifi.decode()).group(1)
pub_ip = ip.get()

while True:
    try:
        connected_wifi = subprocess.check_output(
            ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-I'])
        bssid = re.search(r'BSSID: (\S+)', connected_wifi.decode()).group(1)
        pub_ip = ip.get()
        now = datetime.now()
        connected_wifi = subprocess.check_output(['ping', '-c', '1', 'cse.unsw.edu.au'])
        rtt = re.search(r'time=(.+) ms', connected_wifi.decode()).group(1)
        print("%.0f" % now.timestamp(), bssid, pub_ip, rtt)
        with open('ping2.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["%.0f" % now.timestamp(), bssid, pub_ip, rtt])
        time.sleep(10)
    except:
        print("%.0f" % now.timestamp(), bssid, pub_ip, 4000)
        with open('ping2.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["%.0f" % now.timestamp(), bssid, pub_ip, 4000])
        time.sleep(10)