import logging
from datetime import datetime
from housing.constant import get_current_time_stamp,root_dir
import os
import pandas as pd


logs_dir="Logs"

def file_name():
    return f"log_{get_current_time_stamp}.log"

log_filename=file_name()
logs_path=os.path.join(root_dir,logs_dir)
os.makedirs(logs_path,exist_ok=True)
logs_file_path=os.path.join(logs_path,log_filename)

logging.basicConfig(filename=logs_file_path,
                    filemode="w",
                    level=logging.INFO,
                    format="[%(asctime)s]-%(levelname)s-%(lineno)d-%(filename)s-%(funcName)s-%(message)s"
                    )


def get_log_dataframe(filepath:str):
    data=[]
    with open(filepath) as f:
        for line in f.readlines():
            data.append(line.split("-"))
    
    df=pd.DataFrame(data)
    columns=["asctime","level_name","line_num","file","function","message"]
    df.columns=columns
    df["log_message"]=df["asctime"].astype(str)+"****"+df["message"]
    
    return df["log_message"]
    