import time
import datetime
import json
import requests


headers = {'key': "85e94778-c56e-484c-ae4b-3dd3b513663a"}

bots = ["cryptobot"] #do these at tuples with botname and APIkey
lines = ["what is the price of ETH",
    "what is the price of BTC"]

TIMEOUT = 60 #(s)
URL = "https://platform.hut34.io/botquery?platform=gen&key=43fa344b10e440a381200acfe22e3662"
params = {"platform" : "gen",
    "key" : "43fa344b10e440a381200acfe22e3662"} #can feed this into request as params, it will form up after ?

# For the stream endpoint
STREAM = "https://old.hut34.io/stream"
auth = {"Authorization" : "b4c41e43-b85e-4397-b047-c972c0d7a04a"}

def lambda_handler(event, context):

    # Inst some objects
    price_list = []
    n = 0

    while True:
        # Run until monday 21st may
        if datetime.datetime.now().day > 15:
            break
        print ("[INFO] Scheduler has been running for {} cycles".format(n))
        # Shuffle through multiple bots if required
        for bot in bots:
            inner_list = []

            # Iterate over all requests to each bot
            for line in lines:
                # Build and make request
                payload = json.dumps({"message": "@" + bot + " " + line}) #convert dict to str
                response = requests.post(URL, data = payload) # do post
                # Process request
                # Send to hut34 Firebase
                params = {"botid":"cryptobot"}
                # make my own payload with
                payload = response.json()
                print(payload)
                # payload["timestamp"] = round(time.time())
                # payload["price"] = str(response.json()["message"].split("$")[1])
                # payload["ticker"] = str(line.split("of")[1])
                # payload["source"] = "cryptobot"
                r = requests.post(STREAM, 
                    headers = auth, 
                    params = params, 
                    data = payload)
        time.sleep(60) #wait for 1 min

# Mains
lambda_handler("request","message")