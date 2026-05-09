from flask import Flask, render_template, request
from PIL import Image
import random

app = Flask(__name__)

# Disease data
disease_info = {
    "Healthy": {
        "solution": "Your plant is healthy 🌱",
        "prevention": "Continue proper watering and sunlight."
    },

    "Leaf Spot": {
        "solution": "Use neem oil spray or copper fungicide.",
        "prevention": "Avoid excess moisture on leaves."
    },

    "Blight": {
        "solution": "Remove infected leaves and use fungicide.",
        "prevention": "Maintain proper air circulation."
    }
}

# Fake prediction for demo
def predict_image(img):
    return random.choice(["Healthy", "Leaf Spot", "Blight"])

@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    solution = None
    prevention = None

    if request.method == "POST":

        file = request.files["image"]
        img = Image.open(file)

        result = predict_image(img)

        solution = disease_info[result]["solution"]
        prevention = disease_info[result]["prevention"]

    return render_template(
        "index.html",
        result=result,
        solution=solution,
        prevention=prevention
    )

if __name__ == "__main__":
    app.run(debug=True)