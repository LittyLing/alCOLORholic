from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

apiSrc = "http://www.colr.org/json/color"

@app.route('/')
def home():
   apiData = requests.get(apiSrc + "/random").json()["colors"]
   nameData = apiData[0]["tags"][0]["name"].capitalize()
   hexData = apiData[0]["hex"]
   print nameData + ": " + hexData 
   return render_template("home.html", name = nameData, hexVal = hexData)

@app.route('/<string:hex>')
def viewColor(hex):
   apiData = requests.get(apiSrc + "/" + hex).json()["colors"]
   nameData = apiData[0]["tags"][0]["name"].capitalize()
   hexData = apiData[0]["hex"]
   print nameData + ": " + hexData 
   return render_template("color.html", name = nameData, hexVal = hexData)

@app.route('/random')
def randomColor():
   apiData = requests.get(apiSrc + "/random").json()["colors"]
   nameData = apiData[0]["tags"][0]["name"].capitalize()
   hexData = apiData[0]["hex"]
   print nameData + ": " + hexData 
   return render_template("random.html", name = nameData, hexVal = hexData)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, threaded=True)