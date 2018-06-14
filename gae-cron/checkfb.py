
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,
    {"databaseURL" : "https://hut34sandbox.firebaseio.com"})

# Dont make these objects, just uses memory, do it on the fly
network = db.reference("network")
bots = db.reference("bots")
botlist = []

def get():
    # count bots and update they stats
# change this to a list comp
    for e in bots.get():
        botname = bots.child(e+"/BotName").get()
        if botname not in botlist:
            botlist.append(botname)
    # set       
    network.child("numberOfBots").set(len(botlist))
    print(len(botlist))

    # count the TX
    number_of_requests = len(db.reference("request").get())
    # set
    network.child("numberOfRequests").set(number_of_requests)
    print(number_of_requests)

get()
