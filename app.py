from flask import Flask, render_template, request, jsonify
from src.get_data import read_params
import os
import yaml
import joblib
import numpy as np

params_path = "params.yaml"
webapp_root = "webapp"

static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


def predict(data):
    """This function takes the data from the webform,
    loads the model and makes a prediction on the data.

    Args: 
        data (_type_): list

    Returns:
        _type_: float
    """
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]

def api_response(request):
    try:
        data = np.array([list(request.json.values())])
        response = predict(data)
        response = {"response": response}
        return response
    except Exception as e:
        print(e)
        error = {"error": "Not available"}
        return error


# The route decorator binds the function to the URL
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # this handles request coming from a web form
            if request.form:
                data = dict(request.form).values()
# since data is coming from a form, it'll be represented as a string. The data has to be converted to a float
                data = [list(map(float, data))]
                response = predict(data)
                return render_template("index.html", response=response)

# this handles request coming from an API
            elif request.json:
                response = api_response(request)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Not available"}
            return render_template("404.html", error=error)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
