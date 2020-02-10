import csv, json
from geojson import Feature, FeatureCollection, Point
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener
import time, os
import mapbox

while True:
    features = []
    with open('bus1_sampledatafeed.csv', newline='') as csvfile:
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
    with open("bus1.geojson", "w") as f:
        f.write('%s' % collection)

    pnconfig = PNConfiguration()

    pnconfig.publish_key = 'pub-c-7de404e5-df52-43f0-88b8-18d5805462ca'
    pnconfig.subscribe_key = 'sub-c-76765e0e-4787-11ea-a4fb-16aec0d9ba73'

    pubnub = PubNub(pnconfig)

    my_listener = SubscribeListener()
    pubnub.add_listener(my_listener)

    pubnub.subscribe().channels('Channel1').execute()
    my_listener.wait_for_connect()
    print('connected')

    pubnub.publish().channel('Channel1').message(collection).sync()
    result = my_listener.wait_for_message_on('Channel1')
    print(result.message)
    time.sleep(1)
