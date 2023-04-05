import os
import pandas as pd
import argparse 
from get_data import read_params, get_data

def load_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    # replacinng the space in column names with underscore
    new_cols = [col.replace(" ", "_") for col in df.columns]
    # getting the directory of the raw dataset 
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    # saving the data 
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_save(config_path=parsed_args.config)  