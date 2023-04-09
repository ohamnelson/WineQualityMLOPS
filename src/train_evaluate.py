# Laod train and test files
# train the algorithm
# save the metrics and parameters(hyper-parameter)

import os
import sys
import argparse
import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from get_data import read_params
import joblib # used to save the model
import json

def eval_metrics(actual, predicted):
    """
    Return the rmse, mae and r2 of a model; given its ground truth 
    and predicted data.
    """
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)

    return rmse, mae, r2

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_y = train[target]
    test_y = test[target]

    # dropping the target column
    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    # initializing the model parameters
    lm = ElasticNet(alpha=alpha, 
                    l1_ratio=l1_ratio, 
                    random_state=random_state)
    
    # fitting the model
    lm.fit(train_x, train_y)

    prediction = lm.predict(test_x)
    # calculating the metrics
    (rmse, mae, r2) = eval_metrics(test_y, prediction)

    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    scores_file = config["report"]["scores"]
    with open(scores_file, "w") as f:
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        # writing the json object to the file
        json.dump(scores, f, indent=4)

    params_file = config["report"]["params"]
    with open(params_file, "w") as f:
        params = {
            "alpha": alpha,
            "l1_ratio": l1_ratio
        }
        json.dump(params, f, indent=4)


    # Create a directiory called saved_model if it doesn't exist
    os.makedirs(model_dir, exist_ok=True)
    # creating a path in the crearted directory
    model_path = os.path.join(model_dir, "model.joblib")
    # Saving the model in the created path
    joblib.dump(lm, model_path)



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
