from flask import Flask
from flask import jsonify
import connexion
from joblib import load
from keras.models import load_model

# Load Model
model = load_model("DogCatCNN3-19.tf")

# Create the application instance

app = connexion.App(__name__, specification_dir="./")
# Read the yaml file to configure the endpoints

app.add_api("DogOrCat.yaml")
# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
