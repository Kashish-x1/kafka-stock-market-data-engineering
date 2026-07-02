from kafka import KafkaProducer
import pandas as pd
from time import sleep
from json import dumps
import json
producer = KafkaProducer(
    bootstrap_servers=['98.81.107.164:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
producer.send(
    'demo_testing2',
    value={
        'name': 'Kashish',
        'project': 'Stock Market Kafka'
    }
)
df = pd.read_csv("data/indexProcessed.csv")
df.head()
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send("demo_testing2", value=dict_stock)
    print(dict_stock)
    sleep(1)
producer.flush()
