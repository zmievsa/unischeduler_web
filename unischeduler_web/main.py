import atexit
import io
import sys
from pathlib import Path
from traceback import format_exception

import unischeduler
from flask import Flask, render_template, request, send_file

from .counting import increment, retrieve_counters, save_counters
from .util import get_logger

CURRENT_DIR = Path(__file__).parent
PATH_TO_COUNTER_DB = CURRENT_DIR / "data/counters.ini"
PATH_TO_LOG = CURRENT_DIR / "data/debug.log"
COUNTER_NAMES = ("total_uses", "successful_uses", "unknown_error")


app = Flask(__name__)
counters = retrieve_counters(PATH_TO_COUNTER_DB, COUNTER_NAMES)
atexit.register(save_counters, PATH_TO_COUNTER_DB, counters)
log = get_logger(PATH_TO_LOG)
log.info("Application start")


@app.route('/')
def main_page():
    return render_template("main.html", successful_uses_count=counters['successful_uses'].value)


@app.route('/make_ical/')
def make_ical():
    increment(counters['total_uses'])
    try:
        schedule = request.args.get("schedule")
        isUCF = bool(request.args.get("isUCF"))
        response = send_file(
            io.BytesIO(unischeduler.main(schedule, isUCF)),
            mimetype="text/calendar",
            as_attachment=True,
            attachment_filename="Classes.ics")
    except unischeduler.util.SchedulerError as e:
        return str(e)
    except Exception as e:
        increment(counters['unknown_error'])
        error = ''.join(format_exception(*sys.exc_info()))
        log.error(f"isUCF={isUCF}\n{error}")
        return "An unknown error occured. Contact my developer and he'll fix it ASAP."
    else:
        increment(counters['successful_uses'])
        return response


@app.route('/guide/')
def guide_page():
    return send_file("static/README.pdf", mimetype="application/pdf")
