import multiprocessing
import logging
import sys

def get_logger(log_path):
    log = multiprocessing.get_logger()
    log.setLevel("DEBUG")
    sdtout_handler = logging.StreamHandler(sys.stdout)
    sdtout_handler.setLevel("DEBUG")
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel("INFO")
    log.addHandler(sdtout_handler)
    log.addHandler(file_handler)
    return log