from flask import Flask, render_template, request
from sklearn.neighbors import KNeighborsClassifier
import os

app = Flask(__name__)

# Training data
# [income, credit_score, loan_amount]
data = [
    [80000, 750, 10000],
    [60000, 700, 15000],
    [90000, 800, 20000],
    [75000, 720, 12000],
    [50000, 680, 18000],
    [40000, 600, 25000],
    [30000, 550, 30000],
    [25000, 500, 35000],
    [20000, 480, 40000],
    [15000, 450, 45000],
]

results = [
    "Approved","Approved","Approved","Approved","Approved",
    "Rejected","Rejected","Rejected","Rejected","Rejected"
]

model = KNeighborsClassifier()
model.fit(data, results)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    income = int(request.form["income"])
    credit_score = int(request.form["credit_score"])
    loan_amount = int(request.form["loan_amount"])xx

    prediction = model.predict(
        [[income, credit_score, loan_amount]]
    )[0]

    return render_template("result.html",
        result=prediction,
        income=income,
        credit_score=credit_score,
        loan_amount=loan_amount
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)