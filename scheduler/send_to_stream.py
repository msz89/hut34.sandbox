import requests
import json

STREAM = "https://old.hut34.io/stream"
auth = {"Authorization" : "b4c41e43-b85e-4397-b047-c972c0d7a04a"}
params = json.dumps({"botid":"cryptobot"})
payload = json.dumps({"id": "cb4f3041-5781-4eb8-b018-4bbeea230676", 
	"timestamp": "11-05-2018 02:05:48", 
	"message": "Hut34 Response (cryptobot):  Price of Ethereum is USD $730.265", 
	"response": 
		{"source": "cryptobot", 
		"resolvedQuery": "@cryptobot what is the price of ETH", 
		"isComplete": True}, "input": 
			{"source": "NigellAI", 
			"Key": "43fa344b10e440a381200acfe22e3662"}, 
			"status": {"code": 100, "type": "success"}, 
			"errorData": {"code": 0, "description": ""}, "error": ""}
	)

r = requests.post(STREAM, headers = auth, params = params, data = payload)
print(r.text)

