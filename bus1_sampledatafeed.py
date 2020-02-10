import pandas as pd
import time, os

while True:
    data = pd.read_csv('senate_sampledatafeed.csv')
    # Filter the data accordingly.
    data = data[data['name'] == 'Bus 2.']
    data.to_csv('bus1_sampledatafeed.csv', index=False, header=None, mode='w')
    print(data)
    time.sleep(1)
