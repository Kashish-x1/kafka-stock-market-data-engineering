from kafka import KafkaConsumer
from time import sleep
from json import loads
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    "demo_testing2",
    bootstrap_servers=["98.81.107.164:9092"],
    value_deserializer=lambda x: loads(x.decode("utf-8"))
)

s3 = S3FileSystem()

for count, i in enumerate(consumer):
    with s3.open(
        "s3://kashish-kafka-stock-market-2026/stock_market_{}.json".format(count),
        "w"
    ) as file:
        json.dump(i.value, file)