
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 7,
        "category": "largest car producer",
        "word": "Germany"
    },
    {
        "inputs": 6,
        "category": "The Most Visited Country",
        "word": "France"
    },
    {
        "inputs": 13,
        "category": "Invented golf",
        "word": "UnitedKingdom"
    },
        {
        "inputs": 5,
        "category": "Invented pizza",
        "word": "Italy"
    },
            {
        "inputs": 7,
        "category": "Hitler's birthplace",
        "word": "Austria"
    },



]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()