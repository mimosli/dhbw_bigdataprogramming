# if ModuleNotFoundError: No module named 'confluent_kafka' -> install it in one of your notebooks with: !pip install confluent-kafka
# if ModuleNotFoundError: No module named 'sensemapi' -> install it in one of your notebooks with: !pip install sensemapi

# before you start create topics: sensor_raw, sensor_filtered:
# 1. use vagrant ssh to connect to your vm
# 2. connect to a kafka broker: docker exec -ti kafka-1 bash
# 3. create topic 'sensor_raw': kafka-topics --create --if-not-exists --zookeeper zookeeper-1:2181 --topic sensor_raw --partitions 6 --replication-factor 2
# 4. create topic 'sensor_filtered': kafka-topics --create --if-not-exists --zookeeper zookeeper-1:2181 --topic sensor_filtered --partitions 6 --replication-factor 2

from confluent_kafka import Producer, Consumer
import pandas as pd
import time
import json
import sensemapi

import matplotlib.pyplot as plt
from IPython import display
import datetime

Sensebox = "5d76badc953683001aa283ef"
kafka_brokers = 'kafka-1:19092,kafka-2:19093'
p = Producer({'bootstrap.servers': kafka_brokers})
c = Consumer({'bootstrap.servers': kafka_brokers, 'group.id': 'read_group1', 'auto.offset.reset': 'earliest'})
raw_topic = 'sensor_raw'
filtered_topic = 'sensor_filtered'


def delivery_report(err, msg):    
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    #else:
        #print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
        
        
def poll_and_push_data():
    print("starting round")
    messages = []
    box = sensemapi.client.SenseMapClient().get_box(id = Sensebox)
    measurements = box.sensors[1].get_measurements()
    df = measurements.series.to_frame().reset_index()
    df.columns = ['timestamp', 'pm10']
    pd.to_datetime(df.timestamp)
    df.sort_values(by="timestamp")

    # put the measurements into the messages
    for i in df.index:
        messages.append(df.loc[i].to_json())

    # put the messages into the topic
    for data in messages:
        # Trigger any available delivery report callbacks from previous produce() calls
        p.poll(0)
        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above, or flush() below, when the message has
        # been successfully delivered or failed permanently.
        p.produce(raw_topic, data.encode('utf-8'), callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    p.flush()
    messages = []
    print("finished round")

    
def read_and_display(msg, display):   
    data = json.loads(msg.value().decode('utf-8'))
    if data['pm10'] >= 10.0 :
        circle_color = 'r'
    else:
        circle_color = 'g'
    display.clear_output(wait=True)
    #out.clear_output()
    circle1=plt.Circle((0.5,0.5),.2,color=circle_color)
    plt.gcf().gca().add_artist(circle1)
    plt.axis('equal')
    txt = "value : " + str(data['pm10']) + "  last updated : " + datetime.datetime.fromtimestamp(data['timestamp'] / 1e3).strftime("%d/%m/%Y, %H:%M:%S")
    plt.text(.5, .05, txt, ha='center')
    #display.display()
    display.display(plt.show())
    time.sleep(3.0)
