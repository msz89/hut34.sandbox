device = cryptobot ##this could be any bot
text_area = ["what is the price of ETH", "what is the price of BTC"]

if device.save_stream == True
every minute do this:      
    for each line in text_area:
        send a request (line) to device
        send response to old.hut34.io/request
        send response + {botid = firebase_key_of_device} to old.hut34.io/stream ## Note, bot ID must be sent as a POST request variable

## The purpose of this is to allow a user to stream their data to the hut
## There should be a switch on the GUI to allow users to "save stream"
## As a first pass we can achieve this by having an automated process to call their device
## The process should default to calling the device every 60s (1 min)

## The process should send a custom request defined in the text_area
## If this is a single string it should send 1 request.
## If this is an array* it should send each request in the array every 60s.
## *(suggest comma or newline as delimiter), 
## The process should send an empty request if the text_area is empty

## This process should be set up so we can save a stream on any device
## Both /request and /stream endpoints will send data and a firebase_key if successful