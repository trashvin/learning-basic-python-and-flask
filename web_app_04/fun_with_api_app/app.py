# import libraries
from flask import Flask, render_template, url_for, request
import requests

from fun_with_api_app.model.age_prediction import AgePrediction
from fun_with_api_app.model.sample_list import SampleList

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/genderReveal",methods=['POST','GET'])
def gender_reveal():
    prediction = AgePrediction()
    if request.method == 'POST':
        name = request.form.get('name')

        request_url = f'https://api.genderize.io?name={name}'
        response = requests.get(request_url)
        return_data = response.json()
        prediction.parse(return_data)

    return render_template("predict_gender.html", prediction = prediction )

@app.route("/getNationality")
def get_nationality():
    samples = []
    for i in range(10):
        sample = SampleList()
        sample.id = i
        sample.name = f'Sample {i}'
        samples.append(sample)

    return render_template("guess_nationality.html", samples=samples)

@app.route("/imBored", methods=['POST','GET'])
def im_bored():
    activity = ''
    if request.method == 'POST':
        request_url = 'https://www.boredapi.com/api/activity/'
        response = requests.get(request_url)
        return_data = response.json()
        activity = return_data['activity']

    return render_template("im_bored.html", task=activity)


if __name__ == '__main__':
    app.run(debug=True)
