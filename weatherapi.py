from flask import Flask, jsonify, request
import requests
 
app = Flask(__name__) 

API_KEY = 'enter the api key' #genrate an api key in open weather map and place here  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():               
    try: 
        location = request.args.get('location') 
  
        if not location:
            return jsonify({'error': 'Location not provided'}), 400

        params = {'q': location, 'appid': API_KEY}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'location': data['name'],
                'weather': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity']
            }
            return jsonify(weather_info)
        else:
            return jsonify({'error': data['message']}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
