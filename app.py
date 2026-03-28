print("RUNNING APP...")
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)

        data = response.json()
        current = data["current_condition"][0]

        return {
            "city": city.upper(),
            "temp": current["temp_C"],
            "desc": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind": current["windspeedKmph"]
        }
    except:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")
        weather = get_weather(city)

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=True, host="127.0.0.1", port=5000)