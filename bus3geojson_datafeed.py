import csv, json
from geojson import Feature, FeatureCollection, Point
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import time, os
import mapbox

while True:
    features = []
    with open('bus3_datafeed.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for datetime, name, longitude, latitude in reader:
            longitude, latitude = map(float, (longitude, latitude))
            features.append(
                Feature(
                    geometry = Point((longitude, latitude)),
                    properties = {
                        'name': name
                    }
                )
            )

    collection = FeatureCollection(features)
    with open("bus3.geojson", "w") as f:
        f.write('%s' % collection)

   
    time.sleep(1)
