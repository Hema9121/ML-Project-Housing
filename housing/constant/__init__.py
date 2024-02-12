from datetime import datetime
import os

root_dir=os.getcwd()


def get_current_time_stamp():
    return datetime.now().strftime("%D__%H:%M:%S")

#print(root_dir)