from flask import Flask, render_template, session, request, redirect
from hotel_reservation import predict_reservation
app = Flask(__name__)
app.secret_key = 'thanhnghi1421`'
@app.route('/')
def index():
    return render_template('index.html', state="")

@app.route('/', methods=['POST'])
def predict():
    question = dict(request.form)

    if 'required_car_parking_space' not in question:
        question['required_car_parking_space'] = 0
    else:
        question['required_car_parking_space'] = 1

    if 'repeated_guest' not in question:
        question['repeated_guest'] = 0
    else:
        question['repeated_guest'] = 1

    answer = predict_reservation(question)
    return render_template('index.html', state=answer);


if __name__ == "__main__":
    app.run(debug=True)