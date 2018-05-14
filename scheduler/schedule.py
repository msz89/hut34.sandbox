import time
import datetime
from json import dumps as json_dumps
from requests import post as requests_post


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
        if datetime.datetime.now().day > 20:
            break
        print ("[INFO] Scheduler has been running for {} cycles".format(n))
        # Shuffle through multiple bots if required
        for bot in bots:
            inner_list = []

            # Iterate over all requests to each bot
            for line in lines:
                # Build and make request
                payload = json_dumps({"message": "@" + bot + " " + line}) #convert dict to str
                response = requests_post(URL, data = payload) # do post
                
                # Process request
                print (response.json()["message"])
                #a = dict((k, response.json()[k]) for k in ["timestamp","message"]) # just extact timestamp and message
                #inner_list.append(a) #collect the responses in a list

                # Send to hut34 Firebase
                #params = json_dumps({"botid":"cryptobot"})
                payload = response.json()
                payload["botid"] = "cryptobot"
                payload = json_dumps(payload)
                r = requests_post(STREAM, headers = auth, params = payload) #, data = payload)
                print(r.json())#["firebase_key"]) #print firebase key to confirm

        #price_list = price_list + inner_list #join the lists together
        time.sleep(60) #wait for 1 min

# output the info
    # with open("prices.txt","w+") as f:
        # f.write(str(price_list))

# Mains
lambda_handler("request","message")