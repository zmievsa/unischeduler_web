# TODO: Add logging

from flask import Flask, send_file, render_template, request
import io
import unischeduler
from traceback import print_exception
import sys
import atexit
from counting import retrieve_counters, save_counters, increment
from pathlib import Path 

CURRENT_DIR = Path(__file__).parent
PATH_TO_COUNTER_DB = CURRENT_DIR / "counters.ini"
COUNTER_NAMES = ("total_uses", "successful_use", "unknown_error")


app = Flask(__name__)
counters = retrieve_counters(PATH_TO_COUNTER_DB, COUNTER_NAMES)
atexit.register(save_counters, PATH_TO_COUNTER_DB, counters)

@app.route('/')
def main_page():
    return render_template("main.html")


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
        with open(CURRENT_DIR / "log", 'a') as f:
                print(f"Unknown error: {e}")
                print_exception(*sys.exc_info(), file=f)
        return "An unknown error occured. Contact my developer and he'll fix it ASAP."
    else:
        increment(counters['successful_use'])
        return response


@app.route('/guide/')
def guide_page():
    return send_file("static/README.pdf", mimetype="application/pdf")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)