import weather, os
from flask import Flask, render_template, request
import yelp_api

app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get('city')
	

	businesses = None
#	forecast = None
	if address: 
		forecast = weather.get_weather(address)
		businesses =  yelp_api.get_restaurants(address, "food")
#	return render_template('index.html', forecast=forecast)
	return render_template('index.html', businesses=businesses)

@app.route('/about')
def about():
	return render_template('about.html')	


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


