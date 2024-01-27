# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import time
import logging 


# this can be used for testing locally, to see how long the run time is for
# certain functions
def time_decorator(func):
    def measure_time(*args, **kwargs):            
        # getting the returned value
        s = time.time()
        res = func(*args, **kwargs)
        e = time.time()
        mins_elapsed = (e - s) / 60
        print(f'Time elapsed for {func.__name__}: {mins_elapsed} min')
        return res      
    return measure_time


def get_logger():
    logger = logging.getLogger('envdesign_model_logger')
    logger.setLevel(logging.INFO)
    return logger
