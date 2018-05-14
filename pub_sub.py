import os
import json
import cv2
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from time import sleep
from datetime import date, datetime

 
root = "/home/matt/"
# AWS IoT certificate based connection
myMQTTClient = AWSIoTMQTTClient("dackrambo")
myMQTTClient.configureEndpoint("a1xrgfi7tw2r2a.iot.ap-southeast-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials(root + ".aws/rootCA.crt",
    root + ".aws/2d4288b294-private.pem.key",
    root + ".aws/2d4288b294-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
 
#connect and publish
myMQTTClient.connect()
myMQTTClient.publish("skullcave/info", "connected", 0)

# Set up webcam
webcam = cv2.VideoCapture(0)


# Define a function to handle the callback from the subsciption
def thingdoer(client, userdata, message):
    # Decode message from bytes > str > Json, then get 'message'
    msg = json.loads(message.payload.decode("utf-8"))
    print (msg["message"])
    #publish_temp()
    publish_temp(custom = True, payload = stream_video())
    return True

def publish_temp(custom = False ,payload = 0):
    now = datetime.utcnow()
    now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ') #e.g. 2016-04-18T06:12:25.877Z
    result = (10,20)
    if custom == False:
        payload = '{ "timestamp": "' + now_str + '","temperature": ' + str(result[0]) + ',"humidity": '+ str(result[1]) + ' }'
    myMQTTClient.publish("thing01/img", payload, 0)

def stream_video():
    grabbed, frame = webcam.read()
    if grabbed:
        print(frame.shape)
        frame = cv2.resize(frame, (48,64))
        cv2.imshow("Preview", frame)
        cv2.waitKey(200)
        cv2.destroyAllWindows()
        img = cv2.imencode('.jpg', frame)[1].tostring()
        return str(img)
        # & 0xFF
        # # If the `q` key is pressed, break from the loop
        # if key == ord('q'):
        #     cv2.destroyAllWindows()

myMQTTClient.subscribe("test01", 0, thingdoer)

while True:
    sleep(5)

#myMQTTClient.onMessage = thingdoer

#loop and publish sensor reading
# while 1:
#     now = datetime.utcnow()
#     now_str = now.strftime('%Y-%m-%dT%H:%M:%SZ') #e.g. 2016-04-18T06:12:25.877Z
#     result = (1,2)
#     if True:
#         payload = '{ "timestamp": "' + now_str + '","temperature": ' + str(result[0]) + ',"humidity": '+ str(result[1]) + ' }'
#         print (payload)
#         myMQTTClient.publish("thing01/data", payload, 0)
#         sleep(4)
#     else:
#         print (".")
#         sleep(1)