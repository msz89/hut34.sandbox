'use strict';
// Import requests library. To use this you will have to npm install it into a directory, zip it up and upload it to Lambda
var request = require('request');
// This is the payload for our POST to ES. it instructs ES to return the most recent timestamped data
var json_payload = {"sort":[{"timestamp":{"order":"desc"}}],"size":1}
//Insert your URL here
var myUrl =     'https://search-cartel-sensors-4troqvfmymtu5u2q3u4wur7cca.ap-southeast-2.es.amazonaws.com/'
var myDevice =  'thing01'
// This function handles the POST to ES, parses the response 
// and formulates a response for the API to handball on to Hut34
exports.handler = function(event, context, callback) {
    let responseCode = 200;
    // fetch infofrom ES
    request.post(myUrl + myDevice + '_search',
        json_payload, function (error, response, body) {
        // Console log to understand what ES is sending back
        console.log("response: ", body);

        //Build a message from the ES response for Hut34
        var responseBody = {
            message: JSON.parse(body).hits.hits[0]._source.temperature
        };
        
        // Pack this message into the response format that API expects
        var response1 = {
            statusCode: responseCode,
            headers: {
                "x-custom-header" : "my custom header value"
            },
            body: responseBody
        };

        // Ship it
        callback(null, response1);
    });
    }