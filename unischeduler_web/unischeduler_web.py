from flask import Flask, send_file, render_template, request
import io
import unischeduler


app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/make_ical/')
def make_ical():
    try:
        return send_file(
            io.BytesIO(unischeduler.main(request.args.get("schedule"), bool(request.args.get("isUCF")))),
            mimetype="text/calendar",
            as_attachment=True,
            attachment_filename="Classes.ics")
    except unischeduler.util.SchedulerError as e:
        return str(e)


@app.route('/guide/')
def guide_page():
    return send_file("static/README.pdf", mimetype="application/pdf")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host='0.0.0.0', port=80)