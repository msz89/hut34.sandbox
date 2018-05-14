import random
import time

from allthingstalk import Client, Device, IntegerAsset

class RandomDevice(Device):
    random_number = IntegerAsset()

client = Client('maker:4HzxVU3lNp6JG0lqFzug94RHh3I4y5cEzyCMQJq2')
device = RandomDevice(client=client, id='IxPfSGaqK40GPwlNNoB6T6Zt')

while True:
    device.random_number = random.randint(20, 25)
    time.sleep(1)
