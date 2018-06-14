import webapp2
#import urllib2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,
    {"databaseURL" : "https://hut34sandbox.firebaseio.com"})

# Dont make these objects, just uses memory, do it on the fly
network = db.reference("network")
bots = db.reference("bots")
botlist = []

#URL = "https://us-central1-nigella-ai.cloudfunctions.net/hello-world"
class HourCronPage(webapp2.RequestHandler):
    def get(self):
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
    numberofbots = len(db.reference("request").get())
    # set
    network.child("numberOfRequests").set(numberofbots)
    print(numberofbots)

    # request = urllib2.Request(URL, headers={"cronrequest" : "true"})
    # contents = urllib2.urlopen(request).read()

app = webapp2.WSGIApplication([
    ('/minute', HourCronPage),
    ], debug=True)
