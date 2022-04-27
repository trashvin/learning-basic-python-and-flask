# import libraries
from flask import Flask, render_template, url_for, request
from bmi_calculator_app.library import classify_bmi, compute_bmi
from bmi_calculator_app.model.bmi_data import BMIData

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    data = BMIData(0, '')
    print(str(data))

    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        
        data.bmi = compute_bmi(weight, height)
        data.rating_description = classify_bmi(data.bmi)

    return render_template("index.html", bmi = data)


@app.route("/help")
def help():
    return render_template("faq.html")


if __name__ == '__main__':
    app.run(debug=True)
