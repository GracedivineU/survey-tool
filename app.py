from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import csv

app = Flask(__name__)

# Connect to MongoDB (local or cloud)
client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["participants"]

@app.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        data = {
            "age": int(request.form['age']),
            "gender": request.form['gender'],
            "income": float(request.form['income']),
            "expenses": {
                "utilities": float(request.form.get('utilities', 0)),
                "entertainment": float(request.form.get('entertainment', 0)),
                "school_fees": float(request.form.get('school_fees', 0)),
                "shopping": float(request.form.get('shopping', 0)),
                "healthcare": float(request.form.get('healthcare', 0))
            }
        }
        collection.insert_one(data)
        return redirect('/')
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)


