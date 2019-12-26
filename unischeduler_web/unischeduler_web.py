from flask import Flask, send_file, render_template, request
import io
import unischeduler
from traceback import print_exception
import sys


app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/make_ical/')
def make_ical():
    try:
        schedule = request.args.get("schedule")
        isUCF = bool(request.args.get("isUCF"))
        return send_file(
            io.BytesIO(unischeduler.main(schedule, isUCF)),
            mimetype="text/calendar",
            as_attachment=True,
            attachment_filename="Classes.ics")
    except unischeduler.util.SchedulerError as e:
        return str(e)
    except Exception as e:
        with open("log", 'a') as f:
                print(e)
                f.write(f"\nisUCF={isUCF}\n{schedule}\n")
                print_exception(*sys.exc_info(), file=f)
        return "An unknown error occured. Contact my developer and he'll fix it ASAP."


@app.route('/guide/')
def guide_page():
    return send_file("static/README.pdf", mimetype="application/pdf")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)