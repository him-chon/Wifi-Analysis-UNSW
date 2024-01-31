import pandas as pd
import os
import glob
import re

output_name = '11_10_23_night.csv'
path = 'raw_data/11_10_23_night_data'

# Use glob to get all the csv files in the folder
csv_files = glob.glob(os.path.join(path, "*.csv"))

# Create main dataframe to be appended to
df = pd.DataFrame()

# loop over the list of csv files
for f in csv_files:
    # Read the csv file
    try:
        tmp = pd.read_csv(f)
    except:
        print(f'{f} failed to read')
        continue

    # Get BSSID and SSID from file name
    fname = os.path.basename(f)
    print(fname)
    bssid = re.search(r'\((.*?)\)', fname).group(1)
    ssid = re.search(r'(.*?)\(', fname).group(1)
    bssid = bssid.replace('-', ':')
    tmp['SSID'] = ssid
    tmp['BSSID'] = bssid

    # Drop unnecessary rows
    tmp = tmp.drop(tmp[tmp[' Signal(dBm)'] == ' -'].index)
    tmp = tmp.drop(tmp[tmp[' Signal(dBm)'] == ' Scanning Started'].index)
    tmp = tmp.drop(tmp[tmp[' Signal(dBm)'] == ' Scanning Paused'].index)

    # Add data from file to main dataframe
    df = df.append(tmp, ignore_index=True)
    print(f'{fname} successfully added')

df.to_csv(output_name)