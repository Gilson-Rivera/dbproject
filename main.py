from flask import Flask
from flask_cors import CORS

# import handlers
from Handlers.Fuel import FuelHandler

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def greeting():
    return FuelHandler().getAllFuel()


if __name__ == '__main__':
    app.run()

