from flask import Flask
from functions import weather_city

def weather_city(city,days):
    return 1
app = Flask(__name__)
@app.route('/')



if __name__ == '__main__':
    app.run()