from configparser import ConfigParser
from multiprocessing import Value
from pathlib import Path
from typing import Dict


def retrieve_counters(path_to_db, counter_names) -> Dict[str, Value]:
    config = ConfigParser()
    path = Path(path_to_db)
    if not path.exists:
        path.touch()
    config.read(path_to_db)
    return {name: Value('i', config.getint("DEFAULT", name, fallback=0)) for name in counter_names}


def save_counters(path_to_db, counters: dict):
    counters = {name: counters[name].value for name in counters}
    config = ConfigParser(counters)
    with open(path_to_db, "w") as f:
        config.write(f)


def increment(counter: Value):
    with counter.get_lock():
        counter.value += 1
