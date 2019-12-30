import logging
from multiprocessing import Lock
import sys


class LockedLogger(logging.Logger):
    """ Simple logger that locks every transaction """
    def __init__(self, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = lock

    def _log(self, *args, **kwargs):
        with self.lock:
            return super()._log(*args, **kwargs)



def get_logger(log_path):
    log = LockedLogger(Lock(), "Unischeduler_web")
    log.setLevel("DEBUG")
    sdtout_handler = logging.StreamHandler(sys.stdout)
    sdtout_handler.setLevel("DEBUG")
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel("INFO")
    log.addHandler(sdtout_handler)
    log.addHandler(file_handler)
    return log
