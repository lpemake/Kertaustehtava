import json
from flask import Flask, render_template, request, Response
app = Flask(__name__)

# TODO: tee lista mittauksia varten
positiondata = []

# TODO: avaa sivun result.html ja näyttää mittaukset siinä
@app.route('/')
def get_all_measurements_page():
    return render_template("result.html", result = positiondata)

# TODO: avaa sivun result.html ja näyttää mittaukset siinä
@app.route('/chart/')
def get_all_measurements_page_chart():
    return render_template("chart.html", result = positiondata)    

# TODO: ota vastaan HTTP POSTilla lähetty mittaus ja laita se taulukkoon
@app.route('/newmeasurement/', methods = ['POST'])
def new_measurement():
    meas = request.get_json(force=True)
    positiondata.append(meas)
    return json.dumps(meas, indent=True)

if __name__ == '__main__':
   app.run(debug = True)
   