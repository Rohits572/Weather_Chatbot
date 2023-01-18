import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    
    res = makeResponse(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-type'] = 'application/json'
    return r



def makeResponse(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    date = parameters.get("date")
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=687ec85e3966c698fa03aa71822b3fc8')
    json_object = r.json()
    print('----------------------------')
    print(json_object)
    # weather = json_object['list']
    # for i in range(0, len(weather)):
    #     if date in weather[i]['dt_txt']:            
    #         break
    # condition = weather[i]['weather'][0]['description']
    # for i in range(0,len(weather)):
    #     if date in weather[i]['dt_txt']:
    #         break   
    # temperature= weather[i]['main']['temp']
    # temperature=temperature+17
    # for i in range(0,len(weather)):
    #     if date in weather[i]['dt_txt']:
    #         break   
    # hum= weather[i]['main']['humidity']       
    speech = "The forecast for "+city 
    return {
            "fulfillmentText": speech
            }
    
if __name__ == '__main__':
    app.run()
    # port = int(os.getenv('PORT', 5000))
    # print("Starting app on port %d" % port)
    # app.run(debug=False, port=port, host='0.0.0.0')