from flask import Flask, send_file, render_template, request
import io
import unischeduler


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/make_ical/')
def make_ical():
    i = request.args.get("schedule")
    return send_file(
        io.BytesIO(unischeduler.main(i, bool(request.args.get("isUCF")))),
        mimetype="text/calendar",
        as_attachment=True,
        attachment_filename="Classes.ics")
