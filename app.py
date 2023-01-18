from flask import Flask, request,jsonify, make_response

import json
import requests


app= Flask(__name__)





@app.route('/webhook', methods=["POST"])
def webhook():
    req= request.get_json(silent=True,force=True)
    print(json.dumps(req, indent=4))
    res = formResponse(req)
    res = json.dumps(res, indent=4)
   
    a = make_response(res)
    a.headers['Content-Type'] = 'application/json'
    return a

def formResponse(req):
    result=req.get('queryResult')
    paramters=result.get('parameters')
    city=paramters.get('geo-city')
    r= requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=687ec85e3966c698fa03aa71822b3fc8')
    convert= r.json()
    print("-----------------------------------------------")
    print(convert)
    cloud=""
    weather=convert['weather']
    for x in weather:
        cloud+=x['description']
    temp_min= convert["main"]['temp_min']
    temp_max= convert['main']['temp_max']
    humidity= convert['main']['humidity']
    visibility= convert['visibility']
    sunrise= convert['sys']['sunrise']
    
    speech=("Today the weather in " + city + " is " + cloud +" with minimum temperature of " + str(temp_min) + " with maximum temperature of " 
           + str(temp_max) + " and humidity is " + str(humidity) + " with visibility of " + str(visibility) + ".")
            

    
    return {
            "fulfillmentText": speech
            }



if __name__ == "__main__":
    app.run()